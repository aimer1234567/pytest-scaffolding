import inspect
from pathlib import Path
import os
import functools
import pytest
import csv
import pandas as pd
class DataMappingConfig:
        mapping_folder="data"
        default_file=".csv"

data_type = {'csv', 'xlsx'}
              
    
def data_mapping(func_name):
    # 获取调用栈上一层调用者的信息
    caller_frame = inspect.stack()[2]
    # 获取调用者文件的绝对路径
    caller_file = os.path.abspath(caller_frame.filename)
    cwd= os.getcwd()
    caller_path=caller_file[cwd.__len__()+1:]
    caller_path_list=caller_path.split('\\')
    caller_path_list[0]=DataMappingConfig.mapping_folder
    caller_path_list[-1]=caller_path_list[-1].replace('.py', f'\\{func_name}.*')
    mapping_path="\\".join(caller_path_list)
    mapping_path=cwd+'\\'+mapping_path
    # 构造父目录的Path
    parent_dir = Path(mapping_path).parent
    # glob匹配文件
    pattern = Path(mapping_path).name
    matches = list(parent_dir.glob(pattern))
    if matches.__len__() == 0:
        raise FileNotFoundError(f"未找到文件: {mapping_path}")
    elif matches.__len__() > 1:
        raise OSError(f"找到多个匹配的文件: {mapping_path}")
    type=matches[0].name.split('.')[-1]
    if type not in data_type:
        filename = matches[0].name
        raise OSError(f"不支持读取该文件类型: {filename}")
    if type == 'csv':
        return parse_csv(matches[0].resolve())
    return parse_csv(matches[0].resolve())


def parse_csv(file_path:str):
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        rows = list(reader)
    if not rows:
        raise ValueError("CSV 文件为空")
    header = rows[0]
    data = rows[1:]  
    return header, data

def parse_excel(file_path: str):
    try:
        df = pd.read_excel(file_path)
    except Exception as e:
        raise ValueError(f"读取Excel文件失败: {str(e)}")
    if df.empty:
        raise ValueError("Excel 文件为空")
    header = df.columns.tolist()
    data = df.values.tolist()
    return header, data

def data_driven_test(func):
    header, data = data_mapping(func.__name__)
    @functools.wraps(func)
    @pytest.mark.parametrize(header, data)
    def wrapper(*arg,**kwargs):     
        return func(*arg, **kwargs)
    return wrapper