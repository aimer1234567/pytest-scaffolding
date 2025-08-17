# 一个pytest+allure搭建的测试框架
**使用uiautomator2对安卓小红书8.96.0进行测试，采用pageobject模式进行ui测试** 。通过pytest钩子函数，将assert错误和程序异常打上不同标签在allure中展示

## @data_driven_test装饰器
二次封装@pytest.mark.parametrize，实现了数据文件与测试用例映射，自动注入参数。参数化驱动测试，简化测试数据管理
```
@data_driven_test
def test_1(hhh,ddd,mmm):
    print(f"测试数据：{hhh} - {ddd} - {mmm}")
```


后期将封装requests模块，以及数据库操作，压测工具封装，以及内存、CPU、网络、磁盘监控等工具