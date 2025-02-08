from extractor import * 
from textnode import TextNode, TextType

def split_nodes_images(old_nodes):
    result = []
    for node in old_nodes:
        links = extract_markdown_images(node.text)
        if not links:
            result.append(node)
            continue
        
        current_text = node.text
        for alt_text, href in links:
            markdown_link = f"![{alt_text}]({href})"
            parts = current_text.split(markdown_link, 1)

            if parts[0]:
                result.append(TextNode(parts[0], TextType.NORMAL))
            
            result.append(TextNode(alt_text, TextType.IMAGES, href))

            if len(parts) > 1:
                current_text = parts[1]

        if current_text:
            result.append(TextNode(current_text, TextType.NORMAL))

    return result


def split_nodes_link(old_nodes):
    result = []
    for node in old_nodes:
        links = extract_markdown_links(node.text)
        if not links:
            result.append(node)
            continue
        
        current_text = node.text
        for link_text, url in links:
            markdown_link = f"[{link_text}]({url})"
            parts = current_text.split(markdown_link, 1)

            if parts[0]:
                result.append(TextNode(parts[0], TextType.NORMAL))
            
            result.append(TextNode(link_text, TextType.LINKS, url))

            if len(parts) > 1:
                current_text = parts[1]

        if current_text:
            result.append(TextNode(current_text, TextType.NORMAL))

    return result

def split_nodes_bold(old_nodes):
    result = []
    for node in old_nodes:
        if node.text_type != TextType.NORMAL:
            result.append(node)
            continue

        pieces = node.text.split("**")
        # If no bold markers found, keep original node
        if len(pieces) == 1:
            result.append(node)
            continue

        for i, piece in enumerate(pieces):
            if piece == "":
                continue
            # Even pieces are regular text, odd pieces are bold
            text_type = TextType.BOLD if i % 2 else TextType.NORMAL
            result.append(TextNode(piece, text_type))
            
    return result

def split_nodes_italic(old_nodes):
    result = []
    for node in old_nodes:
        if node.text_type != TextType.NORMAL:
            result.append(node)
            continue

        pieces = node.text.split("*")
        # If no bold markers found, keep original node
        if len(pieces) == 1:
            result.append(node)
            continue

        for i, piece in enumerate(pieces):
            if piece == "":
                continue
            # Even pieces are regular text, odd pieces are bold
            text_type = TextType.ITALIC if i % 2 else TextType.NORMAL
            result.append(TextNode(piece, text_type))
            
    return result

def split_nodes_code(old_nodes):
    result = []
    for node in old_nodes:
        if node.text_type != TextType.NORMAL:
            result.append(node)
            continue

        pieces = node.text.split("`")
        # If no bold markers found, keep original node
        if len(pieces) == 1:
            result.append(node)
            continue

        for i, piece in enumerate(pieces):
            if piece == "":
                continue
            # Even pieces are regular text, odd pieces are bold
            text_type = TextType.CODE if i % 2 else TextType.NORMAL
            result.append(TextNode(piece, text_type))
            
    return result