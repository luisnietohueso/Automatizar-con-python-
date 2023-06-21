'''
Descripción del proyecto: En este proyecto crearemos un archivo de audio basado en un PDF utilizando las siguientes bibliotecas de Python: pyttsx3. También utilizaremos PyPDF2. Para instalar una biblioteca, deberás usar el comando "pip install nombre_de_librería".

Autor de este codigo: Luis Nieto Hueso

Referencias usadas en el: geeksforgeeks
'''
# Importando los módulos
import PyPDF2
import pyttsx3

# Ruta del archivo PDF
ruta = open('ejemplo.pdf', 'rb')

# Creando un objeto PdfReader
pdfReader = PyPDF2.PdfReader(ruta)

# La página desde la cual deseas empezar
# Esto leerá la página 1 del PDF.
pagina = pdfReader.pages[0]

# Extrayendo el texto del PDF
texto = pagina.extract_text()

# Leyendo el texto
speak = pyttsx3.init()
speak.say(texto)
speak.runAndWait()
