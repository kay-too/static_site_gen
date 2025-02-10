import unittest
from block_to_block import block_to_block_type

class TestMarkdownParser(unittest.TestCase):
    def test_heading(self):
        # Test valid headings
        self.assertEqual(block_to_block_type("# Heading 1"), "heading")
        self.assertEqual(block_to_block_type("### Heading 3"), "heading")
        # Test invalid headings
        self.assertEqual(block_to_block_type("#No space"), "paragraph")
        self.assertEqual(block_to_block_type("####### Too many"), "paragraph")

    def test_code(self):
        self.assertEqual(block_to_block_type("```\ncode block\n```"), "code")
        self.assertEqual(block_to_block_type("```\nmulti\nline\ncode\n```"), "code")
        
    def test_quote(self):
        self.assertEqual(block_to_block_type("> Single quote"), "quote")
        self.assertEqual(block_to_block_type("> Line 1\n> Line 2"), "quote")
        # Test invalid quote
        self.assertEqual(block_to_block_type("> Line 1\nLine 2"), "paragraph")


if __name__ == "__main__":
    unittest.main()