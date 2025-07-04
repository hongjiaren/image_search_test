import pytest
from src import image_utils

def test_utils_functions_exist():
    # 检查常用工具函数是否存在
    assert len(dir(image_utils)) > 0 