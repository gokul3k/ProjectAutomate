import logging

from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse

from automator.image import ImageResizer, BackgroundEditor
from automator.utils import save_file, unzip_file

app = FastAPI()
logging.basicConfig(level=logging.DEBUG)
# logger = logging.getLogger()
image_resizer = ImageResizer()
background_editor = BackgroundEditor()


@app.post("/api/resize_image")
async def create_file(width: int, height: int, output_type: str = "jpeg",
                     resize_type: str ="static", image_file: UploadFile = File()):

    saved_directory = save_file(image_file) 
    unziped_directory = unzip_file(saved_directory)
    result = image_resizer.run(unziped_directory.name, operation=resize_type, width=width, height=height)
    unziped_directory.cleanup()

    return FileResponse(path=result, media_type="application/x-zip-compressed", filename="test_file_name.zip")

@app.post("/api/edit_background")
async def create_file(operation: str = "remove", image_file: UploadFile = File()):

    saved_directory = save_file(image_file) 
    unziped_directory = unzip_file(saved_directory)
    result = background_editor.run(unziped_directory.name, operation=operation)
    unziped_directory.cleanup()

    return FileResponse(path=result, media_type="application/x-zip-compressed", filename="test_file_name.zip")

