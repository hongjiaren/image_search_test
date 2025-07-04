import os
from typing import List, Dict
import requests
from PIL import Image
import imagehash
from io import BytesIO

def download_images(images: List[Dict], save_dir: str) -> None:
    """
    下载图片到指定目录，保持原格式，重命名并去重。
    :param images: 图片信息列表，每项包含url和description
    :param save_dir: 图片保存目录
    """
    os.makedirs(save_dir, exist_ok=True)
    hash_set = set()  # 用于去重
    img_count = 0
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
    }
    print(f"即将下载 {len(images)} 张图片，保存到目录: {save_dir}")
    for idx, img in enumerate(images):
        url: str = img.get("url", "")
        desc: str = img.get("description", "")
        if not url:
            print(f"[{idx+1}] 跳过无效图片项（无URL）")
            continue
        print(f"[{idx+1}] 正在下载: {url}")
        try:
            resp = requests.get(url, headers=headers, timeout=10)
            resp.raise_for_status()
            img_bytes = BytesIO(resp.content)
            pil_img = Image.open(img_bytes)
            img_hash = str(imagehash.phash(pil_img))
            if img_hash in hash_set:
                print(f"[{idx+1}] 跳过重复图片: {url}")
                continue
            hash_set.add(img_hash)
            ext = pil_img.format.lower() if pil_img.format else "jpg"
            filename = f"image_{img_count+1:03d}.{ext}"
            filepath = os.path.join(save_dir, filename)
            if pil_img.mode == "P":
                print(f"[{idx+1}] 图片为P模式，自动转换为RGBA以保留透明度。")
                pil_img = pil_img.convert("RGBA")
            pil_img.save(filepath)
            if desc:
                with open(filepath + ".txt", "w", encoding="utf-8") as f:
                    f.write(desc)
            print(f"[{idx+1}] 已保存: {filepath}（格式: {ext}）")
            img_count += 1
        except Exception as e:
            print(f"[{idx+1}] 下载失败: {url}，原因: {e}")
    print(f"下载完成，成功保存图片数量: {img_count}") 