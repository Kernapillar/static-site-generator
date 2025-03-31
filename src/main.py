import sys
from generate_page import *

def main(): 
    basepath = sys.argv[0] if sys.argv[0] != "" else "/"

    static_to_docs()
    generate_pages_recursive("content", "template.html", "docs", basepath)



main()