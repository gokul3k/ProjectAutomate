import packageFunctions
from PIL import Image
import os

eT = packageFunctions.editType()

if eT == '1':
    imageURL = input("Copy and paste url of folder containing all the images: ")
    width = int(input("Enter image width(Values in pixels): "))
    height = int(input("Enter image height(Values in pixels): "))
    for dir in sorted(os.listdir(imageURL)):
        if dir == '.DS_Store':
            continue
        print("on DIR:", dir)
        imageCount = 1
        current_folder = imageURL + '/' + dir
        for x in sorted(os.listdir(current_folder)):
            if x == '.DS_Store':
                continue
            print("resizing: ",x)
            imageList = current_folder + '/' + x
            current_image = Image.open(imageList)
            packageFunctions.staticResize(current_folder, current_image, width, height, x)
        print("Resizing of " + dir + " is complete")

elif eT == '2':
    imageURL = input("Copy and paste url of folder containing all the images: ")
    newSize = int(input("Enter size for the longest side to be changed(Values in pixels): "))
    for dir in sorted(os.listdir(imageURL)):
        if dir == '.DS_Store':
            continue
        print("on DIR:", dir)
        current_folder = imageURL + '/' + dir
        for x in sorted(os.listdir(current_folder)):
            if x == '.DS_Store':
                continue
            print("resizing: ",x)
            imageList = current_folder + '/' + x
            current_image = Image.open(imageList)
            packageFunctions.dynamicResize(current_folder, current_image, newSize, x)
        print("Resizing of " + dir + " is complete")

elif eT == '3':
    imageURL = input("Copy paste image folder url: ")
    newSize = int(input("Enter size for the longest side to be changed(Values in pixels): "))
    for dir in sorted(os.listdir(imageURL)):
        if dir == '.DS_Store':
            continue
        print("Resizing File:", dir)
        current_folder = imageURL + '/' + dir
        current_image = Image.open(current_folder)
        packageFunctions.quickResize(imageURL, current_folder, current_image, newSize)

elif eT == '4':
    imageURL = input("Copy paste image folder url: ")
    whiteBgAdd = input("Do you need to add white background? yes or no (Case-Sensitive!): ")
    for dir in sorted(os.listdir(imageURL)):
        if dir == '.DS_Store':
            continue
        current_folder = imageURL + '/' + dir
        current_image = Image.open(current_folder)
        packageFunctions.removeBackground(imageURL, current_folder, current_image)
        if whiteBgAdd == 'yes':
            packageFunctions.addBackground(imageURL, current_folder, current_image)

elif eT == '5':
    print("Compression of jpeg image files is recommended for better compression results")
    imageURL = input("Copy paste image folder url: ")
    for dir in sorted(os.listdir(imageURL)):
        if dir == '.DS_Store':
            continue
        current_folder = imageURL + '/' + dir
        try:
            current_image = Image.open(current_folder)
            packageFunctions.compress_img(imageURL, current_folder, current_image)
        except:
            print("Image might be corrupted. Check your files")

elif eT == '6':
    imageURL = input("Copy paste image folder url: ")
    extensions = input("Choose output extension [jpeg, jpg, png, gif, tiff, pdf or WEBP]: ")

    for dir in sorted(os.listdir(imageURL)):
        if dir == '.DS_Store':
            continue
        current_folder = imageURL + '/' + dir
        try:
            current_image = Image.open(current_folder)
            packageFunctions.fileFormatConvertor(imageURL, current_folder, current_image, extensions)

        except:
            fileName = current_folder.split('/')[-1]
            print("Error Processing: Check if the image is corrupted or file format is provided correctly in the input: " + fileName)


elif eT == '7':
    imageURL = input("Copy and paste url of folder containing all the images: ")
    for dir in sorted(os.listdir(imageURL)):
        if dir == '.DS_Store':
            continue
        print("on DIR:", dir)
        current_folder = imageURL + '/' + dir
        fileCount = 0
        for x in sorted(os.listdir(current_folder)):
            if x == '.DS_Store':
                continue
            print(x)
            fileCount += 1
            imageList = current_folder + '/' + x
            current_image = Image.open(imageList)
            packageFunctions.fileRenaming(imageList, current_folder, current_image , fileCount)

else:
    print("Please enter only the numeric value specified for each operation. please try again")

print("Image Processing is completed!")
