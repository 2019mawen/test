def setup_function():
    print("只对函数用例生效，每个用例都会执行")
def teardown_function():
    print("只对函数的用户结束之后执行，每个用例都会执行")
def test_a():
    a=1
    print("\n运行步骤：1")
    assert a>0,"失败原因"
def hello():
    print("hello")