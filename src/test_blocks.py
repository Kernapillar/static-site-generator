import unittest

from blocks import *


class TestMarkdownConverter(unittest.TestCase):

    def test_markdown_to_blocks(self):
        md = """
    This is **bolded** paragraph

    This is another paragraph with _italic_ text and `code` here
    This is the same paragraph on a new line

    - This is a list
    - with items
    """
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_empty_line(self):
        md = """
    This is **bolded** paragraph


    This is another paragraph with _italic_ text and `code` here
    This is the same paragraph on a new line

    
    - This is a list
    - with items
    """
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )



    def test_markdown_to_blocks_extra_whitespace(self):
        md = """
    This is **bolded** paragraph            

    This is another paragraph with _italic_ text and `code` here        
    This is the same paragraph on a new line            

    - This is a list
    - with items        
    """
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_block_to_blocktype_heading(self): 
        block = "# This is a Heading block"
        type = block_to_block_type(block)
        self.assertEqual(type, BlockType.HEADING)

    def test_block_to_blocktype_heading2(self): 
        block = "### This is a Heading block"
        type = block_to_block_type(block)
        self.assertEqual(type, BlockType.HEADING)

    def test_block_to_blocktype_heading3(self): 
        block = "3### This is not a Heading block"
        type = block_to_block_type(block)
        self.assertNotEqual(type, BlockType.HEADING)

    def test_block_to_blocktype_code(self): 
        block = "``` This is a Code block```"
        type = block_to_block_type(block)
        self.assertEqual(type, BlockType.CODE)

    def test_block_to_blocktype_code2(self): 
        block = "`` This is not a Code block``"
        type = block_to_block_type(block)
        self.assertNotEqual(type, BlockType.CODE)

    def test_block_to_blocktype_code3(self): 
        block = "``` This is not a Code block``"
        type = block_to_block_type(block)
        self.assertNotEqual(type, BlockType.CODE)

    def test_block_to_blocktype_quote(self): 
        block = "> this \n> is \n> a \n> quote \n> block"
        type = block_to_block_type(block)
        self.assertEqual(type, BlockType.QUOTE)

    def test_block_to_blocktype_quote2(self): 
        block = "> this \n> is \nnot \n> a \n> quote \n> block"
        type = block_to_block_type(block)
        self.assertNotEqual(type, BlockType.QUOTE)

    def test_block_to_blocktype_unordered_list(self): 
        block = "-  this \n-  is \n-  an \n-  unordered list \n-  block"
        type = block_to_block_type(block)
        self.assertEqual(type, BlockType.UNORDEREDLIST)

    def test_block_to_blocktype_unordered_list2(self): 
        block = "-  this \n-  is \nnot \n-  an \n-  unordered list \n-  block"
        type = block_to_block_type(block)
        self.assertNotEqual(type, BlockType.UNORDEREDLIST)

    def test_block_to_blocktype_ordered_list(self): 
        block = "1. this \n2. is \n3. an \n4. ordered list \n5. block"
        type = block_to_block_type(block)
        self.assertEqual(type, BlockType.ORDEREDLIST)

    def test_block_to_blocktype_ordered_list2(self): 
        block = "1. this \n2. is \n3. not \n4. an \n4. ordered list \n5. block"
        type = block_to_block_type(block)
        self.assertNotEqual(type, BlockType.ORDEREDLIST)

    def test_block_to_blocktype_paragraph(self): 
        block = "This is a paragraph block"
        type = block_to_block_type(block)
        self.assertEqual(type, BlockType.PARAGRAPH)

if __name__ == "__main__":
    unittest.main()