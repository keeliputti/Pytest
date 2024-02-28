
def test_arftest01(CmdOpt):
    # print(f"Read config file: {CmdOpt.readline()}")
    assert CmdOpt.readline().index("Lab")
