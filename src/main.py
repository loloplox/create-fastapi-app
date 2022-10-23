import os
import shutil

PROJECT_PATH = os.path.dirname(__file__)
MODEL_PATH = os.path.join(PROJECT_PATH, 'model')


def move_archives() -> list:
    archives_name = []

    for archive in os.listdir(MODEL_PATH):
        path_file = os.path.join(MODEL_PATH, archive)

        if os.path.isdir(path_file):
            try:
                shutil.copytree(path_file, archive)
                archives_name.append(f"{archive}")
            except FileExistsError as error:
                archives_name.append(f"{archive}")
        elif os.path.isfile(path_file):
            try:
                shutil.copyfile(path_file, archive)
                archives_name.append(f"{archive}")
            except Exception as error:
                archives_name.append(f"{archive}")
        else:
            print("unknown error")

    return archives_name


def print_name_archive(archives_name: list):
    archives_name_sorts = sort_name_archives(archives_name)
    for name in archives_name_sorts:
        print(name)


def sort_name_archives(name_archives: list) -> list:
    new_list_archives = []
    for archive in name_archives:
        path_file = os.path.join(MODEL_PATH, archive)

        if os.path.isdir(path_file):
            new_list_archives.insert(0, f"📁 {archive}")
        else:
            new_list_archives.append(f"📄 {archive}")

    return new_list_archives


list_archives = move_archives()
print_name_archive(list_archives)
