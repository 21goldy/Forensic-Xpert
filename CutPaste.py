import shutil

def cut_and_paste_file(source_path, destination_path):
    try:
        # Move (cut and paste) the file
        shutil.move(source_path, destination_path)
        print(f"File '{source_path}' successfully moved to '{destination_path}'")
    except Exception as e:
        print(f"Error: {e}") 