import pyperclip

text = pyperclip.paste()
if text:
    print("Texto copiado del portapapeles:")
    print(text)
else:
    print("El portapapeles está vacío o no contiene texto.")
