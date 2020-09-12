from PIL import Image, ImageOps
import pathlib
import glob
import os

desired_size = 256
home_path = str(pathlib.Path.home())
im_pth = home_path + "/dl-proj/boneage-dataset/boneage-training-dataset/boneage-training-dataset/"
im_resized_pth = home_path + "/dl-proj/boneage-dataset/boneage-training-dataset/boneage-training-dataset-preprocessed/"
file_ext =".png"

#Creating a new directory if does not exist
try:
    if not os.path.isdir(im_resized_pth):
        os.makedirs(im_resized_pth, 777, exist_ok=True)
except OSError:
    print ("Creation of the directory %s failed" % im_resized_pth)
else:
    print ("Successfully created the directory %s " % im_resized_pth)

test_filelist = glob.glob(im_pth + '*' + file_ext) # returns a list of all the pngs in the folder - not in order

for i in range(len(test_filelist)):
    im = Image.open(test_filelist[i])
    filename = test_filelist[i].split('\\')[-1]
    old_size = im.size  # old_size[0] is in (width, height) format

    ratio = float(desired_size)/max(old_size)
    new_size = tuple([int(x*ratio) for x in old_size])
    # use thumbnail() or resize() method to resize the input image

    # thumbnail is a in-place operation

    # im.thumbnail(new_size, Image.ANTIALIAS)

    im = im.resize(new_size, Image.ANTIALIAS)
    # create a new image and paste the resized on it

    new_im = Image.new("L", (desired_size, desired_size))
    new_im.paste(im, ((desired_size-new_size[0])//2,
                        (desired_size-new_size[1])//2))

    new_im.save(os.path.join(im_resized_pth, filename), "PNG")
#new_im.show()
