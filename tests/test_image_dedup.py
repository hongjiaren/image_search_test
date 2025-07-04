import pytest
from src import image_dedup

def test_dedup_function_exists():
    # 假设 image_dedup 有 deduplicate_images 或类似函数
    assert hasattr(image_dedup, 'deduplicate_images') 