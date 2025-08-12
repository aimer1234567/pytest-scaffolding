from utils.data_mapping import data_mapping, data_driven_test
from config import test_init
from pages.homePage import HomePage
from pages.searchPage import SearchPage
from utils.xml_tools import isCurrentActivity
import time

def test_updatePostContainer(test_init):
    """测试下拉刷新

    Args:
        test_init (_type_): _description_
    """
    d=test_init
    homePage=HomePage(d) 
    updateBeforeOneTitle=[homePage.getPostDescription(instance=i) for i in range(3)]
    homePage.updatePostContainer()
    time.sleep(2)
    updateAfterOneTitle=[homePage.getPostDescription(instance=i) for i in range(3)]
    assert updateBeforeOneTitle!=updateAfterOneTitle  #通过前后前三个帖子标题是否相同，判断帖子是否更新

def test_slipPostContentLoad(test_init):
    """测试滑动帖子内容，是否加载新帖子

    Args:
        test_init (_type_): _description_
    """
    d=test_init
    homePage=HomePage(d)
    updateBeforeOneTitle=[homePage.getPostDescription(instance=i) for i in range(3)]
    for i in range(2):
        homePage.slipPostContainer()
    updateAfterOneTitle=[homePage.getPostDescription(instance=i) for i in range(3)]
    assert updateBeforeOneTitle!=updateAfterOneTitle  #通过前后前三个帖子标题是否相同，判断帖子是否更新
    
def test_clickLike(test_init):
    """点击喜欢，判断喜欢数+1

    Args:
        test_init (_type_): _description_
    """
    d=test_init
    homePage=HomePage(d)
    likeBefore=homePage.getLikeNum()
    homePage.clickLike()
    likeAfter=homePage.getLikeNum()
    if likeBefore<10000:   # 如果点赞数大于10000，不会显示个位数，无法判断
        assert likeAfter==likeBefore+1
    
def test_unLike(test_init):
    """取消喜欢，判断喜欢数-1

    Args:
        test_init (_type_): _description_
    """
    d=test_init
    homePage=HomePage(d)
    likeBefore=homePage.getLikeNum()
    homePage.clickLike()
    likeAfter=homePage.getLikeNum()
    if likeBefore<=10000:   # 如果点赞数大于10000，不会显示个位数，无法判断
        assert likeAfter==likeBefore-1

@data_driven_test
def test_search(test_init,data):
    d=test_init
    homePage=HomePage(d)
    homePage.clickSearch()
    assert isCurrentActivity(d, "com.xingin.alioth.search.GlobalSearchActivity")
    searchPage=SearchPage(d)
    searchPage.input(data)
    assert isCurrentActivity(d,"com.xingin.alioth.search.GlobalSearchActivity")
    d.press("back")
    d.press("back")