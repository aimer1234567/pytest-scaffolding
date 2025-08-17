from utils.data_mapping import data_driven_test
from config import test_init,homePage,postPage,searchPage,searchResultPage
from pages.homePage import HomePage
from utils.ui_object_tools import isCurrentActivity
import time
import allure

@allure.feature("首页测试")
class TestHomePage:
    @allure.story("测试下拉刷新,加载新帖子")
    def test_updatePostContainer(self,homePage):
        try:
            updateBeforeOneTitle=[homePage.getPostDescription(index=i) for i in range(3)]
            homePage.updatePostContainer()
            time.sleep(2)
            updateAfterOneTitle=[homePage.getPostDescription(index=i) for i in range(3)]
        except Exception as e:
            raise e
        assert updateBeforeOneTitle!=updateAfterOneTitle  #通过前后前三个帖子标题是否相同，判断帖子是否更新

    @allure.story("测试滑动帖子内容,加载新帖子")
    def test_slipPostContentLoad(self,homePage):
        updateBeforeOneTitle=[homePage.getPostDescription(index=i) for i in range(3)]
        for i in range(2):
            homePage.slipPostContainer()
        updateAfterOneTitle=[homePage.getPostDescription(index=i) for i in range(3)]
        assert updateBeforeOneTitle!=updateAfterOneTitle  #通过前后前三个帖子标题是否相同，判断帖子是否更新

    @allure.story("测试点击喜欢，喜欢数+1")
    def test_clickLike(self,homePage):
        likeBefore=homePage.getLikeNum()
        homePage.clickLike()
        likeAfter=homePage.getLikeNum()
        if likeBefore<10000:   # 如果点赞数大于10000，不会显示个位数，无法判断
            assert likeAfter==likeBefore+1
    @allure.story("测试取消喜欢，喜欢数-1")
    def test_unLike(self,homePage):
        likeBefore=homePage.getLikeNum()
        homePage.clickLike()
        likeAfter=homePage.getLikeNum()
        if likeBefore<=10000:   # 如果点赞数大于10000，不会显示个位数，无法判断
            assert likeAfter==likeBefore-1
    @allure.story("主页搜索测试，判断是否存在搜索结果")
    @data_driven_test
    def test_search(self,test_init,homePage,searchResultPage,searchPage,data):
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