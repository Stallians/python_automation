import os
import shutil

IMAGE_EXTENSIONS = ["jpg", "jpeg", "png"]
PDF_EXTENSIONS = ["pdf"]
DOC_EXTENSIONS = ["doc", "docx"]


files_folders = os.listdir()
files = [f for f in files_folders if not os.path.isdir(f)]

# making the folders
if not os.path.exists("./Images"):
    os.mkdir("Images")
if not os.path.exists("./PDF"):
    os.mkdir("PDF")
if not os.path.exists("./Docs"):
    os.mkdir("Docs")

for f in files:
    if f.split(".")[-1] in IMAGE_EXTENSIONS:
        shutil.move(f, os.path.join("./Images", f))
    elif f.split(".")[-1] in PDF_EXTENSIONS:
        shutil.move(f, os.path.join("./PDF", f))
    elif f.split(".")[-1] in DOC_EXTENSIONS:
        shutil.move(f, os.path.join("./Docs", f))

