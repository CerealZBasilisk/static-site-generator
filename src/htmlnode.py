

class HTMLNode():
    def __init__(self, 
                 tag=None, 
                 value=None, 
                 children=None, 
                 props=None
                 ):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if not isinstance(self.props, dict):
            return ""
        props_list  = list(self.props.items())
        props_string_list = [self.prop_to_string(prop) for prop in props_list]
        return "".join(props_string_list)

    def prop_to_string(self, prop):
        return f' {prop[0]}="{prop[1]}"'

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    
