import os

from os.path import join, dirname, isdir, abspath


def find_empty_dirs(directory: str):
    if not isdir(directory):
        print(f"El directorio '{directory}' no existe.")
        return []

    empty_folders = []
    for subdirectory in os.listdir(directory):
        subdir = join(directory, subdirectory)
        if not isdir(subdir):
            continue
        if not os.listdir(join(directory, subdirectory)):
            empty_folders.append(subdirectory)
    return empty_folders


if __name__ == "__main__":
    parent_dir = dirname(dirname(abspath(__file__)))  # Obtiene el directorio padre
    model_dir = join(parent_dir, "model")
    print(find_empty_dirs(model_dir))
