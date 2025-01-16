
from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag = None, value = None, props = None):
        if value is None:
            raise ValueError("value is required")

        super().__init__(tag, value, None, props)
    
    # renders a leaf node as an HTML string
    def to_html(self) -> str:
        if self.value is None:
            raise ValueError
        elif not self.tag:
            return self.value
        else:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
