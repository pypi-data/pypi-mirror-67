from package_dev import say_hello
def test_helloworld_no_params():
    assert say_hello() == "Hello, world!"

def test_helloworld_with_params():
    assert say_hello("Everyone") == "Hello, Everyone!"