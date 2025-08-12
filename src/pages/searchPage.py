class SearchPage():
    def __init__(self,d):
        self.d = d
        self.searchButton=d(className="android.widget.RelativeLayout").child(className="android.widget.Button",text="搜索")
        self.searchInput=d(className="android.widget.RelativeLayout").child(className="android.widget.EditText")
    
    def input(self,text):
        self.searchInput.send_keys(text)
        self.searchButton.click()