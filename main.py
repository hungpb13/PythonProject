# File detection = checking if a file exists, what type it is (file or folder)

import os

relative_file_path = "resources/"
absolute_file_path = "C:/Users/Hungpb/PycharmProjects/PythonProject/resources/text.pdf"

if os.path.exists(relative_file_path):
    print(f"The location '{relative_file_path}' exists")

    if os.path.isfile(relative_file_path):
        print("That is a file")
    else:
        print("That is a folder")
else:
    print(f"The location '{relative_file_path}' doesn't exist")

existed = True if os.path.exists(absolute_file_path) else False
print(f"Is '{absolute_file_path}' existed?: {existed}")