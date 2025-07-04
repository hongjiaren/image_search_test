import unittest
from src.search_image import TavilyImageSearch

class TestTavilyImageSearch(unittest.TestCase):
    def setUp(self):
        self.searcher = TavilyImageSearch()

    def test_search_images(self):
        results = self.searcher.search_images("长城", max_results=2)
        self.assertIsInstance(results, list)
        self.assertGreater(len(results), 0)
        for img in results:
            self.assertIn("url", img)
            self.assertIn("description", img)
            print(f"图片链接: {img['url']}")
            print(f"描述: {img['description']}")

if __name__ == "__main__":
    unittest.main() 