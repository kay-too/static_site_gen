def markdown_to_blocks(markdown):
    split_text = markdown.split("\n")

    block = []
    current_block = []
    for line in split_text: 
        if line == "":
            joined_blocks = " ".join(current_block).strip()
            if joined_blocks:
                block.append(joined_blocks)
            current_block = []
        else:
            current_block.append(line)
    
    if current_block:
        joined_blocks = " ".join(current_block).strip()
        if joined_blocks:
            block.append(joined_blocks)
    
    return block