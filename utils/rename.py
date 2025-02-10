import os
import sys

def rename_images(directory: str, prefix: str, offset: int):
    if not os.path.isdir(directory):
        print(f"El directorio '{directory}' no existe.")
        return
    
    images = [f for f in os.listdir(directory) if f.lower().endswith(('jpg', 'jpeg', 'png', 'gif', 'bmp', 'tiff'))]
    images.sort()
    
    for index, image in enumerate(images, start=offset):
        ext = os.path.splitext(image)[1]
        new_name = f"{prefix}{index}{ext}"
        old_path = os.path.join(directory, image)
        new_path = os.path.join(directory, new_name)
        os.rename(old_path, new_path)
        print(f"Renombrado: {image} -> {new_name}")

if __name__ == "__main__":
    directorio = os.path.dirname(os.path.abspath(__file__))  # Usa el mismo directorio del script
    prefijo = sys.argv[1] if len(sys.argv) > 1 else "imagen_"  # Obtiene el prefijo de los argumentos o usa el predeterminado
    offset = int(sys.argv[2]) if len(sys.argv) > 2 else 1  # Obtiene el offset del argumento o usa 1 por defecto
    rename_images(directorio, prefijo, offset)
