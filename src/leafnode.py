from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self,tag,value,props=None):
        super().__init__(tag,value,props=props)

    def to_html(self):
        if self.value == None:
            raise ValueError
        if self.tag == None:
            return self.value
        
        html = f"<{self.tag}"
        html += self.props_to_html()  # Use the parent class's method
        html += f">{self.value}</{self.tag}>"
        
        return html