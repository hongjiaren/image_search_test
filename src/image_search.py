from typing import List, Dict, Literal
import os
import requests

# 支持的图片源
ImageSource = Literal["tavily", "bing", "google", "duckduckgo"]

# Bing API配置（用户提供）
BING_API_KEY = "6dfaf2857bf14fafaab261401fe2c75a"
BING_IMAGE_SEARCH_URL = "https://api.bing.microsoft.com/v7.0/images/search"


def search_images(
    query: str,
    max_count: int = 20,
    source: ImageSource = "tavily"
) -> List[Dict]:
    """
    统一图片搜索接口，支持多源，返回图片url和描述。
    :param query: 搜索关键词
    :param max_count: 返回图片数量
    :param source: 图片源（tavily/bing/google/duckduckgo等）
    :return: [{"image_url": str, "image_description": str}]
    """
    if source == "tavily":
        return search_images_tavily(query, max_count)
    elif source == "bing":
        return search_images_bing(query, max_count)
    elif source == "google":
        return search_images_google(query, max_count)
    elif source == "duckduckgo":
        return search_images_duckduckgo(query, max_count)
    else:
        raise ValueError(f"不支持的图片源: {source}")


def search_images_tavily(query: str, max_count: int = 20) -> List[Dict]:
    api_key = os.getenv("TAVILY_API_KEY", "")
    url = "https://api.tavily.com/search"
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {api_key}"}
    payload = {
        "query": query,
        "search_depth": "advanced",
        "include_images": True,
        "include_image_descriptions": True,
        "max_results": max_count,
    }
    try:
        resp = requests.post(url, json=payload, headers=headers, timeout=15)
        resp.raise_for_status()
        data = resp.json()
        images = data.get("images", [])
        return [
            {"image_url": img["url"], "image_description": img.get("description", "")}
            for img in images if "url" in img
        ][:max_count]
    except Exception as e:
        print(f"[ERROR] Tavily API 调用失败: {e}")
        return []


def search_images_bing(query: str, max_count: int = 20) -> List[Dict]:
    """
    使用Bing官方API搜索图片，使用用户提供的KEY和URL。
    """
    url = BING_IMAGE_SEARCH_URL
    api_key = BING_API_KEY
    headers = {"Ocp-Apim-Subscription-Key": api_key}
    params = {"q": query, "count": max_count, "safeSearch": "Moderate"}
    try:
        resp = requests.get(url, headers=headers, params=params, timeout=15)
        resp.raise_for_status()
        data = resp.json()
        images = data.get("value", [])
        return [
            {"image_url": img["contentUrl"], "image_description": img.get("name", "")}
            for img in images if "contentUrl" in img
        ][:max_count]
    except Exception as e:
        print(f"[ERROR] Bing API 调用失败: {e}")
        return []


def search_images_google(query: str, max_count: int = 20) -> List[Dict]:
    """
    使用SerpAPI搜索Google图片，需设置SERPAPI_API_KEY。
    """
    api_key = os.getenv("SERPAPI_API_KEY", "")
    if not api_key:
        print("[WARN] 未设置 SERPAPI_API_KEY，无法调用Google图片搜索API。")
        return []
    url = "https://serpapi.com/search.json"
    params = {
        "q": query,
        "tbm": "isch",
        "api_key": api_key,
        "ijn": 0,
        "num": max_count
    }
    try:
        resp = requests.get(url, params=params, timeout=15)
        resp.raise_for_status()
        data = resp.json()
        images = data.get("images_results", [])
        return [
            {"image_url": img["original"], "image_description": img.get("title", "")}
            for img in images if "original" in img
        ][:max_count]
    except Exception as e:
        print(f"[ERROR] Google(SERPAPI) API 调用失败: {e}")
        return []


def search_images_duckduckgo(query: str, max_count: int = 20) -> List[Dict]:
    """
    DuckDuckGo图片搜索（占位，需接入真实API或爬虫）。
    """
    print("[WARN] DuckDuckGo图片搜索未实现，返回空列表。")
    return [] 