from textnode import TextNode, TextType
from htmlnode import HTMLNode
from parentnode import ParentNode
from leafnode import LeafNode
from constants import *



def text_node_to_html_node(text_node):
    if not text_node.text_type.value in ENUM_TEXT_TAG_STR:
        raise ValueError(f"text type unsupported: {text_node.text_type.value}")
    match text_node.text_type.value:
        case "raw":
            if text_node.url:
                raise ValueError("raw text cant have a url")
            return LeafNode(tag=None, value=text_node.text)
        
        
        case "bold" | "italic" | "code":
            tag = ENUM_TEXT_TAG_STR[text_node.text_type.value]
            value = text_node.text
            if text_node.url:
                raise ValueError(f"{text_node.text_type.value}cant have a url")
            return LeafNode(tag=tag, value=value, props=None)
        
        
        case "link":
            tag = ENUM_TEXT_TAG_STR[text_node.text_type.value]
            value = text_node.text
            if text_node.url:
                prop = {"href": text_node.url}
            else:
                raise ValueError("expects URL or source for link")
            return LeafNode(tag=tag, value=value, props=prop)
        
        case "image":
            tag = ENUM_TEXT_TAG_STR[text_node.text_type.value]
            value = ""
            if text_node.url:
                prop = {
                    "src": text_node.url, 
                    "alt": text_node.text
                    }
            else:
                raise ValueError("expects URL or source for image")
            return LeafNode(tag=tag, value=value, props=prop)
        
        

    
    
    

    


