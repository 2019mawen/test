import pytest
@pytest.fixture(scope="session")
#session执行一次
def login():
    print("用例先登录")
@pytest.fixture(scope="function")
def open_a():
    print("打开a页面")