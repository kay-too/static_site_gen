import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_props_to_html(self):
        node1 = LeafNode("p", "This is a paragraph of text.")
        expected = "<p>This is a paragraph of text.</p>"
        self.assertEqual(node1.to_html(), expected) 


        node2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        expected2 = '<a href="https://www.google.com">Click me!</a>'
        self.assertEqual(node2.to_html(), expected2) 

        node3 = LeafNode(None, "Just some text")
        expected3 = "Just some text"
        self.assertEqual(node3.to_html(), expected3) 

    def test_value_error(self):
        with self.assertRaises(ValueError):
            LeafNode("p", None).to_html()


if __name__ == "__main__":
    unittest.main()