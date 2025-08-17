import allure

def pytest_exception_interact(node, call, report):
    if report.failed:
        if isinstance(call.excinfo.value, AssertionError):
            report.outcome = "failed"
            allure.dynamic.label("error_type", "断言失败")
        else:
            report.outcome = "broken"
            allure.dynamic.label("error_type", "程序异常")