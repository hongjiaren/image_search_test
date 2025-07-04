from typing import List
import requests

def search_images(query: str, max_count: int = 20) -> List[str]:
    """
    根据关键词搜索图片，返回图片URL列表。
    这里只做示例，实际可接入Bing/Tavily/Google等API。
    :param query: 搜索关键词
    :param max_count: 返回图片数量
    :return: 图片URL列表
    """
    # TODO: 替换为真实API调用
    # 示例：用duckduckgo图片搜索API（非官方）
    url = f"https://duckduckgo.com/?q={query}&iax=images&ia=images"
    # 实际应调用API并解析图片URL
    # 这里只返回空列表作为占位
    return [] 