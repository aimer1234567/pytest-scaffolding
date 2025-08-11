from utils.data_mapping import data_mapping, data_driven_test
from config import test_init
from pages.homePage import HomePage
from pages.searchPage import SearchPage
from utils.xml_tools import isCurrentActivity

def test_updateMainContent(test_init):
    d=test_init
    homePage=HomePage(d)   
    homePage.updateMainContent()

def test_slipMainContent_load(test_init):
    d=test_init
    homePage=HomePage(d)
    for i in range(2):
        homePage.slipMainContent()
    assert homePage.getPost().exists
@data_driven_test
def test_search(test_init,data):
    d=test_init
    homePage=HomePage(d)
    homePage.clickSearch()
    assert isCurrentActivity(d, "com.xingin.alioth.search.GlobalSearchActivity")
    searchPage=SearchPage(d)
    searchPage.input(data)
    assert isCurrentActivity(d,"com.xingin.alioth.search.GlobalSearchActivity")
    
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
    assert likeAfter==likeBefore-1
