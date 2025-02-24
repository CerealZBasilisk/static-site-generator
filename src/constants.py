from enum import Enum


class TextType(Enum):
    TEXT = "raw"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

ENUM_TEXT_TAG_STR = {
    "raw": "",
    "bold": "b",
    "italic": "i",
    "code": "code",
    "link": "a",
    "image": "img"
}

BLOCK_TAG_STR ={
    BlockType.PARAGRAPH: "p",
    BlockType.HEADING: "h",
    BlockType.CODE: "code",
    BlockType.QUOTE: "blockquote",
    BlockType.UNORDERED_LIST: "ul",
    BlockType.ORDERED_LIST: "ol",
}

BLOCK_PATTERNS_REGEX_STR = {
    BlockType.HEADING: r'^#{1,6}\s.*$',
    BlockType.QUOTE: r'^>.*$',
    BlockType.CODE: r'^```[\s\S]*```$',
    BlockType.UNORDERED_LIST: r'^(?:\*\s.*|\-\s.*)(?:\n(?:\*\s.*|\-\s.*))*$',
    BlockType.ORDERED_LIST: r'^1\.\s.*(?:\n[2-9]\.\s.*)*$'
}

LINK_REGEX = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
IMAGE_REGEX = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
H1_REGEX = r"^#\s(.*)"
FILENAME_REGEX =r".*/([^/]+)\.md$"