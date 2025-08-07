# 一个pytest搭建的测试框架
@data_driven_test：目前封装@pytest.mark.parametrize，实现了数据文件目录映射装饰器，实现参数化测试
```
@data_driven_test
def test_1(hhh,ddd,mmm):
    print(f"测试数据：{hhh} - {ddd} - {mmm}")
```