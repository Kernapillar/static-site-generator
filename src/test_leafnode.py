import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_eq(self):
        node = LeafNode("p", "test value")
        node2 = LeafNode("p", "test value")
        self.assertEqual(node, node2)

    def test_leaf_to_html(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html2(self):
        node = LeafNode("a", "Hello, world!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Hello, world!</a>')

    def test_value_error(self): 
        with self.assertRaises(ValueError): 
            LeafNode("p", None)


if __name__ == "__main__":
    unittest.main()