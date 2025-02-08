from textnode import TextNode, TextType
from split import *

def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.NORMAL)]
    nodes = split_nodes_bold(nodes)
    nodes = split_nodes_italic(nodes)
    nodes = split_nodes_code(nodes)
    nodes = split_nodes_images(nodes)
    nodes = split_nodes_link(nodes)
    return nodes
