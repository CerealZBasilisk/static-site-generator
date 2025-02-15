from textnode import TextType

ENUM_TEXT_TAG_STR = {
    "raw": "",
    "bold": "b",
    "italic": "i",
    "code": "code",
    "link": "a",
    "image": "img"
}


LINK_REGEX = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
IMAGE_REGEX = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
