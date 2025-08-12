import utils.data_mapping as data_mapping
import pytest
import uiautomator2 as u2
import time
data_mapping.DataMappingConfig.mapping_folder = "data"
data_mapping.DataMappingConfig.default_file = ".txt"
 
@pytest.fixture(scope="session")
def test_init():
    d = u2.connect('5DNNXCAAFQPN9LOR')
       # 启动一个应用，比如微信
    d.app_start("com.xingin.xhs")
    time.sleep(2)  # 等待应用启动
    yield d
    d.app_stop("com.xingin.xhs")  