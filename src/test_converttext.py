import unittest
from textnode import *
from converttext import *

class TestConvertText(unittest.TestCase):
    def test_text_to_textnodes(self):
        # Test basic text
        text = "Hello world"
        nodes = text_to_textnodes(text)
        assert len(nodes) == 1
        assert nodes[0].text == "Hello world"
        assert nodes[0].text_type == TextType.NORMAL

        # Test bold
        text = "Hello **world**"
        nodes = text_to_textnodes(text)
        assert len(nodes) == 2
        assert nodes[0].text == "Hello "
        assert nodes[0].text_type == TextType.NORMAL
        assert nodes[1].text == "world"
        assert nodes[1].text_type == TextType.BOLD

        # Test italic
        text = "Hello *world*"
        nodes = text_to_textnodes(text)
        assert len(nodes) == 2
        assert nodes[0].text == "Hello "
        assert nodes[0].text_type == TextType.NORMAL
        assert nodes[1].text == "world"
        assert nodes[1].text_type == TextType.ITALIC

        text = "Hello `world`"
        nodes = text_to_textnodes(text)
        assert len(nodes) == 2
        assert nodes[0].text == "Hello "
        assert nodes[0].text_type == TextType.NORMAL
        assert nodes[1].text == "world"
        assert nodes[1].text_type == TextType.CODE

        text = "Click [here](https://boot.dev)"
        nodes = text_to_textnodes(text)
        assert len(nodes) == 2
        assert nodes[0].text == "Click "
        assert nodes[0].text_type == TextType.NORMAL
        assert nodes[1].text == "here"
        assert nodes[1].text_type == TextType.LINKS
        assert nodes[1].url == "https://boot.dev"

        text = "Here's an ![image](https://i.imgur.com/zjjcJKZ.png)"
        nodes = text_to_textnodes(text)
        assert len(nodes) == 2
        assert nodes[0].text == "Here's an "
        assert nodes[0].text_type == TextType.NORMAL
        assert nodes[1].text == "image"
        assert nodes[1].text_type == TextType.IMAGES
        assert nodes[1].url == "https://i.imgur.com/zjjcJKZ.png"


if __name__ == "__main__":
    unittest.main()