import pytest
@pytest.fixture(scope="session")
def login():
    print("先登录")
testdata = [
    ("1+1",2),
    ("1+3",4),
    pytest.param("1+1",3,marks=pytest.mark.xfail)
]
@pytest.mark.parametrize("test_input,expect",testdata)
def test_demo(login,test_input,expect):
    # user = test_input.get("user")
    # print(user)
    # psw = test_input.get("psw")
    # print(psw)
    result = eval(test_input)
    assert result == expect
class TestDemo():
    def test_1(self):
        b = "hello world"
        assert "hello" in b
