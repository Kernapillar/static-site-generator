import unittest
from main import *

class TestMarkdownConverter(unittest.TestCase):

    def test_extract_title(self):
        md = """
    This is **bolded** paragraph

    This is another paragraph with _italic_ text and `code` here
    # This is the title

    - This is a list
    - with items
    """
        title = extract_title(md)
        self.assertEqual(title, "This is the title")

    def test_extract_title_not_found(self):
        md = """
    This is **bolded** paragraph

    This is another paragraph with _italic_ text and `code` here
    - This is a list
    - with items
    """
        with self.assertRaises(Exception): 
            title = extract_title(md)