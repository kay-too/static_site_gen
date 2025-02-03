from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self,tag,children,props=None):
        super().__init__(tag,None,children,props)

    def to_html(self):
        if self.tag == None:
            raise ValueError
        if self.children == None:
            raise ValueError("Missing children")

        html = f"<{self.tag}"
        html += f"{self.props_to_html()}>"

        for child in self.children:
            html += f"{child.to_html()}"
            
        html += f"</{self.tag}>"

        return html