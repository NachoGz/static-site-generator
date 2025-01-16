import unittest

from parentnode import ParentNode
from leafnode import LeafNode


class TestParentNode(unittest.TestCase):
    def test_to_html(self):
        """Test ParentNode with multiple LeafNode children."""
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        expected = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        result = node.to_html()
        self.assertEqual(expected, result)

    def test_to_html_with_props(self):
        """Test ParentNode with properties and LeafNode children."""
        node = ParentNode(
            "div",
            [
                LeafNode("span", "Hello", {"class": "highlight"}),
                LeafNode("a", "Click here", {"href": "https://example.com"}),
            ],
            {"class": "container"}
        )
        expected = (
            '<div class="container">'
            '<span class="highlight">Hello</span>'
            '<a href="https://example.com">Click here</a>'
            '</div>'
        )
        result = node.to_html()
        self.assertEqual(expected, result)

    def test_nested_parent_nodes(self):
        """Test nested ParentNode structures."""
        node = ParentNode(
            "div",
            [
                ParentNode(
                    "ul",
                    [
                        LeafNode("li", "Item 1"),
                        LeafNode("li", "Item 2"),
                    ]
                ),
                LeafNode("p", "A paragraph."),
            ],
        )
        expected = (
            "<div>"
            "<ul>"
            "<li>Item 1</li>"
            "<li>Item 2</li>"
            "</ul>"
            "<p>A paragraph.</p>"
            "</div>"
        )
        result = node.to_html()
        self.assertEqual(expected, result)

    def test_missing_tag_raises_error(self):
        """Test that missing tag in ParentNode raises ValueError."""
        with self.assertRaises(ValueError):
            ParentNode(None, [LeafNode("b", "Bold text")])

    def test_missing_children_raises_error(self):
        """Test that missing children in ParentNode raises ValueError."""
        with self.assertRaises(ValueError):
            ParentNode("div", None)

    def test_empty_children(self):
        """Test ParentNode with an empty list of children."""
        with self.assertRaises(ValueError):
            node = ParentNode("div", [])



if __name__ == "__main__":
    unittest.main()
