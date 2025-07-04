import argparse
from src.image_crawler import crawl_images

def main() -> None:
    parser = argparse.ArgumentParser(description="高质量图片采集工具")
    parser.add_argument("--query", type=str, required=True, help="图片搜索关键词")
    parser.add_argument("--output_dir", type=str, required=True, help="图片保存目录")
    parser.add_argument("--max_count", type=int, default=20, help="最多采集图片数量")
    args = parser.parse_args()

    crawl_images(query=args.query, output_dir=args.output_dir, max_count=args.max_count)

if __name__ == "__main__":
    main()
