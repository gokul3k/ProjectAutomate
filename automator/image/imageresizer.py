from pathlib import Path
import logging
import os

from PIL import Image

from automator.utils import zip_folder

logging.basicConfig(level=logging.DEBUG)

class ImageResizer():
    
    def _file_saving(self, new_image, file_path):
        new_image.save(file_path, 'PNG', quality=100)
        # return file_path 

    def _static_resize(self, current_image, width, height, x):
        new_image = current_image.resize((width, height), Image.Resampling.LANCZOS)
        return self._file_saving(new_image, x)

    def _dynamic_resize(self, current_image, base_width, x):
        wpercent = (base_width / float(current_image.size[0]))
        hsize = int((float(current_image.size[1]) * float(wpercent)))
        new_image = current_image.resize((base_width, hsize), Image.Resampling.LANCZOS)  
        return self._file_saving(new_image, x)


    def run(self, tmp_folder_path, operation, width, height=None):
        parent_folder_path = os.getcwd() / Path(tmp_folder_path) # os.listdir(tmp_folder_path)[0]
        for image_directory in sorted(os.listdir(parent_folder_path)):
            current_directory = Path(parent_folder_path) / image_directory

            for image_name in sorted(os.listdir(current_directory)):
                if(image_name == ".DS_Store"):
                    continue
                image_path = current_directory / image_name
                image_data = Image.open(os.path.expanduser(image_path))
                if(operation == "static"):
                    self._static_resize(image_data, width, height, image_path) 
                elif(operation == "dynamic"):
                    self._dynamic_resize(image_data, width, image_path) 
            

        zip_folder_name = zip_folder(parent_folder_path)
        return zip_folder_name
 
if __name__=="__main__":
    image_resizer = ImageResizer()
    images = ["../../ImageTestingFolder/EN-YP-YB005-GR/EN-YP-YB005-GR-11.jpg"]



