import unittest
from block_to_html import *

class TestMarkdownParser(unittest.TestCase):
    def test_paragraphs(self):
        html = markdown_to_html_node("This is a paragraph").to_html()
        self.assertEqual(html, "<div><p>This is a paragraph</p></div>")
    
    def test_headings(self):
        html = markdown_to_html_node("# Heading 1").to_html()
        self.assertEqual(html, "<div><h1>Heading 1</h1></div>")
        
        html = markdown_to_html_node("### Heading 3").to_html()
        self.assertEqual(html, "<div><h3>Heading 3</h3></div>")
    
    def test_code_blocks(self):
        html = markdown_to_html_node("```code here```").to_html()
        self.assertEqual(html, "<div><p><code>code here</code></p></div>")
    
    def test_blockquotes(self):
        html = markdown_to_html_node("> quoted text").to_html()
        self.assertEqual(html, "<div><blockquote>quoted text</blockquote></div>")
    
    def test_unordered_lists(self):
        html = markdown_to_html_node("- list item").to_html()
        self.assertEqual(html, "<div><ul><li>list item</li></ul></div>")
    
    def test_ordered_lists(self):
        html = markdown_to_html_node("1. first item").to_html()
        self.assertEqual(html, "<div><ol><li>first item</li></ol></div>")

    def test_markdown_complex_cases(self):
        # Test multiple blocks
        markdown = """# Header

    This is a paragraph.

    > This is a quote"""
        html = markdown_to_html_node(markdown).to_html()
        self.assertEqual(
            html.replace("\n", ""),
            "<div><h1>Header</h1><p>This is a paragraph.</p><blockquote>This is a quote</blockquote></div>"
        )

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