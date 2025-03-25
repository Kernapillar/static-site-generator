class HTMLNode(): 
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag #string
        self.value = value #string
        self.children = children #list
        self.props = props #dict

    def to_html(self): 
        raise NotImplementedError
    
    def props_to_html(self): 
        prop_list = []
        for key in self.props: 
            prop_list.append(f' {key}="{self.props[key]}"') 
        return "".join(prop_list)
    
    def __repr__(self):
        return f"tag: {self.tag} \n value: {self.value} \n children: {self.children} \n props: {self.props}"

    def __eq__(self, other):
        return (
            self.tag == other.tag
            and self.value == other.value
            and self.children == other.children
            and self.props == other.props
        )