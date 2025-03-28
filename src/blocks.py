from enum import Enum
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