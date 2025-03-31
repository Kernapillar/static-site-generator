from generate_page import *

def main(): 
    static_to_public()
    generate_pages_recursive("content", "template.html", "public")



main()