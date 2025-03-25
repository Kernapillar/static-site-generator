from textnode import TextType, TextNode
from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode


def main(): 
    test_node = TextNode("test Text", TextType.LINK, "https://www.alex.com")
    print(test_node)
    html_node = HTMLNode("p", "test value", [], {"test prop key": "test prop value"})
    print(html_node)
    parent_node = ParentNode(
    "p",
        [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ],
    )

    print(parent_node)

main()