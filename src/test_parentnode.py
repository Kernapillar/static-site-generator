import unittest

from parentnode import ParentNode
from leafnode import LeafNode


class TestParentNode(unittest.TestCase):
    def test_eq(self):
        node = ParentNode("p", "test value")
        node2 = ParentNode("p", "test value")
        self.assertEqual(node, node2)

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_value_error(self): 
        with self.assertRaises(ValueError): 
            ParentNode(None, [1, 2, 3])

    def test_value_error2(self): 
        with self.assertRaises(ValueError): 
            ParentNode("p", None)

    def test_child_value_error(self): 
        with self.assertRaises(ValueError): 
            ParentNode("p", [LeafNode("p", None)])

    def test_repr(self): 
        expected = """tag: p 
 value: None 
 children: [tag: b 
 value: Bold text 
 children: None 
 props: None, tag: None 
 value: Normal text 
 children: None 
 props: None, tag: i 
 value: italic text 
 children: None 
 props: None, tag: None 
 value: Normal text 
 children: None 
 props: None] 
 props: None"""
        parent_node = ParentNode(
            "p",
                [
                    LeafNode("b", "Bold text"),
                    LeafNode(None, "Normal text"),
                    LeafNode("i", "italic text"),
                    LeafNode(None, "Normal text"),
                ],
            )
        self.assertEqual(str(parent_node), expected)

if __name__ == "__main__":
    unittest.main()