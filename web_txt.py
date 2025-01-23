#!/usr/bin/env python3
# 
"""
Captura el texto de cualquier página web. Ctrl+A + Ctrl+C (para copiar),
El texto se guarda automáticamente en un archivo de texto (.txt) 

Lo use para ofertas de trabajo en LinkedIn

Características:
- Detecta automáticamente el texto copiado al portapapeles.
- Crea archivos de texto para cada captura.
- Aún averiguando como activar con una combinación única
- Ponerle marca de tiempo para seguimiento
"""

import keyboard
import pyperclip
# import os
import time
from datetime import datetime

# --------------------------------------
# Graba la captura en un archivo nuevo
# --------------------------------------
def save_text_to_file(text):
    """
    Guarda el texto copiado en un archivo de texto / con una marca de tiempo.
    """
    try:
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f"captura_{timestamp}.txt"
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(text)
        print(f"Texto guardado en {filename}")
    except Exception as e:
        print(f"Error al guardar el archivo: {e}")

# --------------------------------------
# Bloque principal
# --------------------------------------
def main():
    """
    Configura el programa para escuchar la combinación de teclas.
    """
    print("Presiona Ctrl+Alt+C para copiar todo el texto visible de la página web.")
    print("El programa guardará el texto copiado automáticamente.")
    
    # Mantener un registro del contenido previo del portapapeles
    previous_text = ""

    while True:
        try:
            # Detectar la combinación de teclas
            # if keyboard.is_pressed('ctrl+1'): # and keyboard.is_pressed('ctrl+c'):
            # if keyboard.is_pressed('ctrl+a') and keyboard.is_pressed('ctrl+c'):       
            if keyboard.is_pressed('ctrl+c'):   
                print("Combinación de teclas OK.")

                # Esperar un pequeño intervalo para que el portapapeles se actualice
                time.sleep(0.2)  # 200 milisegundos
                
                # Leer el contenido de clip
                current_text = pyperclip.paste()
                
                # Verificar si el texto es nuevo
                if current_text != previous_text and current_text.strip():
                    # Contar el número de líneas del texto capturado
                    line_count = len(current_text.splitlines())
                    print(f"Líneas capturadas: {line_count}")
                    save_text_to_file(current_text)
                    previous_text = current_text
                else:
                    print("No se detectaron cambios en el portapapeles.")
                
                # Esperar el ctrl-a para reiniciar
                keyboard.wait('ctrl+a')  # Espera para soltar las teclas
                print("OK")
        except KeyboardInterrupt:
            print("Programa terminado.")
            break

if __name__ == "__main__":
    main()
