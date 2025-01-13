import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):

    def test_create_leafnode(self):
        node = LeafNode("p", "test text")
        
        self.assertEqual(node.tag, "p")
        self.assertEqual(node.value, "test text")

    def test_no_children(self):
        node = LeafNode("p", "test text")
        
        self.assertEqual(node.children, None)
    
    def test_value_provided(self):
        node = LeafNode("p", "test text")

        self.assertEqual(node.value, "test text")

    def test_value_missing(self):
        # Test that the constructor raises a ValueError when None is passed
        with self.assertRaises(ValueError):
            LeafNode(value=None)

    def test_to_html(self):
        # Test that to_html returns the correct output
        leaf1 = LeafNode("p", "This is a paragraph of text.")
        leaf2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})

        text1 = "<p>This is a paragraph of text.</p>"
        text2 = "<a href=\"https://www.google.com\">Click me!</a>"

        res1 = leaf1.to_html()
        res2 = leaf2.to_html()

        self.assertEqual(res1, text1)
        self.assertEqual(res2, text2)


if __name__ == "__main__":
    unittest.main()


