import re
from enum import Enum
from htmlnode import *
from textnode import *
from parentnode import *
from markdown_converter import text_to_textnodes
class BlockType(Enum): 
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDEREDLIST = "unordered list"
    ORDEREDLIST = "ordered list"

def markdown_to_blocks(markdown): 
    blocks = markdown.split("\n\n")
    result = []
    for block in blocks: 
        block = block.strip()
        lines = block.split("\n")
        lines = [line.strip() for line in lines]
        block = "\n".join(lines)
        if len(block) > 0: 
            result.append(block)
    return result

def block_to_block_type(block): 
    if block.startswith("#"): 
        return BlockType.HEADING
    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
    lines = block.split("\n")
    if all(line.startswith(">") for line in lines): 
        return BlockType.QUOTE
    if all(line.startswith("- ") for line in lines): 
        return BlockType.UNORDEREDLIST
    ordered = True
    for i in range(len(lines)): 
        if lines[i].startswith(f"{i + 1}. ") != True: 
            ordered = False
    if ordered: 
        return BlockType.ORDEREDLIST
    else: 
        return BlockType.PARAGRAPH
    
def markdown_to_html_node(markdown): 
    blocks = markdown_to_blocks(markdown)
    child_list = []
    for block in blocks: 
        type = block_to_block_type(block)
        match type: 
            case BlockType.PARAGRAPH: 
                normalized_text = " ".join(block.split())
                children = text_to_children(normalized_text)
                paragraph = ParentNode("p", children)
                child_list.append(paragraph)
            case BlockType.HEADING: 
                header_num = eval_header(block)
                block = block[header_num:]
                normalized_text = " ".join(block.split())
                children = text_to_children(normalized_text)
                header = ParentNode(f"h{header_num}", children)
                child_list.append(header)
            case BlockType.CODE: 
                block = block.strip("```").lstrip("\n")
                textnode = TextNode(block, TextType.TEXT)
                html_node = text_node_to_html_node(textnode)
                code = ParentNode("code", [html_node])
                pre = ParentNode("pre", [code])
                child_list.append(pre)
            case BlockType.QUOTE: 
                block = clean_lines(block, "> ")
                children = text_to_children(block)
                quote = ParentNode("blockquote", children)
                child_list.append(quote)
            case BlockType.UNORDEREDLIST: 
                lines = block.split("\n")
                line_nodes = format_list(lines)
                unordered_list = ParentNode("ul", line_nodes)
                child_list.append(unordered_list)
            case BlockType.ORDEREDLIST: 
                lines = block.split("\n")
                line_nodes = format_list(lines, True)
                unordered_list = ParentNode("ol", line_nodes)
                child_list.append(unordered_list)
    parent = ParentNode("div", child_list)
    return parent

def text_to_children(text):
    nodes = text_to_textnodes(text)
    children = []
    for node in nodes: 
        html_node = text_node_to_html_node(node)
        children.append(html_node)
    return children

def eval_header(block): 
    count = 0 
    for i in range(len(block)): 
        if count >= 6: 
            return 6
        if block[i] == "#": 
            count += 1
        else: 
            return count
        
def clean_lines(block, char): 
    lines = block.split()
    lines = list(map(lambda line: line.lstrip(f"{char}"), lines))
    return " ".join(lines)

def format_list(lines, ordered=False): 
    new_lines = []
    if not ordered: 
        for line in lines: 
            line = line[2:]
            li_node = ParentNode("li", text_to_children(line))
            new_lines.append(li_node)
    else: 
        for line in lines: 
            line = re.sub(r"^\d+\.\s+", "", line)
            li_node = ParentNode("li", text_to_children(line))
            new_lines.append(li_node)
    return new_lines
