import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
        
        node3 = TextNode("This is a test",TextType.LINKS)
        node4 = TextNode("This is a test",TextType.IMAGES)
        self.assertNotEqual(node3, node4)

        node5 = TextNode("This is a url test",TextType.NORMAL,"test.com")
        node6 = TextNode("This is a url test",TextType.NORMAL)
        self.assertNotEqual(node5, node6)

        node7 = TextNode("This is another url test",TextType.NORMAL,"test.com")
        node8 = TextNode("This is another url test",TextType.NORMAL,"anotherurl.com")
        self.assertNotEqual(node7, node8)

        node9 = TextNode("Text content test",TextType.NORMAL)
        node10 = TextNode("Different text for the Text content test",TextType.NORMAL)
        self.assertNotEqual(node9, node10)

        node11 = TextNode("This is a case sensitivity test",TextType.NORMAL)
        node12 = TextNode("THIS IS A CASE SENSITIVITY TEST",TextType.NORMAL)
        self.assertNotEqual(node11, node12)

        node13 = TextNode("None as a URL vs empty string",TextType.NORMAL,None)
        node14 = TextNode("None as a URL vs empty string",TextType.NORMAL,"")
        self.assertNotEqual(node13, node14)

if __name__ == "__main__":
    unittest.main()