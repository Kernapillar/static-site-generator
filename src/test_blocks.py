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

    def test_paragraphs(self):
        md = """
    This is **bolded** paragraph
    text in a p
    tag here

    This is another paragraph with _italic_ text and `code` here

    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_header(self):
        md = """
    ###This is **bolded** header
    text in a p
    tag here

    #This is another header with _italic_ text and `code` here

    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h3>This is <b>bolded</b> header text in a p tag here</h3><h1>This is another header with <i>italic</i> text and <code>code</code> here</h1></div>",
        )

    def test_eval_header(self): 
        block = "##### Should end up with 5"
        self.assertEqual(eval_header(block), 5)

    def test_eval_header2(self): 
        block = "####### Should end up with 6, despite 7 hashtags "
        self.assertEqual(eval_header(block), 6)

    def test_codeblock(self):
        md = """
    ```
    This is text that _should_ remain
    the **same** even with inline stuff
    ```
    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_quote(self):
        md = """
    >This is **bolded** quote
    >text in a blockquote
    >tag here

    >This is another quote with _italic_ text and `code` here

    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is <b>bolded</b> quote text in a blockquote tag here</blockquote><blockquote>This is another quote with <i>italic</i> text and <code>code</code> here</blockquote></div>",
        )

    def test_unordered_list(self):
        md = """
    - This is an unordered list
    - testing another line
    - li tags within a ul tag
    - final line of the unordered list

    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is an unordered list</li><li>testing another line</li><li>li tags within a ul tag</li><li>final line of the unordered list</li></ul></div>",
        )

    def test_ordered_list(self):
        md = """
    1. This is an ordered list
    2. testing another line
    3. li tags within a ol tag
    4. final line of the ordered list

    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>This is an ordered list</li><li>testing another line</li><li>li tags within a ol tag</li><li>final line of the ordered list</li></ol></div>",
        )

    def test_clean_lines(self): 
            block = """
        >This is a line that needs to be cleaned
        >This is a second line that needs the quote marker removed

        """
            clean = clean_lines(block, ">")
            self.assertEqual(
                clean, "This is a line that needs to be cleaned This is a second line that needs the quote marker removed"
            )


if __name__ == "__main__":
    unittest.main()