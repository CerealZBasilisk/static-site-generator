import unittest

from node_converter import text_node_to_html_node
from textnode import TextNode, TextType
from leafnode import LeafNode
from constants import *

class TestTextNodeToHTML(unittest.TestCase):

    def test_plain_text(self):
        #Test plain raw text conversion
        node = TextNode("Hello, world!", TextType.TEXT)
        html = text_node_to_html_node(node)
        self.assertIsInstance(html, LeafNode)
        self.assertIsNone(html.tag)
        self.assertEqual(html.value, "Hello, world!")
        self.assertIsNone(html.props)

    def test_bold(self):
        #Test bold text conversion
        node = TextNode("Bold text", TextType.BOLD)
        html = text_node_to_html_node(node)
        self.assertIsInstance(html, LeafNode)
        self.assertEqual(html.tag, "b")
        self.assertEqual(html.value, "Bold text")
        self.assertIsNone(html.props)

    def test_italic(self):
        #Test italic text conversion
        node = TextNode("Italic text", TextType.ITALIC)
        html = text_node_to_html_node(node)
        self.assertIsInstance(html, LeafNode)
        self.assertEqual(html.tag, "i")
        self.assertEqual(html.value, "Italic text")
        self.assertIsNone(html.props)

    def test_code(self):
        #Test code text conversion
        node = TextNode("print('Hello')", TextType.CODE)
        html = text_node_to_html_node(node)
        self.assertIsInstance(html, LeafNode)
        self.assertEqual(html.tag, "code")
        self.assertEqual(html.value, "print('Hello')")
        self.assertIsNone(html.props)

    def test_link(self):
        #Test link conversion
        node = TextNode("Click me", TextType.LINK, url="https://www.test_url.com")
        html = text_node_to_html_node(node)
        self.assertIsInstance(html, LeafNode)
        self.assertEqual(html.tag, "a")
        self.assertEqual(html.value, "Click me")
        self.assertEqual(html.props, {"href": "https://www.test_url.com"})

    def test_image(self):
        #Test image conversion
        node = TextNode("alt text", TextType.IMAGE, url="https://i.imgur.com/pic.jpg")
        html = text_node_to_html_node(node)
        self.assertIsInstance(html, LeafNode)
        self.assertEqual(html.tag, "img")
        self.assertEqual(html.value, "")  # empty string for images
        self.assertEqual(html.props, {"src": "https://i.imgur.com/pic.jpg", "alt": "alt text"})

    def test_raw_text_with_url(self):
        #Test raw text should not have a URL
        with self.assertRaises(ValueError) as context:
            node = TextNode("Raw text", TextType.TEXT, url="https://example.com")
            text_node_to_html_node(node)
        

    def test_bold_text_with_url(self):
        #Test bold text should not have a URL
        with self.assertRaises(ValueError) as context:
            node = TextNode("Bold text", TextType.BOLD, url="https://example.com")
            text_node_to_html_node(node)

    def test_italic_text_with_url(self):
        #Test italic text should not have a URL
        with self.assertRaises(ValueError) as context:
            node = TextNode("Italic text", TextType.ITALIC, url="https://example.com")
            text_node_to_html_node(node)

    def test_code_text_with_url(self):
        #Test code text should not have a URL
        with self.assertRaises(ValueError) as context:
            node = TextNode("print('Hello')", TextType.CODE, url="https://example.com")
            text_node_to_html_node(node)

    def test_link_without_url(self):
        #Test link conversion should fail if URL is missing
        with self.assertRaises(ValueError):
            text_node_to_html_node(TextNode("Click me", TextType.LINK))
        
    def test_image_without_url(self):
        #Test image conversion should fail if URL is missing
        with self.assertRaises(ValueError):
            text_node_to_html_node(TextNode("alt text", TextType.IMAGE))
        
    def test_invalid_text_type(self):
        #Test an invalid text type
        class FakeTextType:
            value = "unsupported"
        with self.assertRaises(ValueError):
            text_node_to_html_node(TextNode("Invalid", FakeTextType()))
        


if __name__ == "__main__":
    unittest.main()
