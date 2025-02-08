import unittest
from textnode import *
from split import split_nodes_images, split_nodes_link

class TestSplit(unittest.TestCase):
    def test_empty_nodes(self):
        nodes = []
        assert split_nodes_images(nodes) == []
        assert split_nodes_link(nodes) == []
        
    def test_empty_nodes(self):
        node = TextNode("Just plain text", TextType.NORMAL)

        #test split_nodes_link
        result = split_nodes_link([node])
        assert len(result) == 1
        assert result[0].text == "Just plain text"
        assert result[0].text_type == TextType.NORMAL
        
        #test split_nodes_images
        result = split_nodes_images([node])
        assert len(result) == 1
        assert result[0].text == "Just plain text"
        assert result[0].text_type == TextType.NORMAL

    def test_single_link(self):
        #test text with one link in the middle
        node = TextNode("Click [here](https://boot.dev) for more", TextType.NORMAL)
        result = split_nodes_link([node])
        
        assert len(result) == 3
        assert result[0].text == "Click "
        assert result[0].text_type == TextType.NORMAL
        assert result[1].text == "here"
        assert result[1].text_type == TextType.LINKS
        assert result[1].url == "https://boot.dev"
        assert result[2].text == " for more"
        assert result[2].text_type == TextType.NORMAL

    def test_single_image(self):
        # Test a simple case with one image in the middle
        node = TextNode("Start ![image](test.png) end", TextType.NORMAL)
        result = split_nodes_images([node])
        
        assert len(result) == 3
        assert result[0].text == "Start "
        assert result[0].text_type == TextType.NORMAL
        assert result[1].text == "image"
        assert result[1].text_type == TextType.IMAGES
        assert result[1].url == "test.png"
        assert result[2].text == " end"
        assert result[2].text_type == TextType.NORMAL

    def test_multiple_links(self):
        node = TextNode("Click [here](url1) and [there](url2)", TextType.NORMAL)
        result = split_nodes_link([node])
        
        assert len(result) == 4
        assert result[0].text == "Click "
        assert result[1].text == "here"
        assert result[1].url == "url1"
        assert result[2].text == " and "
        assert result[3].text == "there"
        assert result[3].url == "url2"

    def test_link_at_start(self):
        node = TextNode("[Click](url) at start", TextType.NORMAL)
        result = split_nodes_link([node])
        
        assert len(result) == 2
        assert result[0].text == "Click"
        assert result[0].text_type == TextType.LINKS
        assert result[0].url == "url"
        assert result[1].text == " at start"
        assert result[1].text_type == TextType.NORMAL

    def test_link_at_end(self):
        node = TextNode("End with [link](url)", TextType.NORMAL)
        result = split_nodes_link([node])
        
        assert len(result) == 2
        assert result[0].text == "End with "
        assert result[0].text_type == TextType.NORMAL
        assert result[1].text == "link"
        assert result[1].text_type == TextType.LINKS
        assert result[1].url == "url"

    def test_image_at_start(self):
        node = TextNode("![first](img.png) then text", TextType.NORMAL)
        result = split_nodes_images([node])
        
        assert len(result) == 2
        assert result[0].text == "first"
        assert result[0].text_type == TextType.IMAGES
        assert result[0].url == "img.png"
        assert result[1].text == " then text"
        assert result[1].text_type == TextType.NORMAL

    def test_multiple_images(self):
        node = TextNode("![img1](url1) middle ![img2](url2)", TextType.NORMAL)
        result = split_nodes_images([node])
        
        assert len(result) == 3
        assert result[0].text == "img1"
        assert result[0].text_type == TextType.IMAGES
        assert result[0].url == "url1"
        assert result[1].text == " middle "
        assert result[1].text_type == TextType.NORMAL
        assert result[2].text == "img2"
        assert result[2].text_type == TextType.IMAGES
        assert result[2].url == "url2"

    def test_complex_text_with_links(self):
        node = TextNode("Start [link1](url1) middle [link2](url2) end", TextType.NORMAL)
        result = split_nodes_link([node])
        
        assert len(result) == 5
        assert result[0].text == "Start "
        assert result[1].text == "link1"
        assert result[1].url == "url1"
        assert result[2].text == " middle "
        assert result[3].text == "link2"
        assert result[3].url == "url2"
        assert result[4].text == " end"

    def test_no_split_with_incomplete_markdown(self):
        # Test that incomplete markdown isn't processed
        node = TextNode("This [is not a link and ![not an image", TextType.NORMAL)
        result_links = split_nodes_link([node])
        result_images = split_nodes_images([node])
        
        assert len(result_links) == 1
        assert result_links[0].text == "This [is not a link and ![not an image"
        assert len(result_images) == 1
        assert result_images[0].text == "This [is not a link and ![not an image"

if __name__ == "__main__":
    unittest.main()