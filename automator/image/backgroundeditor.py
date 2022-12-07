from pathlib import Path
import logging
import os

from rembg import remove
from PIL import Image

from automator.utils import zip_folder

class BackgroundEditor():

    def _file_saving(self, new_image, file_path, file_format="JPEG"):
        new_image.save(file_path, file_format, quality=100)
     

    def _remove_background(self, current_image, file_path):
        new_image = remove(current_image)
        self._file_saving( new_image, file_path,  "PNG")

    def _add_background(self, current_image, file_path):
        image = current_image.convert("RGBA")
        image_data = image.getdata()
        new_image_data = []
        for item in image_data:
            if item[0] == 0 and item[1] == 0 and item[2] == 0:
                new_image_data.append((255, 255, 255, 255))
            else:
                new_image_data.append(item)

        image.putdata(new_image_data)
        self._file_saving(image, file_path, "PNG")

    def run(self, tmp_folder_path, operation):
        parent_folder_path = os.getcwd() / Path(tmp_folder_path) #/ os.listdir(tmp_folder_path)[0]
        for image_directory in sorted(os.listdir(parent_folder_path)):
            logging.debug(parent_folder_path) 
            current_directory = Path(parent_folder_path) / image_directory

            for image_name in sorted(os.listdir(current_directory)):
                if(image_name == ".DS_Store"):
                    continue
                image_path = current_directory / image_name 
                image_data = Image.open(image_path)
                if(operation == "remove"):
                    self._remove_background(image_data, image_path)
                elif(operation == "add"):
                    self._add_background(image_data, image_path)

        zip_folder_name = zip_folder(parent_folder_path)
        return zip_folder_name
        
        