import unittest

from split_node_delimiter import split_nodes_delimiter
from textnode import TextNode, TextType


class TestTextNodeDelimiter(unittest.TestCase):

    def test_code_blocks(self):
        # Test basic code block
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(len(nodes), 3)
        self.assertEqual(nodes[0].text, "This is text with a ")
        self.assertEqual(nodes[1].text, "code block")
        self.assertEqual(nodes[1].text_type, TextType.CODE)
        self.assertEqual(nodes[2].text, " word")
        
        # Test multiple code blocks
        node = TextNode("Text with `code` and `another code` block", TextType.TEXT)
        nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(len(nodes), 5)

    def test_bold_text(self):
        node = TextNode("This is **bold** text", TextType.TEXT)
        nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(len(nodes), 3)
        self.assertEqual(nodes[0].text_type, TextType.TEXT)
        self.assertEqual(nodes[1].text_type, TextType.BOLD)
        self.assertEqual(nodes[2].text_type, TextType.TEXT)

    def test_italic_text(self):
        node = TextNode("This is *italic* text", TextType.TEXT)
        nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)
        self.assertEqual(len(nodes), 3)
        self.assertEqual(nodes[0].text_type, TextType.TEXT)
        self.assertEqual(nodes[1].text_type, TextType.ITALIC)
        self.assertEqual(nodes[2].text_type, TextType.TEXT)
    
    def test_invalid_markdown(self):
        test_cases = [
            ("Invalid `code", "`", TextType.CODE),
            ("Invalid **bold", "**", TextType.BOLD),
            ("Invalid *italic", "*", TextType.ITALIC)
        ]
        for text, delimiter, text_type in test_cases:
            node = TextNode(text, TextType.TEXT)
            with self.assertRaises(ValueError):
                split_nodes_delimiter([node], delimiter, text_type)

if __name__ == "__main__":
    unittest.main()
