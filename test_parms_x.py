import pytest
testdata1 = [
    ("222", ),
    ("yoy", ),
    ("中文", ),
]
testdata2 = [
    ("222", ),
    ("yoyo", ),
    ("中文", ),
]
@pytest.mark.parametrize("input1",testdata1)
@pytest.mark.parametrize("input2",testdata2)
def test_demo(input1,input2):
    print("测试组合：%s,%s"%(input1,input2))
    result = True
    assert result
