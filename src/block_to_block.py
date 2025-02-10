

def block_to_block_type(block):
    if block.startswith("#"):
        count = 0
        for char in block:
            if char == "#":
                count += 1
            else:
                break
        
        if 1 <= count <= 6 and block[count] == " ":
            return "heading"

    if block.startswith("```") and block.endswith("```"):
        return "code"
    
    lines = block.split("\n")
    all_lines_are_quotes = True
    for line in lines:
        if not line.startswith(">"): 
            all_lines_are_quotes = False
            break
    
    if all_lines_are_quotes:
        return "quote"
    
    all_lines_are_unordered = True
    for line in lines:
        if not (line.startswith("* ") or line.startswith("- ")):
            all_lines_are_unordered = False
            break

    if all_lines_are_unordered:
        return "unordered_list"

    all_lines_are_ordered = True
    expected_number = 1
    for line in lines:
        if not line.startswith(f"{expected_number}. "):
            all_lines_are_ordered = False
            break
        expected_number += 1

    if all_lines_are_ordered:
        return "ordered_list"


    return "paragraph"