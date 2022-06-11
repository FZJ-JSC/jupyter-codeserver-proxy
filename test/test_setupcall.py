def test_setupcall():
    """
    Test the call of the setup function
    """
    import os
    import jupyter_codeserver_proxy as jx

    os.environ["CODESERVER_BIN"] = "codeserver"

    print("\nRunning test_setupcall...")
    print(jx.setup_codeserver())
