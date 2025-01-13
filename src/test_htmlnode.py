import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    
    def test_create_htmlnode(self):
        child1 = HTMLNode("p", "child 1")
        child2 = HTMLNode("p", "child 2")
        props = {
                    "href": "https://www.google.com", 
                    "target": "_blank",
                }

        node = HTMLNode("p", "test value", [child1, child2], props)

        self.assertEqual(node.tag, "p")
        self.assertEqual(node.value, "test value")
        self.assertEqual(node.children, [child1, child2])
        self.assertEqual(node.props, props)
    
    def test_no_children(self):
        node = HTMLNode("p", "test value")
        
        self.assertEqual(node.children, None)

    def test_no_props(self):
        node = HTMLNode("p", "test value")

        self.assertEqual(node.props, None)

    def test_to_html(self):
        node = HTMLNode("p", "test value")

        self.assertRaises(NotImplementedError, node.to_html)

    def test_props_to_html(self):
        props = {
                    "href": "https://www.google.com", 
                    "target": "_blank",
                }
        node = HTMLNode("p", "test value", [], props)

        res = node.props_to_html()

        self.assertEqual(res, ' href="https://www.google.com" target="_blank"')


if __name__ == "__main__":
    unittest.main()
