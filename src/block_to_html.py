from mark_to_blocks import markdown_to_blocks
from htmlnode import *

def is_numbered_list(block):
    if " " not in block:
        return False
    first_word = block.split(" ")[0]
    return first_word[:-1].isdigit() and first_word[-1] == "."


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    parent = HTMLNode("div")
    
    for block in blocks:
        if block.startswith("#"):
            level = 0
            for char in block:
                if char == "#":
                    level += 1
                else:
                    break
            heading_node = HTMLNode(f"h{level}", None, block[level:].strip())
            parent.add_child(heading_node)

        elif block.startswith("```"):
            code_content = block.strip("`")
            code_node = HTMLNode("code", None, code_content)
            pre_node = HTMLNode("pre", None)
            pre_node.add_child(code_node)
            parent.add_child(pre_node)
            
        elif block.startswith(">"):
            quote_content = block[1:].strip()
            quote_node = HTMLNode("blockquote", None, quote_content)
            parent.add_child(quote_node)

        elif block.startswith("-") or block.startswith("*") or block.startswith("+"):
            list_node = HTMLNode("ul", None)
            item_node = HTMLNode("li", None, block[1:].strip())
            list_node.add_child(item_node)
            parent.add_child(list_node)

        elif is_numbered_list(block): 
            list_node = HTMLNode("ol", None)

            content = block[block.find(" ")+1:].strip()
            item_node = HTMLNode("li", None, content)
            list_node.add_child(item_node)
            parent.add_child(list_node)

        else:
            paragraph_node = HTMLNode("p", None, block)
            parent.add_child(paragraph_node)

    return parent