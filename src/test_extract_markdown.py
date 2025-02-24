import unittest
from extract_markdown import extract_markdown_images, extract_markdown_links, extract_title

class TestMarkdownExtractor(unittest.TestCase):
    def test_extract_single_image(self):
        text = "![alt text](https://example.com/image.png)"
        expected = [("alt text", "https://example.com/image.png")]
        self.assertEqual(extract_markdown_images(text), expected)
    
    def test_extract_multiple_images(self):
        text = "![img1](url1) ![img2](url2)"
        expected = [("img1", "url1"), ("img2", "url2")]
        self.assertEqual(extract_markdown_images(text), expected)
    
    def test_extract_image_empty_alt(self):
        text = "![](https://example.com/image.png)"
        expected = [("", "https://example.com/image.png")]
        self.assertEqual(extract_markdown_images(text), expected)
    
    def test_extract_no_images(self):
        text = "Just plain text"
        self.assertEqual(extract_markdown_images(text), [])
    
    def test_extract_image_with_special_chars(self):
        text = "![My Cool Image!](https://example.com/image.png)"
        expected = [("My Cool Image!", "https://example.com/image.png")]
        self.assertEqual(extract_markdown_images(text), expected)

    def test_extract_single_link(self):
        text = "[link text](https://example.com)"
        expected = [("link text", "https://example.com")]
        self.assertEqual(extract_markdown_links(text), expected)
    
    def test_extract_multiple_links(self):
        text = "[link1](url1) [link2](url2)"
        expected = [("link1", "url1"), ("link2", "url2")]
        self.assertEqual(extract_markdown_links(text), expected)

    def test_mixed_links_and_images(self):
        text = "Here's a ![cute cat](cat.jpg) and a [link](https://example.com) followed by ![dog](dog.png)"
        expected_images = [("cute cat", "cat.jpg"), ("dog", "dog.png")]
        expected_links = [("link", "https://example.com")]
        self.assertEqual(extract_markdown_images(text), expected_images)
        self.assertEqual(extract_markdown_links(text), expected_links)

    def test_urls_with_special_characters(self):
        text = """
        ![complex](https://example.com/path?param=1&other=2)
        [query params](https://api.com/endpoint?id=123&filter=test)
        """
        expected_images = [("complex", "https://example.com/path?param=1&other=2")]
        expected_links = [("query params", "https://api.com/endpoint?id=123&filter=test")]
        self.assertEqual(extract_markdown_images(text), expected_images)
        self.assertEqual(extract_markdown_links(text), expected_links)

    def test_escaped_brackets(self):
        text = """
        ![alt text with no brackets](image.jpg)
        [text with no brackets](link.com)
        """
        expected_images = [("alt text with no brackets", "image.jpg")]
        expected_links = [("text with no brackets", "link.com")]
        self.assertEqual(extract_markdown_images(text), expected_images)
        self.assertEqual(extract_markdown_links(text), expected_links)

    def test_complex_text(self):
        text = """
        ![alt text (with parens)](image.jpg)
        [link text {with braces}](link.com)
        """
        expected_images = [("alt text (with parens)", "image.jpg")]
        expected_links = [("link text {with braces}", "link.com")]
        self.assertEqual(extract_markdown_images(text), expected_images)
        self.assertEqual(extract_markdown_links(text), expected_links)

    def test_complex_text(self):
            text = """
            # heading text with another below 
            # heading text 
            """
            expected_headings = [("heading text with another below", "heading text")]
            self.assertEqual(extract_title(text), expected_headings)

    def test_complex_text(self):
            text = """
            heading text with another below 
            heading text 
            """
            with self.assertRaises(Exception):
                h1 = extract_title(text) 
            

if __name__ == "__main__":
    unittest.main()