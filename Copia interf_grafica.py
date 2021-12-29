import tkinter as tk
from tkinter import ttk

class ModeloFrame(ttk.Frame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.name_entry = ttk.Entry(self)
        self.name_entry.pack()

        self.greet_button = ttk.Button(
        self, text="Saludar", command=self.say_hello)
        self.greet_button.pack()

        self.greet_label = ttk.Label(self)
        self.greet_label.pack()

    def say_hello(self):
        self.greet_label["text"] = \
            "¡Hola, {}!".format(self.name_entry.get())

class SalidaFrame(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.label = ttk.Label(self)
        self.label["text"] = ("Visitanos en recursos python.com y "
        "foro.recursospython.com.")
        self.label.pack()

        self.web_button = ttk.Button(self, text="Visitar web")
        self.web_button.pack(pady=10)

        self.forum_button = ttk.Button(self, text="Visitar foro")
        self.forum_button.pack()

class Application(ttk.Frame):
    def __init__(self, main_window):
        super().__init__(main_window)
        main_window.title("GUI Modelo de Red Neuronal")
        self.notebook = ttk.Notebook(self)

        self.greeting_frame = ModeloFrame(self.notebook)
        self.notebook.add(
        self.greeting_frame, text="Modelo", padding=10)

        self.about_frame = SalidaFrame(self.notebook)
        self.notebook.add(
        self.about_frame, text="Resultado", padding=10)

        self.notebook.pack(padx=10, pady=10)
        #self.configure(width=1800, height=800)
        self.pack(expand=True, fill=tk.BOTH)

main_window = tk.Tk()
app = Application(main_window)
app.mainloop()
