import os
import textnode
from static_to_public import static_to_public
from page_generator import generate_pages_recursive

def main():
    static_to_public()
    content_path = os.path.relpath("./content/")
    template_path = os.path.relpath("./template.html")
    dest_dir_path = os.path.relpath("./public/")
    generate_pages_recursive(content_path , template_path, dest_dir_path)





if __name__ == "__main__":
    main()
