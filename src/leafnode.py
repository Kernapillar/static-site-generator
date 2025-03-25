from htmlnode import HTMLNode

class LeafNode(HTMLNode): 
    def __init__(self, tag, value, props=None):
        if value is None: 
            raise ValueError("LeafNode must have a value")
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:   
            raise ValueError("LeafNode must have a value")
        if self.tag is None: 
            return f"{self.value}"
        
        if self.props != None: 
            props = self.props_to_html()
        else: 
            props = ""
        html = f'<{self.tag}{props}>{self.value}</{self.tag}>'
        return html 
