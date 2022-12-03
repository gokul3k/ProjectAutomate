from pathlib import Path
import logging
import os

from PIL import Image

from automator.utils import zip_folder

class FileEditor():

    def _file_saving(self, new_image, file_path, file_format="JPEG", quality=100, optimze=True):
        new_image.save(file_path, file_format, quality=quality, optimze=optimze)

    def _convert_format(self, current_image, file_path, file_format):
        rgb_img = current_image.convert('RGB')
        self._file_saving(rgb_img, file_path, quality=70, optimze=True, file_format=file_format)

    def _compress_img(self, current_image, file_path):
        rgb_img = current_image.convert("RGB")
        self._file_saving(rgb_img, file_path, quality=70)

    # def _file_renaming(self, )


    def run(self, tmp_folder_path, operation):
        parent_folder_path = os.getcwd() / Path(tmp_folder_path) #/ os.listdir(tmp_folder_path)[0]
        for image_directory in sorted(os.listdir(parent_folder_path)):
            logging.debug(parent_folder_path) 
            current_directory = Path(parent_folder_path) / image_directory

            for image_name in sorted(os.listdir(current_directory)):
                image_path = current_directory / image_name 
                image_data = Image.open(image_path)
                if(operation == "convert"):
                    self._convert_format(image_data, image_path)
                elif(operation == "add"):
                    self._add_background(image_data, image_path)

        zip_folder_name = zip_folder(parent_folder_path)
        return zip_folder_name
        
        