import unittest

from text_to_textnodes import text_to_textnodes
from textnode import TextNode, TextType


class TestTextToTextnodes(unittest.TestCase):

    def test_code_blocks(self):
        # Test basic code block
        text = "This is text with a `code block` word"
        nodes = text_to_textnodes(text)
        self.assertEqual(len(nodes), 3)
        self.assertEqual(nodes[0].text, "This is text with a ")
        self.assertEqual(nodes[1].text, "code block")
        self.assertEqual(nodes[1].text_type, TextType.CODE)
        self.assertEqual(nodes[2].text, " word")
        
        # Test multiple code blocks
        text = "Text with `code` and `another code` block"
        nodes = text_to_textnodes(text)
        self.assertEqual(len(nodes), 5)

    def test_bold_text(self):
        text = "This is **bold** text"
        nodes = text_to_textnodes(text)
        self.assertEqual(len(nodes), 3)
        self.assertEqual(nodes[0].text_type, TextType.TEXT)
        self.assertEqual(nodes[1].text_type, TextType.BOLD)
        self.assertEqual(nodes[2].text_type, TextType.TEXT)

    def test_italic_text(self):
        text = "This is *italic* text"
        nodes = text_to_textnodes(text)
        self.assertEqual(len(nodes), 3)
        self.assertEqual(nodes[0].text_type, TextType.TEXT)
        self.assertEqual(nodes[1].text_type, TextType.ITALIC)
        self.assertEqual(nodes[2].text_type, TextType.TEXT)
    
    def test_invalid_markdown(self):
        test_cases = [
            "Invalid `code",
            "Invalid **bold",
            "Invalid *italic",
            #"[link without closing](https://boot.dev", 
        ]
        for text in test_cases:
            node = TextNode(text, TextType.TEXT)
            with self.assertRaises(ValueError):
                text_to_textnodes(text)

    def test_mixed_format(self):
        test_cases = [
            (
                "This is **bold** and *italic* text",
                5, 
                [TextType.TEXT,TextType.BOLD, TextType.TEXT, TextType.ITALIC, TextType.TEXT]
            ),
            (
                "This is a `code` with a [link](https://boot.dev)",
                4,
                [TextType.TEXT,TextType.CODE, TextType.TEXT, TextType.LINK]
            ),
            (
                "This **bold** has an ![image](https://example.com/img.png)",
                4,
                [TextType.TEXT,TextType.BOLD, TextType.TEXT, TextType.IMAGE]
            )
        ]
        for text, length, tests in test_cases:
                nodes = text_to_textnodes(text)
                self.assertEqual(len(nodes), length)
                self.assertEqual(len(nodes), len(tests))
                for node, expected in zip(nodes, tests):
                    self.assertEqual(node.text_type, expected)

    def test_edge_cases(self):
        test_cases = [
            (
                "",  # empty string
                0, 
                []
            ),
            (
                "Text with **multiple** *formats* and `code`",
                6,
                [TextType.TEXT, TextType.BOLD, TextType.TEXT, TextType.ITALIC, TextType.TEXT, TextType.CODE]
            )
        ]
        for text, length, tests in test_cases:
                nodes = text_to_textnodes(text)
                self.assertEqual(len(nodes), length)
                self.assertEqual(len(nodes), len(tests))
                for node, expected in zip(nodes, tests):
                    self.assertEqual(node.text_type, expected)


    def test_mixed_format_all(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        tests = [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]
        result = text_to_textnodes(text)
        for node ,test in zip(result,tests):
            self.assertEqual(node, test)


if __name__ == "__main__":
    unittest.main()
