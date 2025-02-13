import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node link", 
                         TextType.LINK, 
                         "https://www.test_url.com")
        self.assertNotEqual(node, node2)

    def test_link_eq(self):
        node = TextNode("This is a text node link", 
                        TextType.LINK, 
                        "https://www.test_url.com")
        node2 = TextNode("This is a text node link", 
                         TextType.LINK, 
                         "https://www.test_url.com")
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a test", TextType.BOLD, url="http://example.com")
        
        expected_repr = "TextNode(This is a test, bold, http://example.com)"
        self.assertEqual(repr(node), expected_repr)
        


if __name__ == "__main__":
    unittest.main()
