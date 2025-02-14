from textnode import TextNode, TextType


def split_nodes_delimiter(
    old_nodes: list,       # A list of nodes
    delimiter: str,        # A string delimiter
    text_type: TextType    # A TextType enum instance
    ) -> list:
    
    if not isinstance(old_nodes, list):
        if isinstance(old_nodes, (dict, tuple)): 
            old_nodes = list(old_nodes)
        elif isinstance(old_nodes, list):  
            old_nodes = old_nodes
        else:  
            old_nodes = [old_nodes]

    if not isinstance(delimiter, str):
        raise TypeError("delimiter must be a string")

    if not isinstance(text_type, TextType):
        raise TypeError("text_type must be an instance of TextType Enum")
    

    new_nodes = []
    for node in old_nodes:
        if has_valid_delimiter_pattern(node.text, delimiter):

            string_list = node.text.split(delimiter)
            
            for i, string in enumerate(string_list):
                if i %2 == 0:
                    # print(string)
                    new_node = TextNode(string, node.text_type)
                    new_nodes.append(new_node)
                if i % 2 != 0:
                    # print(string)
                    new_node = TextNode(string, text_type)
                    new_nodes.append(new_node)
        else:
            raise ValueError(f"Invalid markdown syntax: missing closing {delimiter}")
    return new_nodes

def has_valid_delimiter_pattern(text: str, delimiter: str) -> bool:
    count = text.count(delimiter)
    validation = count % 2 == 0
    return validation


if __name__ == "__main__":
    node = TextNode("This is text with a `code block` word", TextType.TEXT)
    new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
    # new_nodes = split_nodes_delimiter(node, "`", TextType.CODE)
    