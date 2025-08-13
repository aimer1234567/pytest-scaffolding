from utils.data_mapping import data_driven_test
from config import test_init,homePage,postPage,searchPage,searchResultPage
from pages.homePage import HomePage
from utils.ui_object_tools import isCurrentActivity
import time

def test_updatePostContainer(homePage):
    """测试下拉刷新

    Args:
        test_init (_type_): _description_
    """
    try:
        updateBeforeOneTitle=[homePage.getPostDescription(instance=i) for i in range(3)]
        homePage.updatePostContainer()
        time.sleep(2)
        updateAfterOneTitle=[homePage.getPostDescription(instance=i) for i in range(3)]
    except Exception as e:
        raise e
    assert updateBeforeOneTitle!=updateAfterOneTitle  #通过前后前三个帖子标题是否相同，判断帖子是否更新

def test_slipPostContentLoad(homePage):
    """测试滑动帖子内容，是否加载新帖子

    Args:
        test_init (_type_): _description_
    """
    updateBeforeOneTitle=[homePage.getPostDescription(instance=i) for i in range(3)]
    for i in range(2):
        homePage.slipPostContainer()
    updateAfterOneTitle=[homePage.getPostDescription(instance=i) for i in range(3)]
    assert updateBeforeOneTitle!=updateAfterOneTitle  #通过前后前三个帖子标题是否相同，判断帖子是否更新
    
def test_clickLike(homePage):
    """点击喜欢，判断喜欢数+1

    Args:
        test_init (_type_): _description_
    """
    likeBefore=homePage.getLikeNum()
    homePage.clickLike()
    likeAfter=homePage.getLikeNum()
    if likeBefore<10000:   # 如果点赞数大于10000，不会显示个位数，无法判断
        assert likeAfter==likeBefore+1
    
def test_unLike(homePage):
    """取消喜欢，判断喜欢数-1

    Args:
        test_init (_type_): _description_
    """
    likeBefore=homePage.getLikeNum()
    homePage.clickLike()
    likeAfter=homePage.getLikeNum()
    if likeBefore<=10000:   # 如果点赞数大于10000，不会显示个位数，无法判断
        assert likeAfter==likeBefore-1

@data_driven_test
def test_search(test_init,homePage,searchResultPage,searchPage,data):
    """主页搜索测试，判断是否存在搜索结果

    """
    try:
        d=test_init
        homePage=HomePage(d)
        homePage.clickSearch()
        assert isCurrentActivity(d, "com.xingin.alioth.search.GlobalSearchActivity") # 判断是否进入搜索页面
        searchPage.input(data)
        assert searchResultPage.isPost(1)  # 判断是否有帖子
        assert isCurrentActivity(d,"com.xingin.alioth.search.GlobalSearchActivity")
    except Exception as e:
        raise e
    finally:
        d.press("back")
        d.press("back")