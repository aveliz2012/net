from logging import root
import tkinter as tk
import tkinter.ttk as ttk
#import matplotlib.pyplot as plt
#import tensorflow as tf
#import numpy as np

root = tk.Tk()
root.geometry("720x480")
root.title("Redes Neuronales")
root.iconbitmap('Jean.Informatico.ico')
#estilo para los borde
style = ttk.Style()
#uso del tema clam que contiene config para los bordes
style.theme_use('clam')
#style.configure("TLabelframe", bordercolor = "red")

#Marco isq y derecho
"""
frameisq =ttk.LabelFrame(root, width= 720*0.6)
frameisq.pack(side="left", padx=2, pady=3, fill = "both", expand = True)
frameder = ttk.LabelFrame(root, width= 720*0.4)
frameder.pack(side = "right", padx=2, pady=3, fill = "both")
"""




#Marco del Menu

#frameMenu = ttk.LabelFrame(frameisq, text="Menu")
#frameMenu.pack( padx=30, pady=30)
frameMenu=ttk.LabelFrame(root, text="Menu")
frameMenu.grid(pady=5,row=0, column=0, sticky = "e, w, n, s")
left = tk.Label(frameMenu, text="prueba",  width = 100)
left.pack(side="left")

# Marco de la opciones
#frameOpciones = ttk.LabelFrame(frameisq, text="Opciones")
#frameOpciones.pack(padx=30, pady=30)
frameOpciones=ttk.LabelFrame(root, text="Opciones")
frameOpciones.grid(pady=5,row=1, column=0)
left2 = tk.Label(frameOpciones, text="prueba de la Opciones")
left2.pack()

#Marco de la consola
#frameCons = ttk.LabelFrame(frameder, text="Consola")
#frameCons.pack(padx=30, pady=30)
frameCons=ttk.LabelFrame(root, text="Consola")
frameCons.grid(pady=5,rowspan=2, column=1)
left1 = tk.Label(frameCons, text="prueba de la consola")
left1.pack()









#Paso Final para Mostrar el todo
root.mainloop()
