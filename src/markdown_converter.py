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


def split_nodes_image(old_nodes): 
    new_nodes = []
    for node in old_nodes: 
        images = extract_markdown_images(node.text)
        if len(images) == 0: 
            new_nodes.append(node)
            continue
        new_nodes.extend(extraction(node.text, images))
    return new_nodes

def extraction(text, images):
    result = [] 
    if len(images) == 0 or len(text) == 0: 
        return 
    alt_code, image_url = images[0]
    split = text.split(f"![{alt_code}]({image_url})")
    if len(split[0]) > 0:
        result.append(TextNode(split[0], TextType.TEXT))
    result.append(TextNode(alt_code, TextType.IMAGE, image_url))
    next =  extraction(split[1], images[1:])
    if next != None: 
        result += next
    return result 