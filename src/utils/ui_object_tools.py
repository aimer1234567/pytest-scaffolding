import uiautomator2 as u2
def slip(d,el,direction=0,duration=0.3,count=1):
    bounds=el.bounds()
    top=bounds[1]
    bottom=bounds[3]
    length=bottom-top
    for i in range(count):
       start_x = (bounds[0] + bounds[2]) // 2
       start_y = bottom - int(length * 0.2)
       end_x=start_x
       end_y = top + int(length * 0.2)
       if direction == 1:
            d.swipe(start_x, start_y, end_x, end_y, duration)
       else:
            d.swipe(end_x, end_y,start_x, start_y,duration)

def isCurrentActivity(d, target_activity: str) -> bool:
    try:
        current = d.app_current()
        current_activity = current.get('activity', '')
        if target_activity in current_activity:
            return True
        else:
            return False
    except Exception as e:
        print(f"获取当前 Activity 失败: {e}")
        return False
    
def clickSafe(el,timeout=5):
    el.wait(timeout=timeout)
    if el.exists:
        el.click()
    else:
        raise Exception("元素不存在")