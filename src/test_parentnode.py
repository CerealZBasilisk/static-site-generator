import unittest

from parentnode import ParentNode
from leafnode import LeafNode


# Default testing nodes

leaf_props = {
    "class": "btn",
    "id": "submit",
    "type": "button"
}
leaf_props1 = {
    "class": "btn",
    "id": "submit",
    "type": "button"
}
leaf_props2 = {
    "type": "button",
    "id": "submit",
    "class": "btn"
}
default_leaf = LeafNode(tag="span", value="Test Value", props=leaf_props)
leaf_with_props = LeafNode(tag="b", value="Bold Text")
nested_parent = ParentNode(tag="div", children=[
    LeafNode(tag="p", value="Paragraph Text"),
    LeafNode(tag="span", value="Inline Text")
])
leaf_with_props1 = LeafNode("button", "Click Me", leaf_props1)  
leaf_with_props2 = LeafNode("button", "Click Me", leaf_props2)  


class TestParentNode(unittest.TestCase):

    def test_repr(self):
        node_props = {
            "href": "https://www.google.com", 
            "target": "_blank",
            }
        node = ParentNode("a", [leaf_with_props, leaf_with_props1, leaf_with_props2], node_props)
        expected_repr = f'ParentNode(a, None, {[leaf_with_props, leaf_with_props1, leaf_with_props2]}, {node_props})'
        self.assertEqual(repr(node), expected_repr)

    def test_props_to_html(self):
        node_props = {
            "href": "https://www.google.com", 
            "target": "_blank",
            }
        node = ParentNode("a", [leaf_with_props, 
                                leaf_with_props1, 
                                leaf_with_props2], 
                                node_props)
        expected_props = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), expected_props)

    def test_props_to_html_no_props(self):
        node = ParentNode("p", [leaf_with_props, leaf_with_props1, leaf_with_props2], None)
        expected_props = ""
        self.assertEqual(node.props_to_html(), expected_props)

    def test_node_no_tag(self):
        # This should throw error no tag 
        with self.assertRaises(ValueError):
            text_node = ParentNode(None, [leaf_with_props, leaf_with_props1, leaf_with_props2], None)
        

    def test_partial_node(self):
        with self.assertRaises(ValueError):
            # Test with only some parameters provided
            node = ParentNode(tag="p")  # All other parameters should be None
            

    def test_to_html_paragraph(self):
        node = ParentNode("p", nested_parent)
        expected_html = "<p><div><p>Paragraph Text</p><span>Inline Text</span></div></p>"
        self.assertEqual(node.to_html(), expected_html)

    def test_to_html_link(self):
        node = ParentNode("a", leaf_with_props, {"href": "https://www.google.com"})
        expected_html = '<a href="https://www.google.com"><b>Bold Text</b></a>'
        self.assertEqual(node.to_html(), expected_html)

    def test_empty_props_dict(self):
        node = ParentNode("p", leaf_with_props, {})
        expected_html = "<p><b>Bold Text</b></p>"
        self.assertEqual(node.to_html(), expected_html)

    def test_special_characters(self):
        # Test that special characters in the value are preserved
        node = ParentNode("p", 
                          [leaf_with_props, 
                           LeafNode(tag="p", value="Paragraph Text"), 
                           LeafNode(tag="span", value="Inline Text")
                          ])
        expected_html = "<p><b>Bold Text</b><p>Paragraph Text</p><span>Inline Text</span></p>" # dont know yet will put correct when i do
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
        
        node1 = ParentNode("button", [leaf_with_props], props1)
        node2 = ParentNode("button", [leaf_with_props], props2)
        
        # Both should produce identical HTML
        html1 = node1.to_html()
        html2 = node2.to_html()
        
        self.assertEqual(html1, html2)

    def test_to_html_output(self):
        node = ParentNode(
            "p",
            [LeafNode("b", "Bold text"),
             LeafNode(None, "Normal text"),
             LeafNode("i", "italic text"), 
             LeafNode(None, "Normal text"),
             ],
             )

        expect_html = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        self.assertEqual(expect_html, node.to_html())

if __name__ == "__main__":
    unittest.main()