import unittest
from textnode import TextNode, TextType
from split_nodes import split_nodes_link, split_nodes_images

class TestSplitNodes(unittest.TestCase):
    def test_split_nodes_link_basic(self):
        node = TextNode("Click [here](url) to continue", TextType.TEXT)
        nodes = split_nodes_link([node])
        self.assertEqual(len(nodes), 3)
        self.assertEqual(nodes[0].text, "Click ")
        self.assertEqual(nodes[1].text, "here")
        self.assertEqual(nodes[1].url, "url")
        self.assertEqual(nodes[1].text_type, TextType.LINK)
        self.assertEqual(nodes[2].text, " to continue")

    def test_split_nodes_link_multiple(self):
        node = TextNode(
            "This is text with [link1](url1) and [link2](url2) and more text",
            TextType.TEXT
        )
        nodes = split_nodes_link([node])
        self.assertEqual(len(nodes), 5)
        self.assertEqual(nodes[0].text, "This is text with ")
        self.assertEqual(nodes[1].text, "link1")
        self.assertEqual(nodes[1].url, "url1")
        self.assertEqual(nodes[2].text, " and ")
        self.assertEqual(nodes[3].text, "link2")
        self.assertEqual(nodes[3].url, "url2")
        self.assertEqual(nodes[4].text, " and more text")


    def test_split_one_link(self):
        node = TextNode("Click [here](url1) please", TextType.TEXT)
        nodes = split_nodes_link([node])
        self.assertEqual(len(nodes), 3)
        self.assertEqual(nodes[0].text, "Click ")
        self.assertEqual(nodes[1].text, "here")
        self.assertEqual(nodes[1].url, "url1")
        self.assertEqual(nodes[2].text, " please")
    
    def test_split_one_image(self):
        node = TextNode("See ![image](pic.jpg) above", TextType.TEXT)
        nodes = split_nodes_images([node])
        self.assertEqual(len(nodes), 3)
        self.assertEqual(nodes[0].text, "See ")
        self.assertEqual(nodes[1].text, "image")
        self.assertEqual(nodes[1].url, "pic.jpg")
        self.assertEqual(nodes[1].text_type, TextType.IMAGE)
        self.assertEqual(nodes[2].text, " above")

    def test_split_no_images(self):
        node = TextNode("Just plain text", TextType.TEXT)
        nodes = split_nodes_images([node])
        self.assertEqual(len(nodes), 1)
        self.assertEqual(nodes[0].text, "Just plain text")
        self.assertEqual(nodes[0].text_type, TextType.TEXT)
    
    def test_split_multiple_images(self):
        node = TextNode("Start ![first](img1.jpg) middle ![second](img2.jpg) end", TextType.TEXT)
        nodes = split_nodes_images([node])
        self.assertEqual(len(nodes), 5)
        self.assertEqual(nodes[0].text, "Start ")
        self.assertEqual(nodes[1].text, "first")
        self.assertEqual(nodes[1].url, "img1.jpg")
        self.assertEqual(nodes[1].text_type, TextType.IMAGE)
        self.assertEqual(nodes[2].text, " middle ")
        self.assertEqual(nodes[3].text, "second")
        self.assertEqual(nodes[3].url, "img2.jpg")
        self.assertEqual(nodes[3].text_type, TextType.IMAGE)
        self.assertEqual(nodes[4].text, " end")

if __name__ == "__main__":
    unittest.main()