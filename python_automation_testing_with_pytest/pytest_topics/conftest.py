import os

import pytest

QA_config = "qa.prod"
prod_config = "prod.prod"

def pytest_addoption(parser):
    parser.addoption("--cmdopt", default="QA")

@pytest.fixture()
def CmdOpt(pytestconfig):
    print("\n In CmdOpt fixture")
    opt = pytestconfig.getoption("cmdopt")
    if opt == "Prod":
        f = open(os.path.join(os.path.dirname(__file__), prod_config), "r")
    else:
        f = open(os.path.join(os.path.dirname(__file__), QA_config), "r")
    yield f
