from config import test_init, postPage,homePage
from utils.data_mapping import data_driven_test

@data_driven_test
def test_nullValueNotSend(test_init,postPage,homePage,text):
    """测试发送评论，空值，空格，换行符不能发送
    """
    try:
        d = test_init
        homePage.clickTextPostRandom()
        if not postPage.isAdButton():
            postPage.clickReview().inputReview(text)
            assert postPage.isEnableClickSend()==False #判断发送按钮是否能点击
    except Exception as e:
        raise e
    finally:
        d.press("back")
        d.press("back")
        homePage.slipPostContainer()
@data_driven_test
def test_sendReview(test_init,postPage,homePage,text):
    """测试发送评论,评论发送成功评论条数＋1
    """
    try:
        d = test_init
        homePage.clickTextPostRandom()
        if not postPage.isAdButton():
            sendReviewBefore=postPage.getReviewNum()
            postPage.clickReview().inputReview(text)
            postPage.clickSendReview()
            sendReviewAfter=postPage.getReviewNum()
            assert sendReviewAfter-sendReviewBefore==1  #评论发送成功评论数＋1
    except Exception as e:
        raise e
    finally:
        d.press("back")
        homePage.slipPostContainer()
    