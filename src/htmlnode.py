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
        if not isinstance(self.props, dict) or len(self.props) == 0:
            return ""
        props_list = [f'{key}="{self.props[key]}"' for key in sorted(self.props.keys())]
        return " " + " ".join(props_list)

    def prop_to_string(self, prop):
        return f' {prop[0]}="{prop[1]}"'

    def __repr__(self):
        return f"{self.__class__.__name__}({self.tag}, {self.value}, {self.children}, {self.props})"
    
