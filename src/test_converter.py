import unittest
from textnode import TextNode, TextType
from leafnode import LeafNode
from converter import text_node_to_html_node

class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_normal_text(self):
        text_node = TextNode(text_type=TextType.NORMAL, text="Hello World")
        html_node = text_node_to_html_node(text_node)
        self.assertIsInstance(html_node, LeafNode)  # Ensure an HTMLNode is returned
        self.assertEqual(html_node.tag, None)  # No tag for normal text
        self.assertEqual(html_node.value, "Hello World")  # Check the value
        self.assertEqual(html_node.props, None)  # Ensure no additional props

    def test_bold_text(self):
        text_node = TextNode(text_type=TextType.BOLD, text="Bold Text")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, "b")  # Bold tag
        self.assertEqual(html_node.value, "Bold Text")  # Check the value
        self.assertEqual(html_node.props, None)

    def test_italic_text(self):
        text_node = TextNode(text_type=TextType.ITALIC, text="Italic Text")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, "i")  # Italic tag
        self.assertEqual(html_node.value, "Italic Text")
        self.assertEqual(html_node.props, None)

    def test_code_text(self):
        text_node = TextNode(text_type=TextType.CODE, text="print('Hello')")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, "code")  # Code tag
        self.assertEqual(html_node.value, "print('Hello')")
        self.assertEqual(html_node.props, None)

    def test_link_text(self):
        text_node = TextNode(
            text_type=TextType.LINKS,
            text="Boot.dev",
            url="https://boot.dev"
        )
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, "a")  # Link tag
        self.assertEqual(html_node.value, "Boot.dev")  # Anchor text
        self.assertEqual(html_node.props, {"href": "https://boot.dev"})  # Ensure the props contain 'href'


    def test_invalid_text_type(self):
        # Use a fake text type not defined in the TextType enum
        class FakeTextType:
            UNKNOWN = "UNKNOWN"

        # Create a TextNode with an invalid text_type
        text_node = TextNode(
            text_type=FakeTextType.UNKNOWN,  # This is invalid since it's not in TextType
            text="This should fail"
        )

    def test_non_textnode_input(self):
        non_textnode = "This is not a TextNode!"
        with self.assertRaises(TypeError):  # Expect TypeError for invalid input type
            text_node_to_html_node(non_textnode)

if __name__ == "__main__":
    unittest.main()