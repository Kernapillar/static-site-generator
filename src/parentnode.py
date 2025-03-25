from htmlnode import HTMLNode

class ParentNode(HTMLNode): 
    def __init__(self, tag, children, props=None):
        if tag is None: 
            raise ValueError("ParentNode must have a tag")
        if children is None: 
            raise ValueError("ParentNode must have children")
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None: 
            raise ValueError("ParentNode must have a tag")
        if self.children is None: 
            raise ValueError("ParentNode must have children")
        if self.props != None: 
            props = self.props_to_html()
        else: 
            props = ""
        children_html = ""
        for child in self.children: 
            children_html += child.to_html()
        html = f'<{self.tag}{props}>{children_html}</{self.tag}>'
        return html 
