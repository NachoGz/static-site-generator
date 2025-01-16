from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag: str = None, children: list = None, props: dict = None):
        if not tag:
            raise ValueError("tag is required")
        if not children or children == []:
            raise ValueError("children is required")

        super().__init__(tag, None, children, props)

    def to_html(self):
        html_str = f"<{self.tag}{self.props_to_html()}>"
        for child in self.children:
            html_str += child.to_html()
        
        return html_str + f"</{self.tag}>"

        
