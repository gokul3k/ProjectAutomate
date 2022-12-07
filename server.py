import logging

from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware

from automator.image import ImageResizer, BackgroundEditor, FileEditor 
from automator.utils import save_file, unzip_file

origins = ["http://localhost:3000"]
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

logging.basicConfig(level=logging.DEBUG)

image_resizer = ImageResizer()
background_editor = BackgroundEditor()
file_editor = FileEditor()


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

@app.post("/api/file_editor")
async def create_file(operation: str = "convert", format: str = "jpeg", image_file: UploadFile = File()):
    saved_directory = save_file(image_file) 
    unziped_directory = unzip_file(saved_directory)
    result = file_editor.run(unziped_directory.name, operation=operation, format=format)
    unziped_directory.cleanup()

    return FileResponse(path=result, media_type="application/x-zip-compressed", filename="test_file_name.zip")

