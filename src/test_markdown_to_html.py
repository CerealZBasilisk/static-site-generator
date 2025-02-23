import unittest
from markdown_to_html import markdown_to_html_node

class TestMarkdownToHTML(unittest.TestCase):
    def test_div_parent(self):
        markdown = "# Test"
        html_node = markdown_to_html_node(markdown)
        self.assertEqual(html_node.tag, "div")
    
    def test_heading_block(self):
        markdown = "## Test Heading"
        html_node = markdown_to_html_node(markdown)
        self.assertEqual(html_node.children[0].tag, "h2")
        self.assertEqual(html_node.children[0].value.strip(), "Test Heading")
    
    def test_nested_paragraph(self):
        markdown = "This is *italics* and **bold**"
        html_node = markdown_to_html_node(markdown)
        p_node = html_node.children[0]
        self.assertEqual(p_node.tag, "p")
        self.assertEqual(len(p_node.children), 4)  # Text, italics, text, bold
        self.assertEqual(p_node.children[1].tag, "i")
    
    def test_unordered_list(self):
        markdown = """* Item 1
* Item 2"""
        html_node = markdown_to_html_node(markdown)
        ul_node = html_node.children[0]
        self.assertEqual(ul_node.tag, "ul")
        self.assertEqual(len(ul_node.children), 2)
        self.assertEqual(ul_node.children[0].tag, "li")

    # Add more test methods as needed

if __name__ == '__main__':
    unittest.main()