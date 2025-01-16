import unittest

from textnode import TextNode, TextType
from textnode_utils import *

class TestTextNodeUtils(unittest.TestCase):
    def test_italic_delimiter(self):
        node = TextNode("This is *italic* text", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)
        expected = [
            TextNode("This is", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode("text", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected)

    def test_bold_delimiter(self):
        node = TextNode("This is **bold** text", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected = [
            TextNode("This is", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode("text", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected)

    def test_code_delimiter(self):
        node = TextNode("This is `code` text", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [
            TextNode("This is", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode("text", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected)

    def test_no_delimiters(self):
        node = TextNode("This has no special formatting", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)
        self.assertEqual(new_nodes, [node])

    def test_empty_text(self):
        node = TextNode("", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)
        self.assertEqual(new_nodes, [node])
    
    def test_extract_markdown_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        expected = [
            ("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
            ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg"),
        ]
        result = extract_markdown_images(text)
        self.assertEqual(result, expected)

    def test_extract_markdown_images_no_images(self):
        text = "This is text without any images."
        expected = []
        result = extract_markdown_images(text)
        self.assertEqual(result, expected)

    def test_extract_markdown_links(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        expected = [
            ("to boot dev", "https://www.boot.dev"), 
            ("to youtube", "https://www.youtube.com/@bootdotdev")
        ]
        result = extract_markdown_links(text)
        self.assertEqual(result, expected)

    def test_extract_markdown_links_no_links(self):
        text = "This is text without any links."
        expected = []
        result = extract_markdown_links(text)
        self.assertEqual(result, expected)

    def test_extract_markdown_images_and_links(self):
        text = (
            "Check out this image ![alt text](https://example.com/image.png) "
            "and this link [example](https://example.com)."
        )
        expected_images = [("alt text", "https://example.com/image.png")]
        expected_links = [("example", "https://example.com")]

        result_images = extract_markdown_images(text)
        result_links = extract_markdown_links(text)
        self.assertEqual(result_images, expected_images)
        self.assertEqual(result_links, expected_links)

    def test_split_nodes_link_single_link(self):
        text = "Check out this [awesome site](https://example.com) for more details."
        node = TextNode(text, TextType.TEXT)
        nodes = split_nodes_link([node])
        
        self.assertEqual(len(nodes), 3)
        self.assertEqual(nodes[0].text, "Check out this")
        self.assertEqual(nodes[0].text_type, TextType.TEXT)
        self.assertEqual(nodes[1].text, "awesome site")
        self.assertEqual(nodes[1].text_type, TextType.LINK)
        self.assertEqual(nodes[1].url, "https://example.com")
        self.assertEqual(nodes[2].text, "for more details.")
        self.assertEqual(nodes[2].text_type, TextType.TEXT)

    def test_split_nodes_link_multiple_links(self):
        text = "Visit [boot dev](https://www.boot.dev) and [Google](https://www.google.com)."
        node = TextNode(text, TextType.TEXT)
        nodes = split_nodes_link([node])
        
        self.assertEqual(len(nodes), 5)
        self.assertEqual(nodes[0].text, "Visit")
        self.assertEqual(nodes[0].text_type, TextType.TEXT)
        self.assertEqual(nodes[1].text, "boot dev")
        self.assertEqual(nodes[1].text_type, TextType.LINK)
        self.assertEqual(nodes[1].url, "https://www.boot.dev")
        self.assertEqual(nodes[2].text, "and")
        self.assertEqual(nodes[2].text_type, TextType.TEXT)
        self.assertEqual(nodes[3].text, "Google")
        self.assertEqual(nodes[3].text_type, TextType.LINK)
        self.assertEqual(nodes[3].url, "https://www.google.com")
        self.assertEqual(nodes[4].text, ".")
        self.assertEqual(nodes[4].text_type, TextType.TEXT)

    def test_split_nodes_link_no_links(self):
        text = "This text has no links."
        node = TextNode(text, TextType.TEXT)
        nodes = split_nodes_link([node])
        
        self.assertEqual(len(nodes), 1)
        self.assertEqual(nodes[0].text, text)
        self.assertEqual(nodes[0].text_type, TextType.TEXT)

    def test_split_nodes_image_single_image(self):
        text = "Here is an image: ![boot dev](https://www.boot.dev/logo.png)"
        node = TextNode(text, TextType.TEXT)
        nodes = split_nodes_image([node])

        self.assertEqual(len(nodes), 3)
        self.assertEqual(nodes[0].text, "Here is an image:")
        self.assertEqual(nodes[0].text_type, TextType.TEXT)
        self.assertEqual(nodes[1].text, "boot dev")
        self.assertEqual(nodes[1].text_type, TextType.IMAGE)
        self.assertEqual(nodes[1].url, "https://www.boot.dev/logo.png")
        self.assertEqual(nodes[2].text, ".")
        self.assertEqual(nodes[2].text_type, TextType.TEXT)

    def test_split_nodes_image_multiple_images(self):
        text = "Here are two images: ![image 1](https://example.com/img1.png) and ![image 2](https://example.com/img2.png)."
        node = TextNode(text, TextType.TEXT)
        nodes = split_nodes_image([node])
        print(nodes)
        self.assertEqual(len(nodes), 5)
        self.assertEqual(nodes[0].text, "Here are two images:")
        self.assertEqual(nodes[0].text_type, TextType.TEXT)
        self.assertEqual(nodes[1].text, "image 1")
        self.assertEqual(nodes[1].text_type, TextType.IMAGE)
        self.assertEqual(nodes[1].url, "https://example.com/img1.png")
        self.assertEqual(nodes[2].text, " and ")
        self.assertEqual(nodes[2].text_type, TextType.TEXT)
        self.assertEqual(nodes[3].text, "image 2")
        self.assertEqual(nodes[3].text_type, TextType.IMAGE)
        self.assertEqual(nodes[3].url, "https://example.com/img2.png")
        self.assertEqual(nodes[4].text, ".")
        self.assertEqual(nodes[4].text_type, TextType.TEXT)

    def test_split_nodes_image_no_images(self):
        text = "This text has no images."
        node = TextNode(text, TextType.TEXT)
        nodes = split_nodes_image([node])

        self.assertEqual(len(nodes), 1)
        self.assertEqual(nodes[0].text, text)
        self.assertEqual(nodes[0].text_type, TextType.TEXT)

    def test_split_nodes_with_mixed_links_and_images(self):
        text = "This is a text with a link [to boot dev](https://www.boot.dev) and an image ![boot logo](https://www.boot.dev/logo.png)."
        node = TextNode(text, TextType.TEXT)
        nodes = split_nodes_link([node])
        nodes = split_nodes_image(nodes)

        self.assertEqual(len(nodes), 5)
        self.assertEqual(nodes[0].text, "This is a text with a link")
        self.assertEqual(nodes[0].text_type, TextType.TEXT)
        self.assertEqual(nodes[1].text, "to boot dev")
        self.assertEqual(nodes[1].text_type, TextType.LINK)
        self.assertEqual(nodes[1].url, "https://www.boot.dev")
        self.assertEqual(nodes[2].text, "and an image")
        self.assertEqual(nodes[2].text_type, TextType.TEXT)
        self.assertEqual(nodes[3].text, "boot logo")
        self.assertEqual(nodes[3].text_type, TextType.IMAGE)
        self.assertEqual(nodes[3].url, "https://www.boot.dev/logo.png")
        self.assertEqual(nodes[4].text, ".")
        self.assertEqual(nodes[4].text_type, TextType.TEXT)

if __name__ == "__main__":
    unittest.main()

