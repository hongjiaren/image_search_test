import os
from typing import Tuple

def get_image_ext_from_url(url: str) -> str:
    """
    从URL获取图片扩展名，默认jpg。
    """
    ext = os.path.splitext(url)[-1].lower()
    if ext in [".jpg", ".jpeg", ".png", ".webp"]:
        return ext
    return ".jpg"

def get_renamed_filename(query: str, idx: int, ext: str) -> str:
    """
    生成规范化重命名文件名。
    """
    return f"{query}_{idx:03d}{ext}" 