def text_node_to_html_node(text_node):
    from textnode import TextNode
    from leafnode import LeafNode

    if not isinstance(text_node, TextNode):
        raise TypeError("Input must be an instance of TextNode!")
    
    if text_node.text_type == text_node.text_type.NORMAL:
        return LeafNode(tag=None, value=text_node.text)
    
    elif text_node.text_type == text_node.text_type.BOLD:
        return LeafNode(tag="b", value=text_node.text)

    elif text_node.text_type == text_node.text_type.ITALIC:
        return LeafNode(tag="i", value=text_node.text)
    
    elif text_node.text_type == text_node.text_type.CODE:
        return LeafNode(tag="code", value=text_node.text)
    
    elif text_node.text_type == text_node.text_type.LINKS:
        return LeafNode(tag="a", value=text_node.text, props={"href": text_node.url})
    
    elif text_node.text_type == text_node.text_type.IMAGES:
        return LeafNode(tag="img", value="", props={"src": text_node.url, "alt": text_node.alt_text})
    
    else:
        raise ValueError("Unknown TextType in TextNode!")