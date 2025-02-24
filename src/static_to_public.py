import os 
import shutil


def static_to_public():
    static_path = os.path.relpath("./static")
    public_path = os.path.relpath("./public")
    if os.path.exists(public_path):
        if os.path.isdir(public_path):
            shutil.rmtree(public_path)
            
        else:
            shutil.remove(public_path)
    os.mkdir(public_path)
    content_copier(static_path)
    
def content_copier(filepath):
    relative_part = filepath.replace("static", "", 1) 
    if relative_part.startswith("/"):
        relative_part = relative_part[1:]
    
    public_filepath = os.path.join("public", relative_part)

    if os.path.isfile(filepath):
        shutil.copy(filepath, public_filepath)
        print(f"Copied file from {filepath} to {public_filepath}")
    
    if os.path.isdir(filepath):
        if not os.path.exists(public_filepath):
            os.mkdir(public_filepath)
        for item in os.listdir(filepath):
            content_copier(os.path.join(filepath, item))
    
    



if __name__ == "__main__":
    static_to_public()