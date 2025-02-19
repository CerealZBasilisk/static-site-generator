from extract_markdown import extract_markdown_images, extract_markdown_links
from textnode import TextNode, TextType
import re
from constants import *


def split_nodes_link(old_nodes: list) -> list:
    result_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            result_nodes.append(node)
            continue
        original_text = node.text
        links = extract_markdown_links(original_text)
        if len(links) == 0:
            result_nodes.append(node)
            continue
        for link in links:
            sections = original_text.split(f"[{link[0]}]({link[1]})", 1)
            if len(sections) != 2:
                raise ValueError("invalid markdown, link section not closed")
            if sections[0] != "":
                result_nodes.append(TextNode(sections[0], TextType.TEXT))
            result_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
            original_text = sections[1]
        if original_text != "":
            result_nodes.append(TextNode(original_text, TextType.TEXT))
    return result_nodes


def split_nodes_images(old_nodes: list) -> list:
    result_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            result_nodes.append(node)
            continue
        original_text = node.text
        images = extract_markdown_images(original_text)
        if len(images) == 0:
            result_nodes.append(node)
            continue
        for alt_text, image in images:
            sections = original_text.split(f"![{alt_text}]({image})", 1)
            if len(sections) != 2:
                raise ValueError("invalid markdown, image section not closed")
            if sections[0] != "":
                result_nodes.append(TextNode(sections[0], TextType.TEXT))
            result_nodes.append(
                TextNode(
                    alt_text,
                    TextType.IMAGE,
                    image,
                )
            )
            original_text = sections[1]
        if original_text != "":
            result_nodes.append(TextNode(original_text, TextType.TEXT))
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
    

