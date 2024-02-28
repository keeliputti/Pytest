from pytest_topics.utils.myconfigparser import *
from pytest_topics.utils.ConfigFileParser import ConfigFileParser

config = ConfigFileParser("prod.ini")

def test_getGmailUrl():
    print(getGmailUrl())

def test_getOutlookUrl():
    print(config.getOutlookUrl())