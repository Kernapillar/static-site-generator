import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("p", "test value")
        node2 = HTMLNode("p", "test value")
        self.assertEqual(node, node2)

    def test_props_to_html(self):
        node = HTMLNode("p", "test value", [], {"test prop key": "test prop value"})
        res = ' test prop key="test prop value"'
        self.assertEqual(node.props_to_html(), res)

    def test_repr(self): 
        node = HTMLNode("p", "test value", [], {"test prop key": "test prop value"})
        res = """tag: p \n value: test value \n children: [] \n props: {'test prop key': 'test prop value'}"""
        self.assertEqual(str(node), res)


if __name__ == "__main__":
    unittest.main()