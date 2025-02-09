import unittest
from mark_to_blocks import markdown_to_blocks

class TestMarkdownToBlocks(unittest.TestCase):
    def test_simple_case(self):
        md = "# Heading\n\nThis is a paragraph.\n\n* Item 1\n* Item 2\n"
        expected = [
            "# Heading",
            "This is a paragraph.",
            "* Item 1 * Item 2"
        ]
        self.assertEqual(markdown_to_blocks(md), expected)

    def test_multiple_blank_lines(self):
        md = "# Heading\n\n\nThis is another paragraph.\n\n\n\n"
        expected = [
            "# Heading",
            "This is another paragraph."
        ]
        self.assertEqual(markdown_to_blocks(md), expected)

    def test_no_blank_lines(self):
        md = "# Heading\nThis is a paragraph.\n* Item\n"
        expected = [
            "# Heading This is a paragraph. * Item"
        ]
        self.assertEqual(markdown_to_blocks(md), expected)

    def test_empty_input(self):
        md = ""
        expected = []
        self.assertEqual(markdown_to_blocks(md), expected)

if __name__ == "__main__":
    unittest.main()