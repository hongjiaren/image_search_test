from typing import Set
from PIL import Image
import imagehash


def is_duplicate(image_path: str, hash_set: Set[str], hash_size: int = 8) -> bool:
    """
    判断图片是否重复（基于感知哈希）。
    :param image_path: 图片路径
    :param hash_set: 已有图片hash集合
    :param hash_size: 哈希尺寸
    :return: 是否重复
    """
    try:
        with Image.open(image_path) as img:
            img_hash = str(imagehash.phash(img, hash_size=hash_size))
        if img_hash in hash_set:
            return True
        hash_set.add(img_hash)
        return False
    except Exception as e:
        print(f"[WARN] 图片去重失败: {image_path}，原因: {e}")
        return False 