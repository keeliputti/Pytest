from pathlib import Path

from pytest_bdd import scenario, scenarios, given, when, then
import pytest

featureFileDir = "myfeatures"
featureFile = "first101.feature"
BASE_DIR = Path(__file__).resolve().parent
FEATURE_FILE = BASE_DIR.joinpath(featureFileDir).joinpath(featureFile)

def pytest_configure(): #global_variable
    pytest.ATM = 0

scenarios(FEATURE_FILE)

# @scenario(FEATURE_FILE, "Withdrawal of money")
# def test_withdrawal():
#     print("End of withdrawal test")
#     pass

@given("the account balance is 100")
def current_balance():
    pytest.ATM = 100

@when("the account holder withdrawas 30")
def withdraw_amount():
    pytest.ATM = pytest.ATM - 300

@then("the account balance should be 70")
def final_balance():
    assert pytest.ATM == 70

# @scenario(FEATURE_FILE, "Removal of items from set")
# def test_removalOfItems():
#     pass

@given("A set of 3 fruits", target_fixture="myset")
def current_balance():
    myset = {"apple", "banana", "cherry"}
    return myset

@when("We remove a fruit from the set")
def remove_fruit(myset):
    myset.pop()
    print(myset)

@then("the set will have 2")
def final_set(myset):
    assert len(myset) == 2
