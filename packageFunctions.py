from rembg import remove
from PIL import Image
import os


def editType():
    editType = input("Enter type Operation StaticResizing(1) or DynamicResizing(2) or QuickResize(3) or "
                     "BackgroundRemoval(4) or Compress Image (5) or File Format Conversion (6) or file renaming (7):")
    return editType


def staticResize(current_folder, current_image, width, height, x):
    new_image = current_image.resize((width, height), Image.Resampling.LANCZOS)
    fileSaving(new_image, current_folder, x)


def dynamicResize(current_folder, current_image, newSize, x):
    basewidth = newSize
    wpercent = (basewidth / float(
        current_image.size[0]))  # Here size[0] refers to image height and if [1], it is width.
    hsize = int((float(current_image.size[1]) * float(wpercent)))
    new_image = current_image.resize((basewidth, hsize),
                                     Image.Resampling.LANCZOS)  # LANCZOS is used to downscale image with high quality.
    fileSaving(new_image, current_folder, x)


def quickResize(imageURL, current_folder, current_image, newSize):
    basewidth = newSize
    wpercent = (basewidth / float(
        current_image.size[0]))  # Here size[0] refers to image height and if [1], it is width.
    hsize = int((float(current_image.size[1]) * float(wpercent)))
    new_image = current_image.resize((basewidth, hsize),
                                     Image.Resampling.LANCZOS)  # LANCZOS is used to downscale image with high quality.

    fileName = current_folder.split('/')[-1]
    new_image.save(imageURL + '/' + fileName, 'JPEG', quality=100)


def fileSaving(new_image, current_folder, x):
    new_image.save(current_folder + '/' + x, 'JPEG', quality=100)


def removeBackground(imageURL, current_folder, current_image):
    new_image = remove(current_image)
    fileName = current_folder.split('/')[-1]
    print("Removed Background of: " + fileName)
    new_image.save(imageURL + '/' + fileName, 'PNG', quality=100)


def addBackground(imageURL, current_folder, current_image):
    img = current_image.convert("RGBA")
    datas = img.getdata()
    newData = []
    for item in datas:
        if item[0] == 0 and item[1] == 0 and item[2] == 0:
            newData.append((255, 255, 255, 255))
        else:
            newData.append(item)

    img.putdata(newData)
    fileName = current_folder.split('/')[-1]
    print("Added white background: " + fileName)
    img.save(imageURL + '/' + fileName, 'PNG', quality=100)


def compress_img(imageURL, current_folder, current_image):
    fileName = current_folder.split('/')[-1]
    rgb_im = current_image.convert('RGB')
    rgb_im.save(imageURL + '/' + fileName, optimize=True, quality=70)
    print("Compressed: ", fileName)


def fileFormatConvertor(imageURL, current_folder, current_image, extension):
    rgb_im = current_image.convert('RGB')
    fileNameWithExtension = current_folder.split('/')[-1]
    fileName = fileNameWithExtension.split('.')[0]
    rgb_im.save(imageURL + '/' + fileName + '.' + extension, optimize=True, quality=70)
    print("File Format changed: " + fileName + '.' + extension)
    os.remove(current_folder)


def fileRenaming(imageList, current_folder, current_image, fileCount):
    f, e = os.path.splitext(imageList)
    fileName = current_folder.split('/')[-1]
    rgb_im = current_image.convert('RGB')
    rgb_im.save(current_folder + '/' + fileName + '-' + str(fileCount) + e, optimize=True, quality=100)
    os.remove(imageList)
