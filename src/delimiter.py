from textnode import *

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for nodes in old_nodes:     
        if nodes.text_type != TextType.NORMAL:
            new_nodes.append(nodes)
        
        else:
            count = nodes.text.count(delimiter)
            if count == 2:
                chunks = nodes.text.split(delimiter)
                for i, chunk in enumerate(chunks):
                    if i % 2 == 0:
                        new_nodes.append(TextNode(chunk, TextType.NORMAL))
                    else:
                        new_nodes.append(TextNode(chunk, text_type))
            elif count < 2:
                raise Exception("Mismatched or missing delimiters in the text node")
            elif count > 2:
                raise Exception("Extra delimiters detected in the text node")
            
    return new_nodes