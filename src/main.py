import sys
from generate_page import *

def main(): 
    basepath = sys.argv[1] if len(sys.argv) > 1 else "/"

    static_to_docs()
    generate_pages_recursive("content", "template.html", "docs", basepath)

main()