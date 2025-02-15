from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag=None, children=None, props=None):
        if tag is None or children is None:
            raise ValueError("`tag` and `children` cannot be None for a ParentNode")
        
        if not isinstance(children, list):
            children = [children]

        if not all(isinstance(child, HTMLNode) for child in children):
            raise TypeError("All children must be instances of HTMLNode.")
        
        if len(children) == 0:
            raise ValueError("ParentNode must have at least one child.")
        
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None or self.children is None:
            raise ValueError("Cannot convert ParentNode to HTML: tag or children cannot be None")
        children_html = [child.to_html() for child in self.children]
        children_output = "".join(children_html)
        
        props_html = self.props_to_html()
        return f"<{self.tag}{props_html}>{children_output}</{self.tag}>"

if __name__ == "__main__":
    pass