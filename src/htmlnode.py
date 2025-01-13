class HTMLNode():
    def __init__(self, tag: str = None, value: str = None, children: list = None, props: dict = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        html_str = ""
        for k, v in self.props.items():
            html_str += f" {k}=\"{v}\""

        return html_str

    def __repr__(self):
        return (
            f"HTMLNode("
            f"{self.tag if self.tag != None else ''}\n,"
            f"{self.value if self.value != None else ''}\n," 
            f"{', '.join(str(child) for child in self.children)}\n," 
            f"{self.props_to_html(self.props) if self.props != None else ''}\n)"
        )
