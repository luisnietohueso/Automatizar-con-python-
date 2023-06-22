import pandas as pd
from tkinter import *
from tkinter import messagebox

# extracción de datos
data = pd.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)


# cómo generar el alfabeto fonético
def generar_fonético():
    palabra = ingresar_palabra.get().upper()

    try:
        lista_salida = [phonetic_dict[letra] for letra in palabra]
    except KeyError as e:
        print(e)  # Imprimir la letra que causó el KeyError
        messagebox.showinfo(title='Oops', message="Solo se pueden usar letras")
        return
    else:
        borrar_resultado.delete("1.0", END)  # Borrar cualquier contenido existente
        borrar_resultado.insert(END, ' '.join(lista_salida))  # Insertar la representación fonética al final


# ---------------------------- CONFIGURACIÓN DE LA INTERFAZ DE USUARIO ------------------------------- #
# Esta es la pantalla principal del programa
ventana = Tk()

ventana.title('Generador de alfabeto fonético')
ventana.config(pady=50, padx=50)

# Estas son todas las etiquetas que necesito para la interfaz
etiqueta_fonético = Label(text='Ingresa una palabra: ')
etiqueta_fonético.grid(row=1, column=0)

# Estas son las entradas que necesito para el programa

ingresar_palabra = Entry(width=35)
ingresar_palabra.grid(row=1, column=1, columnspan=2)
ingresar_palabra.focus()

borrar_resultado = Text(height=5, width=30)
borrar_resultado.grid(row=3, column=2, padx=0, pady=0)

# Estos son los botones que necesitaré para el programa

boton_enviar = Button(text='Enviar', command=generar_fonético)
boton_enviar.grid(row=4, column=2, padx=0, pady=0)

ventana.mainloop()
