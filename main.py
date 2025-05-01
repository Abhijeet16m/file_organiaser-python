import os
import shutil



#getting input
path = input("Enter the path of folder: ")
os.chdir(path)
items = os.listdir()

def get_extension(filename):
    _, extension = os.path.splitext(filename)
    return extension.lower()

file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp",".webp"],
    "Documents": [".pdf", ".docx", ".txt", ".doc", ".xls", ".xlsx", ".ppt", ".pptx"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi"],
    "Music": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Programs": [".py", ".exe", ".bat", ".sh", ".js", ".java", ".cpp", ".c"],
    }




for i in items:
    if os.path.isdir(i):
        continue
    else:
        extension = get_extension(i)
        for j in file_types:
            if extension in file_types[j]:
                if os.path.exists(j):
                    shutil.move(i,os.path.join(os.getcwd(),j))
                    print(f"Moved '{i}' to '{j}' folder.")

                    break
                else:
                    os.makedirs(j, exist_ok=True)
                    shutil.move(i,os.path.join(os.getcwd(),j))
                    print(f"Moved '{i}' to '{j}' folder.")

                    break
        else:
            if os.path.exists("Others"):
                shutil.move(i,os.path.join(os.getcwd(),"Others"))
                print(f"Moved '{i}' to 'Others' folder.")

            else:
                os.makedirs("Others",exist_ok=True)
                shutil.move(i,os.path.join(os.getcwd(),"Others"))
                print(f"Moved '{i}' to 'Others' folder.")


print("Work is done!!")



                    
