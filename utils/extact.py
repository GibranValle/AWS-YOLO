import os
import re

def extract_image_names(directory: str):
    if not os.path.isdir(directory):
        print(f"El directorio '{directory}' no existe.")
        return set()
    
    images = [f for f in os.listdir(directory) if f.lower().endswith(('jpg', 'jpeg', 'png', 'gif', 'bmp', 'tiff'))]
    name_set = set()
    
    for image in images:
        name_without_index = re.sub(r"\d+$", "", os.path.splitext(image)[0])
        name_set.add(name_without_index)
    
    return name_set

if __name__ == "__main__":
    parent_directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Obtiene el directorio padre
    directorio = os.path.join(parent_directory, "datasets", "images", "train")  # Construye la ruta deseada
    nombres = extract_image_names(directorio)
    print("Nombres de imágenes sin índice:", nombres)
