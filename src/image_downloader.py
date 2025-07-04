from typing import Optional
import requests
import os


def download_image(url: str, save_path: str) -> bool:
    """
    下载图片到指定路径，保持原格式。
    :param url: 图片URL
    :param save_path: 保存路径（含文件名）
    :return: 下载是否成功
    """
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        with open(save_path, 'wb') as f:
            f.write(response.content)
        return True
    except Exception as e:
        print(f"[WARN] 下载失败: {url}，原因: {e}")
        return False 