import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np
from tkinter import filedialog as FileDialog

fichero = FileDialog.askopenfilename(title="Cagar Modelo")
print (fichero)
try:
    #Cargar el modelo si existe
    json_file = open('modelo.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    modelo = tf.keras.models.model_from_json(loaded_model_json)
    # cargar pesos al nuevo modelo
    modelo.load_weights("model.h5")
    print("Cargado modelo desde disco.")
    modelo.compile(
        optimizer = tf.keras.optimizers.Adam(0.1), 
        loss = 'mean_squared_error')

    
except Exception  as e:
    print("habido un error")
    print(type(e).__name__)
    # Valores entrada y salidad 
    celsius = np.array([-40, -10, 0, 8, 15, 22, 38], dtype=float)
    fahrenheit = np.array([-40, 14, 32, 46, 59, 72, 100], dtype=float)

    #Crear redes neurorales simple con Kera
    capa = tf.keras.layers.Dense (units = 1, input_shape = [1])
    modelo = tf.keras.Sequential([capa])
    modelo.compile(
        optimizer = tf.keras.optimizers.Adam(0.1), 
        loss = 'mean_squared_error')
    print("Comenzando el entrenamiento.....")
    historial = modelo.fit(celsius,fahrenheit, epochs = 1000, verbose = False)
    print("Modelo entrenado")

    # Salvar el modelo entrenado
    # serializar el modelo a json
    model_json = modelo.to_json()
    with open("modelo.json", "w") as json_file:
        json_file.write(model_json)
    # serializar los pesos a HDF5
    modelo.save_weights("model.h5")
    print("Modelo Guardado!")
    plt.xlabel("#Epoca")
    plt.ylabel("#Magnitud de Perdida")
    plt.plot(historial.history["loss"])
    #imprimir valores interno del modelo
    print("Variables interna del modelo")
    print(capa.get_weights())


# Hacer la prediccion
print("Hagamos una predicion")
resultado = modelo.predict([200.0])
print("Resultado es {} fahrenheit".format(resultado))


