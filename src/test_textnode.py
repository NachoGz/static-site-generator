import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):

    
    def test_eq(self):
        text = "this is a test text node"
        type = TextType.ITALIC
        url = "https://test.com"

        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_creation(self):
        text = "this is a test text node"
        type = TextType.ITALIC
        url = "https://test.com"

        node = TextNode(text, type, url)
        
        self.assertEqual(node.text, text)
        self.assertEqual(node.text_type, type)
        self.assertEqual(node.url, url)
    
    def test_no_url(self):
        text = "this is a test text node"
        type = TextType.ITALIC
        url = "https://test.com"

        node = TextNode(text, type)
        
        self.assertEqual(node.text, text)
        self.assertEqual(node.text_type, type)
        self.assertEqual(node.url, None)
    
    def test_different_properties(self):
        text = "this is a test text node"
        type = TextType.ITALIC
        url = "https://test.com"

        node = TextNode(text, type)
        node2 = TextNode(text, TextType.BOLD)

        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()
