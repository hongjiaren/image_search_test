import os
import requests
from typing import List, Dict, Optional


TAVILY_API_KEY: Optional[str] = os.getenv("TAVILY_API_KEY")
TAVILY_API_URL: str = "https://api.tavily.com/search"

class TavilyImageSearch:
    """
    Tavily 搜图API封装类。
    """
    def __init__(self, api_key: Optional[str] = None) -> None:
        """
        初始化TavilyImageSearch。
        :param api_key: Tavily API Key，可选，默认从环境变量读取
        """
        self.api_key: str = api_key or TAVILY_API_KEY
        if not self.api_key:
            raise ValueError("Tavily API key is required.")

    def search_images(self, query: str, max_results: int) -> List[Dict]:
        """
        搜索图片，返回图片信息列表。
        :param query: 搜索关键词
        :param max_results: 返回图片数量
        :return: 图片信息列表，每项包含url和description
        """
        payload: Dict = {
            "api_key": self.api_key,
            "query": query,
            "max_results": max_results,
            "include_images": True,
            "include_image_descriptions": True,
        }
        response = requests.post(TAVILY_API_URL, json=payload)
        response.raise_for_status()
        data = response.json()
        images = data.get("images", [])
        actual_count = len(images)
        print(f"Tavily API 实际返回图片数量: {actual_count}")
        if actual_count < max_results:
            print(f"提示：Tavily API 返回的图片数量少于你请求的 {max_results} 张，实际最多只返回了 {actual_count} 张。")
        # 兼容API返回格式
        if isinstance(images, list) and images and isinstance(images[0], dict):
            return images
        # 旧格式：images为url字符串列表
        elif isinstance(images, list):
            return [{"url": url, "description": ""} for url in images]
        return []

if __name__ == "__main__":
    searcher = TavilyImageSearch()
    results = searcher.search_images("中国美食", max_results=3)
    for img in results:
        print(f"图片链接: {img.get('url')}")
        print(f"描述: {img.get('description')}")
        print("-") 