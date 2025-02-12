import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_repr(self):
        node_props = {
            "href": "https://www.google.com", 
            "target": "_blank",
            }
        node = LeafNode("a", "This is a link node", node_props)
        expected_repr = f'LeafNode(a, This is a link node, None, {node_props})'
        self.assertEqual(repr(node), expected_repr)

    def test_props_to_html(self):
        node_props = {
            "href": "https://www.google.com", 
            "target": "_blank",
            }
        node = LeafNode("a", "This is a link node", node_props)
        expected_props = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), expected_props)

    def test_props_to_html_no_props(self):
        node = LeafNode("p", "This is a text node", None)
        expected_props = ""
        self.assertEqual(node.props_to_html(), expected_props)

    def test_node_no_tag(self):
        # This should represent raw text
        text_node = LeafNode(None, "Just text", None)
        expected_repr = f'LeafNode(None, Just text, None, None)'
        self.assertEqual(repr(text_node), expected_repr)

    def test_partial_node(self):
        with self.assertRaises(ValueError):
            # Test with only some parameters provided
            node = LeafNode(tag="p")  # All other parameters should be None
            

    def test_to_html_paragraph(self):
        node = LeafNode("p", "This is a paragraph of text.")
        expected_html = "<p>This is a paragraph of text.</p>"
        self.assertEqual(node.to_html(), expected_html)

    def test_to_html_link(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        expected_html = '<a href="https://www.google.com">Click me!</a>'
        self.assertEqual(node.to_html(), expected_html)

    def test_empty_props_dict(self):
        node = LeafNode("p", "Some text", {})
        expected_html = "<p>Some text</p>"
        self.assertEqual(node.to_html(), expected_html)

    def test_special_characters(self):
        # Test that special characters in the value are preserved
        node = LeafNode("p", "Text with <b>tags</b> & symbols")
        expected_html = "<p>Text with <b>tags</b> & symbols</p>"
        self.assertEqual(node.to_html(), expected_html)

    def test_props_order_consistency(self):
        # Create two nodes with same props in different orders
        props1 = {
            "class": "btn",
            "id": "submit",
            "type": "button"
        }
        props2 = {
            "type": "button",
            "id": "submit",
            "class": "btn"
        }
        
        node1 = LeafNode("button", "Click Me", props1)
        node2 = LeafNode("button", "Click Me", props2)
        
        # Both should produce identical HTML
        html1 = node1.to_html()
        html2 = node2.to_html()
        
        self.assertEqual(html1, html2)


if __name__ == "__main__":
    unittest.main()