from split_nodes import split_nodes_images, split_nodes_link
from textnode import TextNode, TextType
from split_node_delimiter import split_nodes_delimiter
import re
from constants import *




def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_delimiter(nodes, "*", TextType.ITALIC)
    nodes = split_nodes_link(nodes)
    nodes = split_nodes_images(nodes)
    return nodes


if __name__ == "__main__":
    text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
    text = "Text with **multiple** *formats* and `code`"
    result = text_to_textnodes(text)
    for node in result:
        print(node)
    