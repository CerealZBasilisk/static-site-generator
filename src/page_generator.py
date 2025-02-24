import os
import shutil
from markdown_to_html import markdown_to_html_node
from extract_markdown import extract_title
from constants import *
from pathlib import Path



    
def generate_pages_recursive(dir_path_content,template_path,dest_dir_path):
    print(dir_path_content)
    relative_part = dir_path_content.replace("content", "", 1) 
    if relative_part.startswith("/"):
        relative_part = relative_part[1:]
    
    public_filepath = os.path.join(dest_dir_path, relative_part)
    print(public_filepath, relative_part)

    if os.path.isfile(dir_path_content):
        file_path = Path(dir_path_content)
        if file_path.suffix == ".md":
            generate_page(dir_path_content, template_path, public_filepath)
            print(f"converted file at {dir_path_content} to html at {public_filepath}")
    
    if os.path.isdir(dir_path_content):
        if not os.path.exists(public_filepath):
            os.mkdir(public_filepath)
        for item in os.listdir(dir_path_content):
            generate_pages_recursive(os.path.join(dir_path_content, item),template_path,dest_dir_path)


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, "r", encoding="utf-8") as file:
        markdown = file.read()

    with open(template_path, "r", encoding="utf-8") as file:
        template = file.read()

    html_node = markdown_to_html_node(markdown)
    content = html_node.to_html()
    title = extract_title(markdown)
    
    html = template.replace(r"{{ Title }}", title[0])
    html = html.replace(r"{{ Content }}", content)
    
    # print(html)
    print("dest path:" + dest_path)
    directory_path = Path(dest_path).parent
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
    filename = Path(from_path).stem
    with open(str(directory_path)+f"/{filename}.html", "w", encoding="utf-8") as file:
        file.writelines(html)

if __name__ == "__main__":
    from_path = os.path.relpath("./content/index.md")
    template_path = os.path.relpath("./template.html")
    dest_path = os.path.relpath("./public/content")
    # generate_page(from_path, template_path, dest_path)
    content_path = os.path.relpath("./content/")
    template_path = os.path.relpath("./template.html")
    dest_dir_path = os.path.relpath("./public/")
    generate_pages_recursive(content_path , template_path, dest_dir_path)