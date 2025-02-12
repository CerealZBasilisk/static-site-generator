from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        if value == None:
            raise ValueError("Value cannot be None for a LeafNode")
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.tag == None:
            return f"{self.value}"
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"



if __name__ == "__main__":
    node_props = {
            "href": "https://www.google.com", 
            "target": "_blank",
            }
    test_node = LeafNode("a", "This is a link node", node_props)
    expected_props = ' href="https://www.google.com" target="_blank"'
    print(f"props to html test: {test_node.props_to_html()}")
    print(f"expected html: {expected_props}")

    # Let's print these values
    print(f"Props dictionary: {test_node.props}")
    print(f"Full HTML output: {test_node.to_html()}")
    print(f"Props HTML part: {test_node.props_to_html()}")
