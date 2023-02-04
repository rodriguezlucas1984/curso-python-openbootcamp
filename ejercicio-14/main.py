from tkinter import Tk, ttk, StringVar, Text
# Modulo de control Tex ReadOnly
from readOnlyTex import ReadOnlyTex

# Configuración de Ventana
window = Tk()
window.title("RadioButtons")
window.geometry("400x310")
window.resizable(0, 0)

# Configuración de grid
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=3)

# Label
label_titulo_lista = ttk.Label(
    window, text="TU LENGUAJE FAVORITO:", foreground="blue")
label_titulo_lista.grid(column=0, row=0, sticky='w', columnspan=3, padx=5)

# Variable lenguaje seleccionado
lenguaje = StringVar()

# Descripción del lenguaje seleccionado
text_lenguaje = ReadOnlyTex(window, height=15, width=30,
                            font=('Times New Roman', 10, 'bold'), background='#DAF7A6')
text_lenguaje.grid(column=2, row=1, rowspan=7, sticky='e', padx=10, pady=5)


# Función seleccionar lenguaje


def seleccionarLenguaje():
    descripcion = {'python': '- Interpretado\n- Facil de utilizar\n- Tipado dinamico y fuerte\n- De alto nivel\n- Orientado a objetos,estructurado,multiparadigma',
                   'java': '- Interpretado\n- Facil de utilizar\n- Tipado estatico y fuerte\n- De alto nivel\n- Orientado a objetos, multiparadigma',
                   'c': '- Compilado\n- Tipado estatico y fuerte\n- De nivel medio\n- Estructurado',
                   'c++': '- Compilado\n- Tipado estatico y fuerte\n- De alto nivel\n- Orientado a objetos,estructurado,multiparadigma',
                   'c#': '- Compilado\n- Tipado estatico y fuerte\n- De alto nivel\n- Orientado a objetos,estructurado,multiparadigma',
                   'javascript': '- Interpretado\n- Tipado dinamico y debil\n- De alto nivel\n- Orientado a objetos,estructurado,multiparadigma',
                   'otro': 'Seguro que te gusta programar?'}

    text_lenguaje.set_Text(descripcion[lenguaje.get()])


# Lista de RadioButtons


radio_button_python = ttk.Radiobutton(window,
                                      text="python", variable=lenguaje, value="python", command=seleccionarLenguaje)
radio_button_python.grid(column=1, row=1, padx=5, pady=5, sticky='w')

radio_button_javascript = ttk.Radiobutton(window,
                                          text="javascript", variable=lenguaje, value="javascript", command=seleccionarLenguaje)
radio_button_javascript.grid(column=1, row=2, padx=5, pady=5, sticky='w')

radio_button_cmas = ttk.Radiobutton(window,
                                    text="c++", variable=lenguaje, value="c++", command=seleccionarLenguaje)
radio_button_cmas.grid(column=1, row=3, padx=5, pady=5, sticky='w')

radio_button_csharp = ttk.Radiobutton(window,
                                      text="c#", variable=lenguaje, value="c#", command=seleccionarLenguaje)
radio_button_csharp.grid(column=1, row=4, padx=5, pady=5, sticky='w')

radio_button_c = ttk.Radiobutton(window,
                                 text="c", variable=lenguaje, value="c", command=seleccionarLenguaje)
radio_button_c.grid(column=1, row=5, padx=5, pady=5, sticky='w')

radio_button_java = ttk.Radiobutton(window,
                                    text="java", variable=lenguaje, value="java", command=seleccionarLenguaje)
radio_button_java.grid(column=1, row=6, padx=5, pady=5, sticky='w')

radio_button_otro = ttk.Radiobutton(window,
                                    text="otro", variable=lenguaje, value="otro", command=seleccionarLenguaje)
radio_button_otro.grid(column=1, row=7, padx=5, pady=5, sticky='w')


# Funcion reiniciar radiobuttons
def reiniciar():
    lenguaje.set("")
    text_lenguaje.set_Text("")


# Boton reiniciar
style_button = ttk.Style()
style_button.configure('btnReiniciar.TButton',
                       background='blue')
button_reiniciar = ttk.Button(
    window,  text="REINICIAR", style='btnReiniciar.TButton', command=reiniciar)
button_reiniciar.grid(column=2, row=8, sticky='s', pady=10)


window.mainloop()
