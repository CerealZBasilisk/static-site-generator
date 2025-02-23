from enum import Enum
from constants import BLOCK_PATTERNS_REGEX_STR , BlockType
import re



def block_to_block_type(block: str) -> BlockType:
    for block_type, pattern in BLOCK_PATTERNS_REGEX_STR.items():
        if re.match(pattern, block, re.MULTILINE):
            if block_type == BlockType.ORDERED_LIST:
                lines = block.split('\n')
                expected_number = 1
                for line in lines:
                    if not line.startswith(f"{expected_number}. "):
                        return BlockType.PARAGRAPH
                    expected_number += 1
            return block_type
    return BlockType.PARAGRAPH