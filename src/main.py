from generate_page import *

def main(): 
    static_to_public()
    generate_page("content/index.md", "template.html", "public/index.html")


main()