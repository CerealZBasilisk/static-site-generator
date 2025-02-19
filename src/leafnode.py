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

    def __repr__(self):
        return f"{self.__class__.__name__}({self.tag}, {self.value}, {self.props})"

