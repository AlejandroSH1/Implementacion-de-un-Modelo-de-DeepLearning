import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import numpy as np
import tensorflow as tf

MODEL_PATH = "Models/modelo2_effnetb0_seed42.keras"
IMG_SIZE = (224, 224)
CLASS_NAMES = ["Audi_R8", "Audi_RS5", "BMW_M3", "BMW_M5", "Chevrolet_Camaro",
               "Ford_Mustang", "Mercedes_AMG_GT", "Nissan_GT_R", "Porsche_911", "Toyota_Supra"]

model = tf.keras.models.load_model(MODEL_PATH, compile=False)

# FUNCIONES
def seleccionar_imagen():
    ruta = filedialog.askopenfilename(
        title="Seleccionar imagen",
        filetypes=[
            ("Imágenes", "*.jpg *.jpeg *.png *.bmp"),
            ("Todos los archivos", "*.*")
        ]
    )

    if not ruta:
        return

    try:
        # Mostrar imagen original
        imagen = Image.open(ruta).convert("RGB")
        imagen_mostrar = imagen.copy()
        imagen_mostrar.thumbnail((400, 300))
        imagen_tk = ImageTk.PhotoImage(imagen_mostrar)

        label_imagen.config(image=imagen_tk, text="", width=0, height=0)
        label_imagen.image = imagen_tk

        imagen_modelo = imagen.resize(IMG_SIZE)

        imagen_array = np.array(imagen_modelo, dtype=np.float32)
        imagen_array = np.expand_dims(imagen_array, axis=0)

        # Predicción
        predicciones = model.predict(imagen_array, verbose=0)[0]
        indices = np.argsort(predicciones)[::-1]

        resultados = ""
        for i in indices:
            porcentaje = predicciones[i] * 100
            resultados += (f"{CLASS_NAMES[i]}: {porcentaje:.2f}%\n")

        label_resultados.config(text=resultados)

    except Exception as e:
        messagebox.showerror("Error", f"No se pudo procesar la imagen:\n{e}")


# INTERFAZ
ventana = tk.Tk()

ventana.title("Detector de Autos")
ventana.geometry("650x600")
ventana.resizable(False, False)

titulo = tk.Label(
    ventana,
    text="Detector de Autos",
    font=("Arial", 16, "bold")
)

titulo.pack(pady=15)

boton = tk.Button(
    ventana,
    text="Seleccionar imagen",
    command=seleccionar_imagen,
    font=("Arial", 11),
    padx=15,
    pady=5
)

boton.pack(pady=10)

label_imagen = tk.Label(
    ventana,
    text="Aquí aparecerá la imagen",
    width=50,
    height=15,
    bg="#eeeeee"
)

label_imagen.pack(pady=10)

label_resultados = tk.Label(
    ventana,
    text="",
    font=("Arial", 12),
    justify="left"
)

label_resultados.pack(pady=10)
ventana.mainloop()