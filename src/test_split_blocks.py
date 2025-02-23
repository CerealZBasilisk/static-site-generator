import unittest

from split_blocks import markdown_to_blocks


class TestMarkdownToBlocks(unittest.TestCase):

    def test_one_word_blocks(self):
        # Test basic code block
        markdown = "This\n\n is\n\n text "
        blocks = markdown_to_blocks(markdown)
        self.assertEqual(len(blocks), 3)
        
        
        

    def test_text(self):
        markdown = "This is one line\n\nthis is another line\n\nin this test each line is a paragrapgh "
        blocks = markdown_to_blocks(markdown)
        self.assertEqual(len(blocks), 3)
        self.assertEqual(blocks[0], "This is one line")
        self.assertEqual(blocks[1], "this is another line")
        self.assertEqual(blocks[2], "in this test each line is a paragrapgh")

    def test_multiple_empty_lines(self):
        markdown = "  \n\n  \n\n   "
        blocks = markdown_to_blocks(markdown)
        self.assertEqual(len(blocks), 0)
    
    def test_cases_markdown(self):
        test_cases = [
            ("# Heading\n\nParagraph\n\n* List",3,["# Heading","Paragraph","* List"]),
            ("# Heading\n\n\n\nParagraph\n\n* List",3,["# Heading","Paragraph","* List"]),
            ("\n\n# Heading\n\nParagraph\n\n* List\n\n",3,["# Heading","Paragraph","* List"]),
            ("   # Heading   \n\n   Paragraph   \n\n   * List   ",3,["# Heading","Paragraph","* List"])
        ]
        for markdown, length, tests in test_cases:
            blocks = markdown_to_blocks(markdown)
            self.assertEqual(len(blocks), length)
            self.assertEqual(len(blocks), len(tests))
            for block, expected in zip(blocks, tests):
                self.assertEqual(block, expected)

            

    def test_empty_lines_between_points_markdown(self):
        markdown = "#This is one line\n\n*this is another line\n*this is another line\n*this is another line\n\nin this test each line is a paragrapgh "
        blocks = markdown_to_blocks(markdown)
        self.assertEqual(len(blocks), 3)
        self.assertEqual(blocks[0], "#This is one line")
        self.assertEqual(blocks[1], "*this is another line\n*this is another line\n*this is another line")
        self.assertEqual(blocks[2], "in this test each line is a paragrapgh")


    def test_multiline(self):

     test_cases = [("""# Getting Started with Python

This is a paragraph that contains *italic* and **bold** text.
It can even span multiple lines without being split.
As long as there's no blank line, it's one block.

* First list item
* Second list item with **bold**
* Third list item with *italic*

Final paragraph here.""",4)

,("""# Code Examples

Here's a code block:

```python
def hello_world():
print('Hello World')
```

And here's a quote:

> This is a blockquote
> It can span multiple lines
> Like this
    """,5)]
     for case, length in test_cases:

         blocks = markdown_to_blocks(case)

         self.assertEqual(len(blocks),length)


if __name__ == "__main__":
    unittest.main()