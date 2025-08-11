import uiautomator2 as u2
from utils.xml_tools import xmlElementToUiObject,slip
class HomePage():
    widgets={
        "mainContentXpath":'//androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/androidx.viewpager.widget.ViewPager[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]/androidx.viewpager.widget.ViewPager[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/androidx.viewpager.widget.ViewPager[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/androidx.recyclerview.widget.RecyclerView[1]',
        "tabBar":'//androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/androidx.viewpager.widget.ViewPager[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]/androidx.viewpager.widget.ViewPager[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]',
        "loadImage":'//androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/androidx.viewpager.widget.ViewPager[1]/android.view.ViewGroup[1]/android.widget.FrameLayout[1]/androidx.viewpager.widget.ViewPager[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/androidx.viewpager.widget.ViewPager[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.widget.ImageView[1]',
        "search":'//*[@content-desc="搜索"]'
    }
    def __init__(self,d):
        self.tabBar = d(className="android.view.ViewGroup",instance=0).child(className="androidx.recyclerview.widget.RecyclerView",instance=0)
        self.postContainer=d(className="androidx.viewpager.widget.ViewPager",instance=2) \
        .child(className="android.widget.FrameLayout").child(className="android.widget.FrameLayout") \
        .child(className="android.view.ViewGroup").child(className="androidx.recyclerview.widget.RecyclerView")
        
        for key,value in self.widgets.items():
            selector = d.xpath(value)
            if selector.wait(timeout=5):
                setattr(self, key, selector.get())
            else:
                setattr(self, key, None)  # 或者抛异常，提示元素没找到
    def clickTabBar(self, instance=0):
        """点击兴趣标签

        Args:
            instance (int, optional): 索引第几个标签. Defaults to 0.
        """
        self.tabBar.child(className="android.widget.FrameLayout",instance=instance).click()
        
    def clickPost(self,instance=0):
        """点击帖子

        Args:
            instance (int, optional): 索引第几个帖子. Defaults to 0.
        """
        self.postContainer.child(className="android.widget.FrameLayout",instance=instance*3).click()
    def clickLike(self,instance=0):
        """点击帖子点赞

        Args:
            instance (int, optional): 索引第几个帖子. Defaults to 0.
        """
        self.postContainer.child(className="android.widget.FrameLayout",instance=instance*3+1).child(className="android.widget.TextView",instance=1).click()
    def getLikeNum(self,instance=0):
        """获取帖子点赞数

        Args:
            instance (int, optional): 索引第几个帖子. Defaults to 0.

        Returns:
            int: 点赞数
        """
        return int(self.postContainer.child(className="android.widget.FrameLayout",instance=instance*3+1).child(className="android.widget.TextView",instance=1).get_text())
    
    def slipMainContent(self):
        slip(self.d,self.mainContentXpath,1,0.3,1)
    def updateMainContent(self):
        slip(self.d,self.mainContentXpath,0,0.3,1)
    def clickPost(self):
        self.getPost().click()
    def getPost(self):
        selector = self.d.xpath('//*[contains(@content-desc, "笔记") or contains(@content-desc, "视频")]')
        return xmlElementToUiObject(self.d,selector)
    def clickSearch(self):
        if self.search:
            self.search.click()
        else:
            raise ValueError("搜索元素未找到")
        
