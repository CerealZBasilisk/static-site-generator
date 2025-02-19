from textnode import TextNode, TextType

"""

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
        #print(f"Processing node: {node.text} of type {node.text_type}")
        if node.text_type != TextType.TEXT:
            #print(f"Skipping node because it's type {node.text_type}")
            new_nodes.append(node)
            continue
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
    # Special case for single asterisk
    if delimiter == "*":
        # Don't count double asterisks
        count = text.count("**")
        # Subtract double asterisks from total asterisks to get single asterisks
        single_asterisks = text.count("*") - (2 * count)
        return single_asterisks > 0 and single_asterisks % 2 == 0
    
        # For all other delimiters
    count = text.count(delimiter)
    return count > 0 and count % 2 == 0

"""
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes


if __name__ == "__main__":
    node = TextNode("This is text with a `code block` word", TextType.TEXT)
    new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
    # new_nodes = split_nodes_delimiter(node, "`", TextType.CODE)
    