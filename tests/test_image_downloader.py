import pytest
from src import image_downloader

def test_download_function_exists():
    # 假设 image_downloader 有 download_image 或 download_images
    assert hasattr(image_downloader, 'download_image') or hasattr(image_downloader, 'download_images') 