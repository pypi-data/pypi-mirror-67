# Common test class with miscellaneous utilities and fixtures
import logging
import os
import shutil
from pathlib import Path

import pytest
from _pytest.fixtures import FixtureRequest


@pytest.mark.usefixtures("logs")
class TestHelper:
    # Output folder
    @property
    def output_folder(self) -> Path:
        return self.root_folder / "out" / "tests"

    # Test folder (running)
    @property
    def test_folder(self) -> Path:
        return self.output_folder / "__running__" / self.worker / self.test_name

    # Test folder (final)
    @property
    def __test_final_folder(self) -> Path:
        return self.output_folder / self.test_name

    # Test name
    @property
    def test_name(self) -> str:
        return Path(os.environ["PYTEST_CURRENT_TEST"].split(" ")[0]).name.replace("::", "_").replace(".py", "")

    # Worker name in parallelized tests
    @property
    def worker(self) -> str:
        return os.environ["PYTEST_XDIST_WORKER"] if "PYTEST_XDIST_WORKER" in os.environ else "master"

    # Per-test logging management
    @pytest.fixture
    def logs(self, request: FixtureRequest):
        # Set root folder
        self.root_folder = Path(request.config.rootdir).absolute().resolve()

        # Prepare test folder
        shutil.rmtree(self.test_folder, ignore_errors=True)
        shutil.rmtree(self.__test_final_folder, ignore_errors=True)
        self.test_folder.mkdir(parents=True, exist_ok=False)

        # Install logging
        for handler in logging.root.handlers[:]:
            logging.root.removeHandler(handler)
        logging.basicConfig(
            level=logging.DEBUG,
            format=f"%(asctime)s.%(msecs)03d [{self.worker}/%(name)s] %(levelname)s %(message)s - %(filename)s:%(funcName)s:%(lineno)d",
            datefmt="%Y-%m-%d %H:%M:%S",
            filename=str(self.test_folder / "pytest.log"),
            filemode="w",
        )
        logging.info("-----------------------------------------------------------------------------------")
        logging.info(f"    New test: {self.test_name}")
        logging.info("-----------------------------------------------------------------------------------")

        # Return to test
        yield

        # Flush logs
        logging.info("-----------------------------------------------------------------------------------")
        logging.info(f"    End of test: {self.test_name}")
        logging.info("-----------------------------------------------------------------------------------")
        logging.shutdown()

        # Move folder
        shutil.move(self.test_folder, self.__test_final_folder)
        self.test_folder.parent.rmdir()
