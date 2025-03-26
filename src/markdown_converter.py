import re
from textnode import TextType, TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type): 
    new_nodes = []
    for node in old_nodes: 
        if node.text_type != TextType.TEXT: 
            new_nodes.append(node)
        else: 
            split = node.text.split(delimiter)
            if len(split) == 2: 
                raise Exception("Invalid Markdown Syntax: matching delimiter not found")
            for i in range(len(split)):
                if split[i] == "": 
                    continue
                if i % 2 == 1: 
                    new_nodes.append(TextNode(split[i], text_type))
                else: 
                    new_nodes.append(TextNode(split[i], TextType.TEXT))
    return new_nodes
            

def extract_markdown_images(text): 
    images = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return images

def extract_markdown_links(text): 
    images = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return images
