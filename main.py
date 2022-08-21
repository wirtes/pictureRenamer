import os, sys


# Configs
local_directory = "1980/"
slug = "1980 Merrillville Town Board Swearing In, Otis Bowen, Rose Marie Show, Dan Quayle, "
extension = ".jpg"

picture_directory = "/Users/wirtes/OneDrive/Pictures/Archive Photo Scans/_Scans To Process/"

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    working_directory = picture_directory + local_directory
    dir_list = os.listdir(working_directory)
    os.chdir(working_directory)
    print("Files and directories in '", working_directory, "' :")
    file_count = 1


    for image_file in dir_list:
        if image_file.endswith(".JPG"):
            new_file_name = slug + str(file_count).zfill(4) + extension
            print(image_file + " becomes " + new_file_name)
            os.rename(image_file, new_file_name)
            file_count = file_count + 1


