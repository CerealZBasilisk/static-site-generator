def markdown_to_blocks(markdown: str):
    markdown_blocks = markdown.split("\n\n")
    results = [block.strip() for block in markdown_blocks if block.strip() != ""]
    return results






if __name__ == "__main__":
    markdown = """# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item
"""

    test = markdown_to_blocks(markdown)
    for i, block in enumerate(test):
        print(f"block: {i}", block)