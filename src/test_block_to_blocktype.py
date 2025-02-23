import unittest

from block_to_blocktype import block_to_block_type, BlockType


class TestBlockType(unittest.TestCase):
    def test_heading_blocks(self):
        self.assertEqual(block_to_block_type("# Heading 1"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("## Heading 2"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("###### Heading 6"), BlockType.HEADING)
    
    def test_paragraph_blocks(self):
        self.assertEqual(block_to_block_type("Just a normal paragraph"), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type("Multiple\nline\nparagraph"), BlockType.PARAGRAPH)
    
    def test_code_blocks(self):
        self.assertEqual(block_to_block_type("```\ncode block\n```"), BlockType.CODE)
        self.assertEqual(block_to_block_type("```python\ndef hello():\n    pass\n```"), BlockType.CODE)
    
    def test_quote_blocks(self):
        self.assertEqual(block_to_block_type(">Single line quote"), BlockType.QUOTE)
        self.assertEqual(block_to_block_type(">Multiple\n>line\n>quote"), BlockType.QUOTE)
    
    def test_unordered_list_blocks(self):
        self.assertEqual(block_to_block_type("* Item 1\n* Item 2"), BlockType.UNORDERED_LIST)
        self.assertEqual(block_to_block_type("- Item 1\n- Item 2"), BlockType.UNORDERED_LIST)
        
    def test_ordered_list_blocks(self):
        self.assertEqual(block_to_block_type("1. First item\n2. Second item"), BlockType.ORDERED_LIST)
        self.assertEqual(block_to_block_type("1. First\n2. Second\n3. Third"), BlockType.ORDERED_LIST)

    def test_invalid_blocks(self):
        # These should be paragraphs since they don't strictly match the rules
        self.assertEqual(block_to_block_type("#No space after hash"), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type("####### Too many hashes"), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type("1.No space after period"), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type("*No space after asterisk"), BlockType.PARAGRAPH)

    def test_malformed_ordered_lists(self):
        # These should be paragraphs since they don't follow the 1,2,3 sequence
        self.assertEqual(block_to_block_type("2. Wrong start\n3. Wrong sequence"), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type("1. First\n3. Skipped number"), BlockType.PARAGRAPH)

if __name__ == "__main__":
    unittest.main()