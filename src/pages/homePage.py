import uiautomator2 as u2
from utils.ui_object_tools import slip,clickSafe
class HomePage():
    def __init__(self,d:u2.Device):
        self.d = d
        # 兴趣标签
        self.tabBar = d(className="android.view.ViewGroup").child(className="androidx.recyclerview.widget.RecyclerView")
        # 主内容
        self.postContainer=d(className="androidx.viewpager.widget.ViewPager") \
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
    def clickTabBar(self, index=0):
        """点击兴趣标签

        Args:
            index (int, optional): 索引第几个标签. Defaults to 0.
        """
        el=self.tabBar.child(className="android.widget.FrameLayout",index=index)
        clickSafe(el)
    def getPost(self,index=0):
        """获取帖子元素

        Returns:
            u2.UiObject: 帖子元素
        """
        return self.postContainer.child(className="android.widget.FrameLayout",index=index)
    
    def isAdvertisement(self,index=0):
        """判断帖子是否为广告

        Args:
            index (int, optional): 帖子索引. Defaults to 0.

        Returns:
            _type_: _description_
        """ 
        return self.getPost(index).child(className="android.widget.TextView",text="广告").exists
        
    def clickPost(self,index=0):
        """点击帖子

        Args:
            index (int, optional): 索引第几个帖子. Defaults to 0.
        """
        el=self.getPost(index)
        clickSafe(el)
    def clickTextPostRandom(self):
        """点击文字帖子非广告，随机点击一个
        """
        for i in range(3):
            if self.getPostDescription(index=i).split(" ")[0]=="笔记" and not self.isAdvertisement(index=i):
                self.clickPost(index=i)
                return
        slip(self.d,self.postContainer,1,0.3,2)
        self.clickTextPostRandom()

    def getPostDescription(self,index=0):
        """获取帖子标题和其作者信息

        Args:
            index (int, optional): 索引第几个帖子. Defaults to 0.

        Returns:
            str: 帖子标题
        """
        element = self.getPost(index)
        if not element.exists:
            raise Exception(f"帖子索引 {index} 没有发现")
        return self.getDescription(element)
    def getLikeButton(self,index=0):
        return self.getPost(index).child(className='android.widget.LinearLayout').\
            child(className='android.widget.LinearLayout').\
            child(className="android.widget.RelativeLayout").\
            child(className="android.widget.TextView")
    def clickLike(self,index=0):
        """点击帖子点赞

        Args:
            index (int, optional): 索引第几个帖子. Defaults to 0.
        """
        clickSafe(self.getLikeButton(index))
    def getLikeNum(self,index=0):
        """获取帖子点赞数

        Args:
            index (int, optional): 索引第几个帖子. Defaults to 0.

        Returns:
            int: 点赞数
        """
        likeNumStr=self.getLikeButton(index).get_text()
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
    
        
