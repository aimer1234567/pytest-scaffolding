class SearchPage():
    widgets={
        "searchInput":'//*[@text="搜索, "]',
        "searchButton":'//*[@text="搜索"]',
    }
    def __init__(self,d):
        self.d = d
        for key,value in self.widgets.items():
            selector = d.xpath(value)
            if selector.wait(timeout=5):
                setattr(self, key,selector)
            else:
                setattr(self, key, None)  # 或者抛异常，提示元素没找到
    
    def input(self,text):
        self.searchInput.set_text(text)
        self.searchButton.click()