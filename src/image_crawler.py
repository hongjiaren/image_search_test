from typing import Optional, Set
import os
from .image_search import search_images
from .image_downloader import download_image
from .image_dedup import is_duplicate
from .image_utils import get_image_ext_from_url, get_renamed_filename

def crawl_images(query: str, output_dir: str, max_count: int = 20) -> None:
    """
    根据关键词采集高质量图片，去重并重命名后保存到指定目录。
    :param query: 图片搜索关键词
    :param output_dir: 图片保存目录
    :param max_count: 最多采集图片数量
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    print(f"[INFO] 采集关键词: {query}")
    print(f"[INFO] 图片保存目录: {output_dir}")
    print(f"[INFO] 最大图片数量: {max_count}")

    image_urls = search_images(query, max_count * 2)  # 多抓一些，便于去重
    print(f"[INFO] 搜索到图片URL数量: {len(image_urls)}")
    hash_set: Set[str] = set()
    saved_count = 0
    for idx, url in enumerate(image_urls):
        ext = get_image_ext_from_url(url)
        filename = get_renamed_filename(query, saved_count + 1, ext)
        save_path = os.path.join(output_dir, filename)
        if download_image(url, save_path):
            if is_duplicate(save_path, hash_set):
                os.remove(save_path)
                continue
            saved_count += 1
            print(f"[OK] 已保存: {filename}")
            if saved_count >= max_count:
                break
    print(f"[DONE] 实际保存图片数量: {saved_count}") 