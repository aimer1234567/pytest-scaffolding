def slip(d,el,direction=1,duration=0.3,count=1):
    bounds=el.bounds
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

def click(d,el):
    bounds=el.bounds
    top=bounds[1]
    bottom=bounds[3]
    left=bounds[0]
    right=bounds[2]
    center_x = (left + right) // 2
    center_y = (top + bottom) // 2
    d.click(center_x, center_y)

def xmlElementToUiObject(d, xml_element):
    attrib = xml_element.attrib
    resource_id = attrib.get('resource-id', None)
    text = attrib.get('text', None)
    description = attrib.get('content-desc', None)
    loc_params = {}
    if resource_id and resource_id.strip():
        loc_params['resourceId'] = resource_id.strip()
    if text and text.strip():
        loc_params['text'] = text.strip()
    if description and description.strip():
        loc_params['description'] = description.strip()
    if not loc_params:
        raise ValueError("无法根据 xml_element 的属性构造定位参数")
    return d(**loc_params)

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