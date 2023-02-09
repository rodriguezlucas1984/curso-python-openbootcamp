from tkinter import ttk, Tk, BooleanVar, messagebox

from random import randint
from PIL import Image, ImageTk
from urllib.request import urlopen
from io import BytesIO
import ssl


# Configuración de la ventana
window = Tk()
window.title("ELEMENTOS SELECCIONABLES")
window.geometry("470x470")
window.resizable(0, 0)

# Configuración de grid
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=3)


# ComboBox
label_combobox = ttk.Label(window, text="ComboBox ")
label_combobox.grid(column=0, row=0, sticky='w', padx=10)

label_value_combobox = ttk.Label(window, text="")
label_value_combobox.config(width=15)
label_value_combobox.grid(column=2, row=0, sticky="e", padx=20)


def selection_change(event):
    if comboBox.get() != "":
        label_value_combobox.config(background='#56A556')
    else:
        label_value_combobox.config(background='#F1F1F1')
    label_value_combobox.config(text=comboBox.get())


comboBox = ttk.Combobox(
    window, values=["", "Opcion 1", "Opcion 2", "Opcion 3"])
comboBox.grid(row=0, column=1, sticky="w")
comboBox.bind('<<ComboboxSelected>>', selection_change)

# Titulo arbol
label_titulo_tree = ttk.Label(
    window, text="ARBOL DE IMAGENES", justify="center",  font=('Times New Roman', 10, 'bold'), foreground='blue')
label_titulo_tree.grid(column=0, row=1, columnspan=3,  pady=5)

# TreeView
treeview_imagenes = ttk.Treeview(window)
treeview_imagenes.config(height=15)
treeview_imagenes.grid(column=0, row=2, columnspan=2,
                       pady=10, padx=10, sticky='w')

# Items
for i in range(0, 3):
    hijos = randint(1, 4)
    item = treeview_imagenes.insert("", 'end', text=f'Elemento {i+1}')
    while hijos > 0:
        treeview_imagenes.insert(
            item, 0, text=f'Hijo {hijos}', tags=f'https://picsum.photos/id/{randint(10,300)}/200/320')
        hijos -= 1

treeview_imagenes_label = ttk.Label()
treeview_imagenes_label.grid(column=2, row=2, sticky='e', padx=10)

context = ssl._create_unverified_context()

# Funcion que obtiene la imagen al selecccionar un elemento hoja del arbol


def ver(event):
    item = treeview_imagenes.focus()
    if "Hijo" in treeview_imagenes.item(item)["text"]:
        global photo
        URL = treeview_imagenes.item(item)["tags"][0]
        u = urlopen(URL, context=context)
        raw_data = u.read()
        u.close()

        im = Image.open(BytesIO(raw_data))

        photo = ImageTk.PhotoImage(im)
        treeview_imagenes_label.config(image=photo)


treeview_imagenes.bind('<<TreeviewSelect>>', ver)

# Checkbox
checked = BooleanVar(value=False)
checkbutton_condiciones = ttk.Checkbutton(
    window, text="Acepta terminos y condiciones", variable=checked)
checkbutton_condiciones.grid(
    column=0, row=3, sticky="w", padx=10, columnspan=3)


# Boton Aceptar


def click():
    if not checked.get():
        messagebox.showerror(
            message="Es necesario que acepte los terminos y condiciones", title="Terminos y condiciones")
    else:
        messagebox.showinfo(
            message="Gran elección, gracias!!!!", title="Confirmación")


button_aceptar = ttk.Button(
    window, text="Aceptar", command=click, width=10)
button_aceptar.grid(column=2, row=4, sticky='e', pady=15, padx=85)


# Boton Salir
button_salir = ttk.Button(window, text="Salir", command=exit, width=10)
button_salir.grid(column=2, row=4, sticky='e', pady=15, padx=10)


# Hilo de ejecución
window.mainloop()
