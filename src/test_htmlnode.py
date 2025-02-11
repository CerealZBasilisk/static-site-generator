import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_repr(self):
        node_props = {
            "href": "https://www.google.com", 
            "target": "_blank",
            }
        node = HTMLNode("<p>", "This is a text node", None, node_props)
        expected_repr = f'HTMLNode(<p>, This is a text node, None, {node_props})'
        self.assertEqual(repr(node), expected_repr)

    def test_props_to_html(self):
        node_props = {
            "href": "https://www.google.com", 
            "target": "_blank",
            }
        node = HTMLNode("<p>", "This is a text node", None, node_props)
        expected_props = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), expected_props)

    def test_props_to_html_no_props(self):
        node = HTMLNode("p", "This is a text node", None, None)
        expected_props = ""
        self.assertEqual(node.props_to_html(), expected_props)

    def test_node_with_children(self):
        child_node = HTMLNode("b", "child")
        parent_node = HTMLNode("p", None, [child_node], None)
        expected_repr = f'HTMLNode(p, None, [{repr(child_node)}], None)'
        self.assertEqual(repr(parent_node), expected_repr)

    def test_node_no_tag(self):
        # This should represent raw text
        text_node = HTMLNode(None, "Just text", None, None)
        expected_repr = f'HTMLNode(None, Just text, None, None)'
        self.assertEqual(repr(text_node), expected_repr)

    def test_partial_node(self):
        # Test with only some parameters provided
        node = HTMLNode(tag="p")  # All other parameters should be None
        expected_repr = 'HTMLNode(p, None, None, None)'
        self.assertEqual(repr(node), expected_repr)

    def test_to_html_raises(self):
        node = HTMLNode("p", "hello")
        with self.assertRaises(NotImplementedError):
            node.to_html()


if __name__ == "__main__":
    unittest.main()