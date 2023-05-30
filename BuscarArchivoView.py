import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import pandas as pd

def open_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        file_extension = file_path.split(".")[-1]
        if file_extension == "txt":
            with open(file_path, 'r') as file:
                content = file.read()
                text.delete('1.0', tk.END)
                text.insert(tk.END, content)
        elif file_extension == "csv":
            df = pd.read_csv(file_path)
            display_data(df)
        elif file_extension in ["xlsx", "xls"]:
            df = pd.read_excel(file_path)
            display_data(df)

def display_data(df):
    text.delete('1.0', tk.END)
    text.configure(state='normal')
    text.insert(tk.END, df.to_string(index=False))

    # Ajustar el tamaño de las columnas automáticamente
    text.configure(state='disabled')
    text.update_idletasks()  # Actualizar el estado de la interfaz
    for i in range(df.shape[1]):
        text.columnconfigure(i, minsize=20)
        text.columnconfigure(i, weight=1)

    # Habilitar el desplazamiento horizontal
    text.configure(xscrollcommand=scrollbar_horizontal.set)
    scrollbar_horizontal.configure(command=text.xview)
    scrollbar_horizontal.pack(fill=tk.X, side=tk.BOTTOM)

# Crear la ventana principal
window = tk.Tk()
window.title("Visor de Archivos")
window.geometry("800x400")

# Botón para seleccionar archivo
open_button = tk.Button(window, text="Abrir archivo", command=open_file)
open_button.pack(pady=10)

# Área de texto para mostrar el contenido
text_frame = ttk.Frame(window)
text_frame.pack(fill=tk.BOTH, expand=True)

text = tk.Text(text_frame, wrap=tk.NONE)
text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar_vertical = ttk.Scrollbar(text_frame, orient=tk.VERTICAL, command=text.yview)
scrollbar_vertical.pack(side=tk.RIGHT, fill=tk.Y)

scrollbar_horizontal = ttk.Scrollbar(window, orient=tk.HORIZONTAL, command=text.xview)

text.configure(yscrollcommand=scrollbar_vertical.set)

# Ejecutar la aplicación
window.mainloop()
