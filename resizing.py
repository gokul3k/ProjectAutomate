from PIL import Image
import os


def editType():
    editType = input("Enter type of resizing Static(1) or Dynamic(2) or QuickResize(3): ")
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


print("Resizing is now completed successfully!")
