import uiautomator2 as u2
d = u2.connect()

selector = d.xpath('//*[@content-desc="笔记 几乎废了的大号 如何拯救 来自小南和大橘喔 217赞"]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]')

if selector.exists:
    element = selector.get()    # 得到 UiObject
    print(element.info)         # 查看元素属性
    element.click()             # 点击元素
else:
    print("元素不存在")
