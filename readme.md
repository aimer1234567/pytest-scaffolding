# 一个pytest搭建的测试框架
@data_driven_test：目前封装@pytest.mark.parametrize，实现了数据文件目录映射装饰器，实现参数化驱动测试，简化测试数据管理
```
@data_driven_test
def test_1(hhh,ddd,mmm):
    print(f"测试数据：{hhh} - {ddd} - {mmm}")
```

后期将封装requests模块，实现接口测试开箱即用<br>以及数据库操作，测试报告生成，压测工具封装，ui自动化测试封装