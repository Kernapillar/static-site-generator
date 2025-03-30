import os
import shutil
from textnode import *
from htmlnode import *
from leafnode import *
from parentnode import *
from blocks import *


def main(): 
    static_to_public()
    generate_page("content/index.md", "template.html", "public/index.html")

def static_to_public(): 
    # clear public directory: 
    if os.path.exists("./public"):
        shutil.rmtree("./public")
    os.mkdir("./public")

    # recursively copy everything into public: 
    def copy_over(current_path=""): 
        copy_path = os.path.join("static", current_path)
        target_path = os.path.join("public", current_path)
        for item in os.listdir(copy_path): 
            item_path = os.path.join(copy_path, item)
            dest_path = os.path.join(target_path, item)
            if os.path.isfile(item_path):
                shutil.copy(item_path, dest_path)
            elif os.path.isdir(item_path): 
                os.mkdir(dest_path)
                new_current_path = os.path.join(current_path, item)
                copy_over(new_current_path)
    copy_over()


def extract_title(markdown): 
    lines = markdown.split("\n")
    for line in lines: 
        line = line.strip()
        if len(line) > 2 and line[0] == "#" and line[1] != "#": 
            return line[1:].strip()
    raise Exception("No h1 title found")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path) as f, open(template_path) as t, open(dest_path, "w") as output_file:
        markdown = f.read()
        template = t.read()
        markdown_str = markdown_to_html_node(markdown).to_html()
        title = extract_title(markdown)
        # blockquote fix 
        html_output = template.replace('{{ Title }}', title).replace('{{ Content }}', markdown_str).replace("<blockquote> ", "<blockquote>")
        print(html_output)
        output_file.write(html_output)

main()