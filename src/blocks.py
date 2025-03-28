

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