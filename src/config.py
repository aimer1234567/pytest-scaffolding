import utils.data_mapping as data_mapping
import pytest
import uiautomator2 as u2
import time
from pages.homePage import HomePage
from pages.searchPage import SearchPage
from pages.searchResultPage import SearchResultPage
from pages.postPage import PostPage

data_mapping.DataMappingConfig.mapping_folder = "data"

@pytest.fixture(scope="session")
def test_init():
    d = u2.connect('5DNNXCAAFQPN9LOR')
       # 启动一个应用，比如微信
    d.app_start("com.xingin.xhs")
    time.sleep(5)  # 等待应用启动
    yield d
    d.app_stop("com.xingin.xhs")  

@pytest.fixture(scope="session")
def postPage(test_init):
   return PostPage(test_init)

@pytest.fixture(scope="session")
def homePage(test_init):
   return HomePage(test_init)
   
@pytest.fixture(scope="session")
def searchPage(test_init):
   return SearchPage(test_init)

@pytest.fixture(scope="session")
def searchResultPage(test_init):
   return SearchResultPage(test_init)
   