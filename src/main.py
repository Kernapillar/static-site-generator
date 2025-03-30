import os
import shutil
from textnode import TextType, TextNode
from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode


def main(): 
    static_to_public()

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
            # print(item)
            item_path = os.path.join(copy_path, item)
            dest_path = os.path.join(target_path, item)
            # print('itemPath = '+ item_path)
            # print('destPath = '+ dest_path)
            if os.path.isfile(item_path):
                # print("found an item" + item)
                shutil.copy(item_path, dest_path)
            elif os.path.isdir(item_path): 
                # print("found dir" + item)
                os.mkdir(dest_path)
                new_current_path = os.path.join(current_path, item)
                copy_over(new_current_path)

    copy_over()


main()