import uiautomator2 as u2
from utils.ui_object_tools import slip,clickSafe
class HomePage():
    def __init__(self,d:u2.Device):
        self.d = d
        # 兴趣标签
        self.tabBar = d(className="android.view.ViewGroup",instance=0).child(className="androidx.recyclerview.widget.RecyclerView",instance=0)
        # 主内容
        self.postContainer=d(className="androidx.viewpager.widget.ViewPager",instance=2) \
            .child(className="android.widget.FrameLayout").child(className="android.widget.FrameLayout") \
            .child(className="android.view.ViewGroup").child(className="androidx.recyclerview.widget.RecyclerView")
        # 加载符号
        self.load=d(className="androidx.viewpager.widget.ViewPager",instance=2) \
            .child(className="android.widget.FrameLayout").child(className="android.widget.FrameLayout") \
            .child(className="android.view.ViewGroup").child(className="android.widget.ImageView")
        self.searchButton=d(description="搜索") # 通搜索按钮

    def isLoadNum(self):
        """获取当前页面子元素个数，通过子元素个数判断是否加载
        """
        return self.load.count
    def clickTabBar(self, instance=0):
        """点击兴趣标签

        Args:
            instance (int, optional): 索引第几个标签. Defaults to 0.
        """
        el=self.tabBar.child(className="android.widget.FrameLayout",instance=instance)
        clickSafe(el)
        
    def clickPost(self,instance=0):
        """点击帖子

        Args:
            instance (int, optional): 索引第几个帖子. Defaults to 0.
        """
        el=self.postContainer.child(className="android.widget.FrameLayout",instance=instance*3)
        clickSafe(el)
    def clickTextPostRandom(self):
        """点击文字帖子非广告，随机点击一个
        """
        for i in range(3):
            if self.getPostDescription(instance=i).split(" ")[0]=="笔记" and ("商业" not in self.getPostDescription(instance=i)):
                self.clickPost(instance=i)
                return
        slip(self.d,self.postContainer,1,0.3,2)
        self.clickTextPostRandom()
            
        el=self.postContainer.child(className="android.widget.FrameLayout",instance=1)
        clickSafe(el)
    def getPostDescription(self,instance=0):
        """获取帖子标题和其作者信息

        Args:
            instance (int, optional): 索引第几个帖子. Defaults to 0.

        Returns:
            str: 帖子标题
        """
        element = self.postContainer.child(className="android.widget.FrameLayout", instance=instance*3)
        if not element.exists:
            raise Exception(f"帖子索引 {instance} 没有发现")
        return self.getDescription(element)
    def clickLike(self,instance=0):
        """点击帖子点赞

        Args:
            instance (int, optional): 索引第几个帖子. Defaults to 0.
        """
        el=self.postContainer.child(className="android.widget.FrameLayout",instance=instance*3+1).child(className="android.widget.TextView",instance=1)
        clickSafe(el)
    def getLikeNum(self,instance=0):
        """获取帖子点赞数

        Args:
            instance (int, optional): 索引第几个帖子. Defaults to 0.

        Returns:
            int: 点赞数
        """
        likeNumStr=self.postContainer.child(className="android.widget.FrameLayout",instance=instance*3+1).child(className="android.widget.TextView",instance=1).get_text()
        if "万" in likeNumStr:
            likeNum=float(likeNumStr.split("万")[0])
            # 转换为实际数值（1万 = 10000）
            likeNum = int(likeNum * 10000)
        else:
            likeNum=int(likeNumStr)
        return likeNum
        
    def slipPostContainer(self):
        """向下滑动内容
        """
        slip(self.d,self.postContainer,1,0.3,2)
    def updatePostContainer(self):
        """刷新内容
        """
        slip(self.d,self.postContainer,0,0.3,1)
    def clickSearch(self):
        """点击搜索按钮
        """
        el=self.searchButton
        clickSafe(el)
                
    def getDescription(self,el:u2.UiObject)->str:
        """获取元素的描述

        Args:
            el (u2.UiObject): _description_

        Returns:
            str: _description_
        """
        try:
            # 检查元素是否存在
            if el.exists:
                info = el.info
                return info.get('contentDescription', '')
            else:
                return ''  
        except Exception as e:
            return ''
    
        
