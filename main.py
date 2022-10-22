import os
import shutil

import emoji
from cli_color_py import red, bold, green

PROJECT_PATH = os.path.dirname(__file__)
EXAMPLE_PATH = os.path.join(PROJECT_PATH, 'example')

for archive in os.listdir(EXAMPLE_PATH):
    # print(archives)
    # shutil.copyfile(os.path.join(EXAMPLE_PATH, '.gitignore'), '.gitignore')
    path_file = os.path.join(EXAMPLE_PATH, archive)

    if os.path.isdir(path_file):
        try:
            # shutil.copytree(path_file, archive)
            print(emoji.emojize(':pulgar_hacia_arriba:', language='es'))
        except FileExistsError as error:
            print(red("The following directory already exists in the project: {}".format(bold(archive))))
    elif os.path.isfile(path_file):
        print("is a file")
    else:
        print(red("El archivo "))
