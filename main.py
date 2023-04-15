import pytest
import sys


class MyPlugin:

    def pytest_sessionfinish(self):
        print(r'*** rest run reporting finishing ***')


if __name__ == "__main__":
    # Passing --pdb it will run the debugger when fail
    # Pssing -x the test will stop when first test fail
    # Passing --ff fail first is setup
    # You could pass -k to define which test you want run (based on method name)
    # You could pass -s to show console outputs (everything from print)
    # -rs: show the reason of skip
    sys.exit(
        pytest.main(
            ["--pdb", "-rs", "--ff", "-x", "-v", "-qq", "--junitxml", "report.xml"],
            plugins=[MyPlugin()]))
