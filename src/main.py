from textnode import TextType, TextNode
from htmlnode import HTMLNode


def main(): 
    test_node = TextNode("test Text", TextType.LINK, "https://www.alex.com")
    print(test_node)
    html_node = HTMLNode("p", "test value", [], {"test prop key": "test prop value"})
    print(html_node)

main()