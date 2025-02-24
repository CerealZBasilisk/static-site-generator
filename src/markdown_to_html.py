from block_to_blocktype import block_to_block_type
from split_blocks import markdown_to_blocks
from text_to_textnodes import text_to_textnodes
from node_converter import text_node_to_html_node
from leafnode import LeafNode
from parentnode import ParentNode
from textnode import TextNode
from constants import *
import re


def markdown_to_html_node(markdown):
    body_nodes = []
    blocks = markdown_to_blocks(markdown)

    block_types = []
    for block in blocks:
        block_type = block_to_block_type(block)
        block_types.append(block_type)
    block_dict = dict(zip(blocks, block_types))
    
    for block , block_type in block_dict.items():

        # block_text = TextNode(block,text_type=TextType.TEXT)
        match block_type:
            case BlockType.HEADING:
                h_count = block.count("#")
                block = block.strip("#")
                head_html_node = LeafNode(BLOCK_TAG_STR[block_type]+f"{h_count}", block.strip())
                body_nodes.append(head_html_node)

            case BlockType.PARAGRAPH:
                text_nodes = text_to_textnodes(block)
                html_nodes = []
                for old_node in text_nodes:
                    new_node = text_node_to_html_node(old_node)
                    html_nodes.append(new_node)
                para_html_node = ParentNode(BLOCK_TAG_STR[block_type], html_nodes)
                body_nodes.append(para_html_node)

            case BlockType.CODE:
                code_html_node = LeafNode(BLOCK_TAG_STR[block_type], block.strip("```"))
                pre_html_node = ParentNode("pre",[code_html_node])
                body_nodes.append(pre_html_node)

            case BlockType.QUOTE:
                text_nodes = text_to_textnodes(block.lstrip(">").strip())
                html_nodes = []
                for old_node in text_nodes:
                    new_node = text_node_to_html_node(old_node)
                    html_nodes.append(new_node)
                quote_html_node = ParentNode(BLOCK_TAG_STR[block_type], html_nodes)
                body_nodes.append(quote_html_node)

            case BlockType.UNORDERED_LIST:
                li_list = []
                lines_list = block.split("\n")
                for line in lines_list:
                    filter_quote = re.match(r"^[*,\-,+]\s(.*)",line)
                    text = filter_quote.group(1)
                    text_nodes = text_to_textnodes(text)
                    html_nodes = [text_node_to_html_node(text_node) for text_node in text_nodes]
                    li_list.append(ParentNode("li",html_nodes))
                unorder_list_html_node = ParentNode(BLOCK_TAG_STR[block_type], li_list)
                body_nodes.append(unorder_list_html_node)


            case BlockType.ORDERED_LIST:
                li_list = []
                lines_list = block.split("\n")
                for line in lines_list:
                    cleaned = re.sub(r'^\d+\.\s+', '', line)
                    text_nodes = text_to_textnodes(cleaned)
                    html_nodes = [text_node_to_html_node(text_node) for text_node in text_nodes]
                    li_list.append(ParentNode("li",html_nodes))
                order_list_html_node = ParentNode(BLOCK_TAG_STR[block_type], li_list)
                body_nodes.append(order_list_html_node)


    BodyNode = ParentNode("div",body_nodes)
    return BodyNode




if __name__ == "__main__":
    markdown = """
# Block to HTML

I'm going to give you quite a few steps to do with a bit less guidance. _I think you're a beautiful peacock and are ready for it._

![I'm a peacock from the other guys](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/bTynJfz.jpeg)

## Assignment

Create a new function called `def markdown_to_html_node(markdown):` that converts a full markdown document into a single parent `HTMLNode`. That one parent `HTMLNode` should of course contain many child `HTMLNode` objects representing the nested elements.

I created an additional 8 helper functions to keep my code neat and easy to understand, because there's a _lot_ of logic necessary for the `markdown_to_html_node`. I don't want to give you my exact functions because I want you to do this from scratch. However, I'll give you the basic order of operations:

1. [ ] Split the markdown into blocks (you already have a function for this)
2. [ ] Loop over each block
3. [ ] Make all the block nodes children under a single parent HTML node (which should just be a [`div`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/div)) and return it.

* this is *unordered* list.
* this is the **second** item on said list.
* this could be the **third** idk it is unordered.

Create unit tests.

```python
print("hello world")
def test_this(text):
    print(text)
```

> this is a quote just testing if my markdown to html cathes this.
"""
    html = markdown_to_html_node(markdown)
    for child in html.children:
        if isinstance(child,ParentNode):
            print(child.__class__, child.tag)
            #print(type(child.children))
            for sub_child in child.children:
                #print(type(sub_child))
                print(sub_child)
        else:
            print(child)
    # print(html.to_html())