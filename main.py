import os
from exif import Image, DATETIME_STR_FORMAT
from datetime import datetime, date
from pathlib import Path
# import pprint


##################
# Configs
##################
local_directory = "1991-08/"  # Add ending slash
slug = "1991-08 Steve, Dianne, Stuart, Barb Kids, Sue Wedding Prep, "
extension = ".jpg"
datetime_taken = datetime(year=1991, month=8, day=23, hour=1, minute=1, second=1)
datetime_scanned = date.today()

picture_directory = "/Users/wirtes/OneDrive/Pictures/Archive Photo Scans/_Processing/"  # Add ending slash
modified_image_subdirectory = "mods/"


def exif_debugging(photo_image):
    # exif documentation: https://exif.readthedocs.io/en/latest/usage.html
    if photo_image.has_exif:
        status = f"contains EXIF (version {photo_image.exif_version}) information."
    else:
        status = "does not contain any EXIF information."
    print(f"Image {status}")
    image_members = []
    image_members.append(dir(photo_image))
    for element in dir(photo_image):
        print(element)
        value = photo_image.get(element, "Unknown")
        print(value)
        print("-----")


def get_metadata(image_file, working_directory):
    print("Getting EXIF data from " + image_file)
    with open(working_directory + image_file, "rb") as photo:
        photo_image = Image(photo)
        # Uncomment below to print out the EXIF data:
        exif_debugging(photo_image)
    return photo_image


def write_updated_image(original_image, working_directory, modified_image_subdirectory, image_file):
    # Make sure that the mods/ directory exists, if not, create it:
    Path(working_directory + modified_image_subdirectory).mkdir(parents=True, exist_ok=True)
    # Write out the modified image into the mods/ directory
    with open(working_directory + modified_image_subdirectory + image_file, "wb") as photo_write:
        photo_write.write(original_image.get_file())

    return


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    working_directory = picture_directory + local_directory
    dir_list = os.listdir(working_directory)
    dir_list.sort()
    os.chdir(working_directory)
    print("Files and directories in '", working_directory, "' :")
    file_count = 1
    for image_file in dir_list:
        if (image_file.endswith(".JPG") or image_file.endswith(".jpg")) and not image_file.startswith("."):
            new_file_name = slug + str(file_count).zfill(4) + extension
            print(image_file + " becomes " + new_file_name)
            photo_image = get_metadata(image_file, working_directory)
            # Update the EXIF values:
            photo_image.image_description = new_file_name
            photo_image.datetime_original = datetime_taken.strftime(DATETIME_STR_FORMAT)
            photo_image.datetime_digitized = datetime_scanned.strftime(DATETIME_STR_FORMAT)
            write_updated_image(photo_image, working_directory, modified_image_subdirectory, image_file)
            # Rename the updated file:
            os.rename(working_directory + modified_image_subdirectory + image_file, working_directory + modified_image_subdirectory + new_file_name)

            file_count = file_count + 1


