from utils.ui_object_tools import clickSafe
class SearchPage():
    def __init__(self,d):
        self.d = d
        # 搜索按钮
        self.searchButton=d(className="android.widget.RelativeLayout").child(className="android.widget.Button",text="搜索")
        # 搜索输入框
        self.searchInput=d(className="android.widget.RelativeLayout").child(className="android.widget.EditText")
    
    def input(self,text):
        self.searchInput.send_keys(text)
        clickSafe(self.searchButton)