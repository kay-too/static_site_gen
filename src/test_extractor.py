import unittest
from extractor import extract_markdown_images, extract_markdown_links

class Extractor(unittest.TestCase):
    def test_extract_markdown_images(self):
        #test single
        text1 = "![alt text](https://example.com/image.jpg)"
        self.assertEqual(
            extract_markdown_images(text1), 
            [("alt text", "https://example.com/image.jpg")]
        )

        #test empty
        self.assertEqual(extract_markdown_images(""), [])

        #test multiple
        text2 = "![img1](url1.jpg) some text ![img2](url2.jpg)"
        self.assertEqual(
            extract_markdown_images(text2),
            [("img1", "url1.jpg"), ("img2", "url2.jpg")]
        )

        #test text with no images
        self.assertEqual(extract_markdown_images("just plain text"), [])

        #test image with spaces in alt text
        text3 = "![my cool image](https://example.com/pic.jpg)"
        self.assertEqual(
            extract_markdown_images(text3),
            [("my cool image", "https://example.com/pic.jpg")]
        )

        #test image mixed with links
        text4 = "[link](url.com) ![image](pic.jpg) [another](link.com)"
        self.assertEqual(
            extract_markdown_images(text4),
            [("image", "pic.jpg")]
        )

    def test_extract_markdown_links(self):
        #test single link
        text1 = "[Boot.dev](https://boot.dev)"
        self.assertEqual(
            extract_markdown_links(text1),
            [("Boot.dev", "https://boot.dev")]
        )

        #test multiple links
        text2 = "[link1](url1.com) text [link2](url2.com)"
        self.assertEqual(
            extract_markdown_links(text2),
            [("link1", "url1.com"), ("link2", "url2.com")]
        )

        # Test empty string
        self.assertEqual(extract_markdown_links(""), [])

        
        #test links with special characters in URL
        text3 = "[complex link](https://api.github.com/users?id=123&type=admin)"
        self.assertEqual(
            extract_markdown_links(text3),
            [("complex link", "https://api.github.com/users?id=123&type=admin")]
        )

        #test links mixed with images
        text4 = "![img](pic.jpg) [link](url.com) ![img2](pic2.jpg)"
        self.assertEqual(
            extract_markdown_links(text4),
            [("link", "url.com")]
        )

if __name__ == "__main__":
    unittest.main()