import os
import shutil
from textnode import *
from htmlnode import *
from leafnode import *
from parentnode import *
from blocks import *

def static_to_docs(): 
    # clear docs directory: 
    if os.path.exists("./docs"):
        shutil.rmtree("./docs")
    os.mkdir("./docs")

    # recursively copy everything into docs: 
    def copy_over(current_path=""): 
        copy_path = os.path.join("static", current_path)
        target_path = os.path.join("docs", current_path)
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

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    dirs = dest_path.replace("/index.html", "")
    if not os.path.exists(dirs): 
        os.makedirs(dirs)
    with open(from_path) as f, open(template_path) as t, open(dest_path, "w") as output_file:
        markdown = f.read()
        template = t.read()
        markdown_str = markdown_to_html_node(markdown).to_html()
        title = extract_title(markdown)
        html_output = template.replace('{{ Title }}', title).replace('{{ Content }}', markdown_str)
        final_html_output = html_output.replace('href="/', f'href="{basepath}').replace('src="/',f'src="{basepath}')
        output_file.write(final_html_output)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    for item in os.listdir(dir_path_content): 
        content_path = os.path.join(dir_path_content, item)
        dest_path = os.path.join(dest_dir_path, item)
        if os.path.isfile(content_path) and item[-3:] == ".md":
            generate_page(content_path, template_path, dest_path.replace(".md", ".html"), basepath)
        elif os.path.isdir(content_path): 
            generate_pages_recursive(content_path, template_path, dest_path, basepath)