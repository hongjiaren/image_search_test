import pytest
from src import image_crawler

def test_main_flow():
    # 假设 image_crawler 有 main 或 crawl_images 等主流程函数
    assert hasattr(image_crawler, 'main') or hasattr(image_crawler, 'crawl_images') 