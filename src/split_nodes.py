from extract_markdown import extract_markdown_images, extract_markdown_links
from textnode import TextNode, TextType
import re
from constants import *


def split_nodes_link(old_nodes: list) -> list:
    result_nodes = []
    for node in old_nodes:
        links = extract_markdown_links(node.text)
        if not links:
            result_nodes.append(node)
        else:
            current_text = node.text
            # Process each link in order
            for link_text, link_url in links:
                pattern = f"[{link_text}]({link_url})"
                # Split into before_link and remaining_text
                before_link, current_text = current_text.split(pattern, 1)
                
                # Add text node for content before link (if any)
                if before_link:
                    result_nodes.append(TextNode(before_link, TextType.TEXT))
                
                # Add the link node
                result_nodes.append(TextNode(link_text, TextType.LINK, link_url))
            
            # Don't forget any remaining text after last link
            if current_text:
                result_nodes.append(TextNode(current_text, TextType.TEXT))

    return result_nodes

def split_nodes_images(old_nodes: list) -> list:
    result_nodes = []
    for node in old_nodes:
        links = extract_markdown_images(node.text)
        if not links:
            result_nodes.append(node)
        else:
            current_text = node.text
            # Process each link in order
            for link_text, link_url in links:
                pattern = f"![{link_text}]({link_url})"
                # Split into before_link and remaining_text
                before_link, current_text = current_text.split(pattern, 1)
                
                # Add text node for content before link (if any)
                if before_link:
                    result_nodes.append(TextNode(before_link, TextType.TEXT))
                
                # Add the link node
                result_nodes.append(TextNode(link_text, TextType.IMAGE, link_url))
            
            # Don't forget any remaining text after last link
            if current_text:
                result_nodes.append(TextNode(current_text, TextType.TEXT))

    return result_nodes





if __name__ == "__main__":
    node = TextNode(
    "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
    TextType.TEXT,
)
    new_nodes = split_nodes_link([node])
    for node in new_nodes:

        print(node)
# [
#     TextNode("This is text with a link ", TextType.TEXT),
#     TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
#     TextNode(" and ", TextType.TEXT),
#     TextNode(
#         "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
#     ),
# ]
    

