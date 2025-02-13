import time
from PIL import ImageGrab, ImageChops
import os
import keyboard
import threading
from datetime import datetime

# Variable global para controlar el estado de pausa
pausado = False

def capturar_pantalla(directorio, intervalo=1):
    global pausado

    # Crear el directorio si no existe
    if not os.path.exists(directorio):
        os.makedirs(directorio)

    contador = 1
    ultima_captura = None

    while True:
        # Si está pausado, esperar un poco y continuar
        if pausado:
            time.sleep(0.1)
            continue

        # Capturar la pantalla
        captura = ImageGrab.grab()

        # Comparar con la última captura guardada
        if ultima_captura is not None:
            diferencia = ImageChops.difference(captura, ultima_captura)
            if not diferencia.getbbox():  # Si no hay diferencia
                print("La pantalla no ha cambiado. No se guarda la captura.")
                time.sleep(intervalo)
                continue

        # Guardar la imagen en el directorio especificado
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

        nombre_archivo = os.path.join(directorio, f"captura_{timestamp}.png")
        captura.save(nombre_archivo)

        print(f"Captura guardada como {nombre_archivo}")

        # Actualizar la última captura
        ultima_captura = captura

        # Incrementar el contador
        contador += 1

        # Esperar el intervalo de tiempo configurado
        time.sleep(intervalo)

def manejar_teclas():
    global pausado

    print("Presiona 'P' para pausar y 'R' para reanudar.")
    while True:
        # Verificar si se presionó la tecla 'P' para pausar
        if keyboard.is_pressed('p'):
            pausado = True
            print("Captura pausada. Presiona 'R' para reanudar.")
            time.sleep(0.5)  # Evitar múltiples detecciones

        # Verificar si se presionó la tecla 'R' para reanudar
        if keyboard.is_pressed('r'):
            pausado = False
            print("Captura reanudada.")
            time.sleep(0.5)  # Evitar múltiples detecciones

        # Esperar un poco para evitar uso excesivo de CPU
        time.sleep(0.1)

if __name__ == "__main__":
    # Directorio donde se guardarán las capturas
    directorio_capturas = "capturas_pantalla"

    # Intervalo de tiempo en segundos (configurable)
    intervalo_tiempo = 1  # 1 segundo

    # Crear un hilo para manejar las teclas
    hilo_teclas = threading.Thread(target=manejar_teclas)
    hilo_teclas.daemon = True  # El hilo se detendrá cuando el programa principal termine
    hilo_teclas.start()

    # Iniciar la captura de pantalla en el hilo principal
    try:
        capturar_pantalla(directorio_capturas, intervalo_tiempo)
    except KeyboardInterrupt:
        print("Captura de pantalla detenida.")