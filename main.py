import os, sys


# Configs
local_directory = "1975/" # Add edning slash
slug = "1975 Las Vegas April, Barb St. Marys Fall, Thanksgiving and Christmas at Miller School, "
extension = ".jpg"

picture_directory = "/Volumes/USB/DCIM/100MEDIA/" # Add ending slash

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    working_directory = picture_directory + local_directory
    dir_list = os.listdir(working_directory)
    os.chdir(working_directory)
    print("Files and directories in '", working_directory, "' :")
    file_count = 1


    for image_file in dir_list:
        if (image_file.endswith(".JPG") or image_file.endswith(".jpg")) and not image_file.startswith("."):
            new_file_name = slug + str(file_count).zfill(4) + extension
            print(image_file + " becomes " + new_file_name)
            os.rename(image_file, new_file_name)
            file_count = file_count + 1


