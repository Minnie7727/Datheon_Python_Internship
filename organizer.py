import os
import shutil

def organize_files(directory_path):
    if not os.path.exists(directory_path):
        print("Directory not found!")
        return

    # Extension mapping
    extensions = {
        '.pdf': 'Documents',
        '.docx': 'Documents',
        '.txt': 'Documents',
        '.jpg': 'Images',
        '.png': 'Images',
        '.jpeg': 'Images',
        '.zip': 'Archives',
        '.py': 'Code'
    }

    files_moved = 0
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)
        if os.path.isfile(file_path):
            file_ext = os.path.splitext(filename)[1].lower()
            folder_name = extensions.get(file_ext, 'Other_Files')
            
            folder_path = os.path.join(directory_path, folder_name)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
            
            try:
                shutil.move(file_path, os.path.join(folder_path, filename))
                print(f"Moved: {filename} -> {folder_name}/")
                files_moved += 1
            except Exception as e:
                print(f"Error moving {filename}: {e}")

    print(f"\nCompleted! Total {files_moved} files have been relocated.")

if __name__ == "__main__":
    path = input("Enter the path of the folder to organize: ")
    organize_files(path)