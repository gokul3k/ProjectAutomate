import shutil
from pathlib import Path 
import os
import zipfile
import tempfile



def save_file(uploaded_file):
    tmp_fp = tempfile.NamedTemporaryFile(suffix=".zip")
    tmp_fp.write(uploaded_file.file.read())
    return tmp_fp

def unzip_file(file_location):
    tmp_directory = tempfile.TemporaryDirectory()
    with zipfile.ZipFile(file_location.name) as zip_file:
        zip_file.extractall(tmp_directory.name)
        file_location.close()
        
    return  tmp_directory

def zip_folder(folder_location):
    folder_location = Path(folder_location)    
    return shutil.make_archive("ImageFolder", format="zip", root_dir=folder_location) 
