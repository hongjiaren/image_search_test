import argparse
from dotenv import load_dotenv
import os

# 自动加载根目录下的 .env
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), ".env"))

from src.search_image import TavilyImageSearch
from src.download_images import download_images

def main() -> None:
    parser = argparse.ArgumentParser(description="Tavily 搜图工具")
    parser.add_argument("--query", type=str, required=True, help="图片搜索关键词")
    parser.add_argument("--save_dir", type=str, default="images", help="图片保存目录")
    parser.add_argument("--max_results", type=int, default=5, help="最多采集图片数量")
    args = parser.parse_args()

    searcher = TavilyImageSearch()
    images = searcher.search_images(args.query, max_results=args.max_results)
    print(f"准备下载图片数量: {len(images)}")
    images = images[:args.max_results]  # 强制只保留 max_results 个
    print(f"实际将下载图片数量: {len(images)}")
    if not images:
        print("未找到图片结果。")
        return
    download_images(images, args.save_dir)

if __name__ == "__main__":
    main() 