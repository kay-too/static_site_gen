import unittest

from parentnode import ParentNode
from leafnode import LeafNode


class TestParentNode(unittest.TestCase):
    def test_parents_with_props_og(self):
        node = ParentNode("div", [LeafNode(None, "A test string")])
        expected = "<div>A test string</div>"
        self.assertEqual(node.to_html(), expected) 

    def test_multiple_children(self):
        node = ParentNode("div", [
        LeafNode(None, "First"),
        LeafNode(None, "Second")
        ])
        expected = "<div>FirstSecond</div>"
        self.assertEqual(node.to_html(), expected)

    def test_parent_with_props(self):
        node = ParentNode("div", [LeafNode(None, "Hello")], {"class": "greeting"})
        expected = '<div class="greeting">Hello</div>'
        self.assertEqual(node.to_html(), expected)

    def test_nested_parents(self):
        node = ParentNode("div", [
        ParentNode("p", [
            LeafNode(None, "Hello")
        ])
        ])
        expected = "<div><p>Hello</p></div>"
        self.assertEqual(node.to_html(), expected)

    def test_no_tag_error(self):
        with self.assertRaises(ValueError):
            ParentNode(None, [LeafNode(None, "Hello")]).to_html()

    def test_mixed_nodes(self):
        node = ParentNode("p", [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
        ])
        expected = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        self.assertEqual(node.to_html(), expected)

    def test_value_error(self):
        with self.assertRaises(ValueError):
            ParentNode("p", None).to_html()


if __name__ == "__main__":
    unittest.main()