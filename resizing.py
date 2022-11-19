from PIL import Image
from rembg import remove
import os


def editType():
    editType = input("Enter type Operation StaticResizing(1) or DynamicResizing(2) or QuickResize(3) or "
                     "BackgroundRemoval(4) or Compress Image (5) or File Format Conversion (6):")
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
    print("Rezized " + x)
    fileSaving(new_image, current_folder, x)


def quickResize(imageURL, current_folder, current_image, newSize):
    basewidth = newSize
    wpercent = (basewidth / float(
        current_image.size[0]))  # Here size[0] refers to image height and if [1], it is width.
    hsize = int((float(current_image.size[1]) * float(wpercent)))
    new_image = current_image.resize((basewidth, hsize),
                                     Image.Resampling.LANCZOS)  # LANCZOS is used to downscale image with high quality.

    fileName = current_folder.split('/')[-1]
    print("Rezized " + fileName)
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
    current_image.save(imageURL + '/' + fileName, optimize=True, quality=70)


def fileFormatConvertor(imageURL, current_folder, current_image, newExtension):

    rgb_im = current_image.convert('RGB')
    fileNameWithExtension = current_folder.split('/')[-1]
    fileName = fileNameWithExtension.split('.')[0]
    rgb_im.save(imageURL + '/' + fileName + '.' + newExtension, optimize=True, quality=70)


eT = editType()

if eT == '1':
    imageURL = input("Copy and paste url of folder containing all the images: ")
    width = int(input("Enter image width(Values in pixels): "))
    height = int(input("Enter image height(Values in pixels): "))
    for dir in os.listdir(imageURL):
        if dir == '.DS_Store':
            continue
        print("on DIR:", dir)
        imageCount = 1
        current_folder = imageURL + '/' + dir
        for x in os.listdir(current_folder):
            if x == '.DS_Store':
                continue
            print(x)
            imageList = current_folder + '/' + x
            current_image = Image.open(imageList)
            staticResize(current_folder, current_image, width, height, x)
        print("Resizing of " + dir + " is complete")

elif eT == '2':
    imageURL = input("Copy and paste url of folder containing all the images: ")
    newSize = int(input("Enter size for the longest side to be changed(Values in pixels): "))
    for dir in os.listdir(imageURL):
        if dir == '.DS_Store':
            continue
        print("on DIR:", dir)
        current_folder = imageURL + '/' + dir
        for x in os.listdir(current_folder):
            if x == '.DS_Store':
                continue
            print(x)
            imageList = current_folder + '/' + x
            current_image = Image.open(imageList)
            dynamicResize(current_folder, current_image, newSize, x)
        print("Resizing of " + dir + " is complete")

elif eT == '3':
    imageURL = input("Copy paste image folder url: ")
    newSize = int(input("Enter size for the longest side to be changed(Values in pixels): "))
    for dir in os.listdir(imageURL):
        if dir == '.DS_Store':
            continue
        print("Resizing File:", dir)
        current_folder = imageURL + '/' + dir
        current_image = Image.open(current_folder)
        quickResize(imageURL, current_folder, current_image, newSize)
elif eT == '4':
    imageURL = input("Copy paste image folder url: ")
    whiteBgAdd = input("Do you need to add white background? yes or no (case-sensitive): ")
    for dir in os.listdir(imageURL):
        if dir == '.DS_Store':
            continue
        current_folder = imageURL + '/' + dir
        current_image = Image.open(current_folder)
        removeBackground(imageURL, current_folder, current_image)
        if whiteBgAdd == 'yes':
            addBackground(imageURL, current_folder, current_image)

elif eT == '5':
    imageURL = input("Copy paste image folder url: ")
    for dir in os.listdir(imageURL):
        if dir == '.DS_Store':
            continue
        current_folder = imageURL + '/' + dir
        current_image = Image.open(current_folder)
        compress_img(imageURL, current_folder, current_image)

elif eT == '6':
    imageURL = input("Copy paste image folder url: ")
    newExtension = input("Choose output extension[jpeg, png, gif, tiff, pdf or WEBP]: ")
    for dir in os.listdir(imageURL):
        if dir == '.DS_Store':
            continue
        current_folder = imageURL + '/' + dir
        current_image = Image.open(current_folder)
        fileFormatConvertor(imageURL, current_folder, current_image, newExtension)


print("Image Processing is completed successfully!")
