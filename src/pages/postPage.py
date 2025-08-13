from utils.ui_object_tools import slip,clickSafe
import uiautomator2 as u2 
class PostPage():
    def __init__(self,d:u2.Device):
        self.d = d
        # 帖子主屏幕
        self.PostContainer = d(className="android.widget.LinearLayout").\
            child(className="android.widget.RelativeLayout").\
            child(className="android.view.ViewGroup")
        self.reviewButton = d(className="android.widget.RelativeLayout").child(className="android.widget.FrameLayout")\
            .child(className="android.widget.TextView",text="说点什么...")
        # 评论输入框
        self.reviewInput=d(className="android.view.ViewGroup").child(className="android.widget.EditText")
        # 发送评论按钮
        self.sendReviewButton = d(className="android.view.ViewGroup").child(className="android.view.ViewGroup").child(className="android.widget.TextView",text="发送")
        # 评论数
        self.reviewNum = d(className="android.widget.RelativeLayout").child(className="android.widget.FrameLayout")\
            .child(className="android.widget.Button",instance=2).child(className="android.widget.TextView",instance=0)  
        # 广告按钮
        self.adButton1=d(className="android.widget.FrameLayout").child(className="android.widget.FrameLayout",instance=0).child(className="android.widget.TextView",text="立即预约")
        self.adButton2=d(className="android.widget.FrameLayout").child(className="android.widget.FrameLayout",instance=0).child(className="android.widget.TextView",text="立即咨询")
    def clickReview(self):
        """点击评论按钮
        """
        clickSafe(self.reviewButton)
        return self
    def isAdButton(self):
        if self.adButton1.exists() or self.adButton2.exists():
            return True
        return False
    def inputReview(self,text:str):
        """输入评论

        Args:
            text (_type_): _description_
        """
        if not self.reviewInput.exists(timeout=5):
            raise Exception("评论输入框不存在")
        self.reviewInput.send_keys(text)
        return self
        
    def clickSendReview(self):
        """点击发送评论按钮
        """
        el=self.sendReviewButton
        clickSafe(el)
        
    def isSendReview(self):
        """判断评论是否发送成功

        Returns:
            bool: 发送成功返回True，失败返回False
        """
        return not self.reviewInput.exists()
    
    def isEnableClickSend(self)->bool:
        """是否能点击发送评论
        """
        return self.sendReviewButton.info.get('enabled')
        
    def getReviewNum(self)->int:
        """获取评论数 
        Returns:
            int: 评论数
        """
        str=self.reviewNum.get_text()
        return int(str)
        