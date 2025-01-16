from textnode import TextNode, TextType
from leafnode import LeafNode
import unittest


class TestTextNode(unittest.TestCase):

    def test_eq(self):
        text = "this is a test text node"
        type = TextType.BOLD

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

        node = TextNode(text, type)

        self.assertEqual(node.text, text)
        self.assertEqual(node.text_type, type)
        self.assertIsNone(node.url)

    def test_different_properties(self):
        text = "this is a test text node"

        node = TextNode(text, TextType.ITALIC)
        node2 = TextNode(text, TextType.BOLD)

        self.assertNotEqual(node, node2)

    def test_text_node_to_html_node_text(self):
        text = "Plain text"
        node = TextNode(text, TextType.TEXT)
        result = node.text_node_to_html_node()

        expected = LeafNode(None, text)
        self.assertEqual(result.to_html(), expected.to_html())

    def test_text_node_to_html_node_bold(self):
        text = "Bold text"
        node = TextNode(text, TextType.BOLD)
        result = node.text_node_to_html_node()

        expected = LeafNode("b", text)
        self.assertEqual(result.to_html(), expected.to_html())

    def test_text_node_to_html_node_italic(self):
        text = "Italic text"
        node = TextNode(text, TextType.ITALIC)
        result = node.text_node_to_html_node()

        expected = LeafNode("i", text)
        self.assertEqual(result.to_html(), expected.to_html())

    def test_text_node_to_html_node_code(self):
        text = "Code snippet"
        node = TextNode(text, TextType.CODE)
        result = node.text_node_to_html_node()

        expected = LeafNode("c", text)
        self.assertEqual(result.to_html(), expected.to_html())

    def test_text_node_to_html_node_link(self):
        text = "Click me"
        url = "https://example.com"
        node = TextNode(text, TextType.LINK, url)
        result = node.text_node_to_html_node()

        expected = LeafNode("a", text, {"href": url})
        self.assertEqual(result.to_html(), expected.to_html())

    def test_text_node_to_html_node_image(self):
        text = "Image alt text"
        url = "https://example.com/image.png"
        node = TextNode(text, TextType.IMAGE, url)
        result = node.text_node_to_html_node()

        expected = LeafNode("img", "", {"src": url, "alt": text})
        self.assertEqual(result.to_html(), expected.to_html())

    def test_text_node_to_html_node_invalid_type(self):
        text = "Invalid type"
        node = TextNode(text, None)

        with self.assertRaises(ValueError):
            node.text_node_to_html_node()


if __name__ == "__main__":
    unittest.main()

