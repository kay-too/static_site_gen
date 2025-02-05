import unittest
from textnode import *
from leafnode import LeafNode
from delimiter import split_nodes_delimiter

class TestDelimiter(unittest.TestCase):
    def test_valid_markdown(self):
        old_nodes = [TextNode("This is **bold** text", TextType.NORMAL)]  # Use NORMAL instead of TEXT
        delimiter = "**"  # The delimiter for bold text
        text_type = TextType.BOLD  # The type for bolded text

        # Expected result after processing
        result = [
            TextNode("This is ", TextType.NORMAL),  # Use NORMAL here as well
            TextNode("bold", TextType.BOLD),
            TextNode(" text", TextType.NORMAL),
        ]
        
        # Call the function and pass all required arguments
        self.assertEqual(split_nodes_delimiter(old_nodes, delimiter, text_type), result)

    def test_extra_delimiter(self):
        old_nodes = [TextNode("This is **bold text and **another bold text**", TextType.NORMAL)]
        delimiter = "**"
        text_type = TextType.BOLD

        # Use assertRaises to expect an exception
        with self.assertRaises(Exception) as context:
            split_nodes_delimiter(old_nodes, delimiter, text_type)
        
        # Optionally, check the exception message (not always required)
        self.assertEqual(str(context.exception), "Extra delimiters detected in the text node")


if __name__ == "__main__":
    unittest.main()