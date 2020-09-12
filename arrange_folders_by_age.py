import csv
import os
import glob

train_path = "./train"
test_path = "./test"

def get_bones_info(is_test=False):

    file_name = "boneage-test-dataset.csv" if is_test else "boneage-training-dataset.csv"

    with open(os.path.dirname(os.path.realpath(__file__)) + '\\' + file_name) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        bones_ages_dict = {}
        bones_is_male_dict = {}
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                bone_id = int(row[0])
                if not is_test:
                    bone_age = int(row[1])
                    is_male = bool(row[2])
                else:
                    bone_age = None
                    is_male = True if str(row[1]) == 'M' else False

                bones_ages_dict[bone_id] = bone_age
                bones_is_male_dict[bone_id] = is_male

    return bones_ages_dict, bones_is_male_dict

def arrange_train_folders():

    im_pth = "./train/"
    bones_ages, bones_is_male = get_bones_info()
    file_ext = ".png"

    image_paths = glob.glob(im_pth + '*' + file_ext)  # returns a list of all the pngs in the folder - not in order
    # Creating a new directory if does not exist

    for im in image_paths:

        image_name = (os.path.basename(im)).split('.')[0]
        image_age = bones_ages[int(image_name)]
        new_dir = os.path.dirname(im_pth + '\\' + str(image_age) + '\\')
        try:
            if not os.path.isdir(new_dir):
                os.makedirs(str(new_dir), 777, exist_ok=True)
        except OSError:
            print("Creation of the directory %s failed" % str(image_age))
        else:
            print("Successfully created the directory %s " % str(image_age))

        os.replace(im,
                   os.path.dirname(str(new_dir) + '\\' + os.path.basename(im) + '\\'))

if __name__ == '__main__':
    arrange_train_folders()
