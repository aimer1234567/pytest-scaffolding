postContainer=d(className="android.view.ViewGroup") \
        .child(className="androidx.viewpager.widget.ViewPager",instance=0).child(className="android.view.ViewGroup") \
        .child(className="android.widget.FrameLayout").child(className="androidx.recyclerview.widget.RecyclerView") \
        .child(className="android.widget.FrameLayout",instance=9) \
        .child(className="android.widget.RelativeLayout") \
        .child(className="android.widget.ImageView",instance=0).click()
        
class SearchResultPage():
    def __init__(self,d):
        self.d = d
        
    def clickPost(self,instance:int=1):
        """点击帖子

        Args:
            instance (int, optional): 索引第几个帖子. Defaults to 1.
        """
        if instance < 1 or instance > 4:
            raise ValueError("索引要在1到4之间")
        self.d(className="android.view.ViewGroup") \
            .child(className="androidx.viewpager.widget.ViewPager",instance=0).child(className="android.view.ViewGroup") \
            .child(className="android.widget.FrameLayout").child(className="androidx.recyclerview.widget.RecyclerView") \
            .child(className="android.widget.FrameLayout",instance=instance*2) \
            .child(className="android.widget.RelativeLayout") \
            .child(className="android.widget.ImageView",instance=0).click()
            
        