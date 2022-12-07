from pathlib import Path
import logging
import os

from PIL import Image

from automator.utils import zip_folder

class FileEditor():

    def _file_saving(self, new_image, file_path, file_format="jpeg", quality=100, optimize=True):
        logging.debug(file_format)
        file_path = file_path.parent / (file_path.stem + "." + file_format) 
        new_image.save(file_path, file_format, quality=quality, optimize=optimize)

    def _convert_format(self, current_image, file_path, file_format):
        rgb_img = current_image.convert('RGB')
        self._file_saving(rgb_img, file_path, quality=70, optimize=True, file_format=file_format)
        os.remove(file_path)

    def _compress_img(self, current_image, file_path):
        rgb_img = current_image.convert("RGB")
        self._file_saving(rgb_img, file_path, quality=70)
        os.remove(file_path)

    def _file_renaming(self, image_list, current_folder, current_image, file_count):
        f, e = os.path.splitext((image_list))
        file_name = current_folder.name
        rgb_img = current_image.convert("RGB")
        final_name = Path(str(current_folder) + '/' + str(file_name) + '-' + str(file_count) + e)

        self._file_saving(rgb_img, final_name, optimize=True)
        os.remove(image_list)


    def run(self, tmp_folder_path, operation, format):
        parent_folder_path = os.getcwd() / Path(tmp_folder_path) 
        for image_directory in sorted(os.listdir(parent_folder_path)):
            logging.debug(parent_folder_path) 
            current_directory = Path(parent_folder_path) / image_directory

            for index, image_name in enumerate(sorted(os.listdir(current_directory))):
                if(image_name == ".DS_Store"):
                    continue
                image_path = current_directory / image_name 
                image_data = Image.open(image_path)
                if(operation == "convert"):
                    self._convert_format(image_data, image_path, format)
                elif(operation == "compress"):
                    self._compress_img(image_data, image_path)
                elif(operation == "rename"):
                    self._file_renaming(image_path, current_directory, image_data, index)

        zip_folder_name = zip_folder(parent_folder_path)
        return zip_folder_name
        
        