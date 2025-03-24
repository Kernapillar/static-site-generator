from textnode import TextType, TextNode


def main(): 
    test_node = TextNode("test Text", TextType.LINK, "https://www.alex.com")
    print(test_node)

main()