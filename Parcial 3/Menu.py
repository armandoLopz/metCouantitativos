import tkinter as tk
import subprocess
import os
from PIL import Image, ImageTk

class Aplicacion:
    def __init__(self):        
        self.ventana = tk.Tk()                             
        self.ventana.title('Calculadora para Simulaciones')
        self.ventana.geometry('800x500')
        self.ventana.config(bg='#fcfcfc')
        self.ventana.resizable(width=0, height=0)    
        self.centrar_ventana(self.ventana, 1100, 800)

        # Cargar el logo usando la ruta absoluta
        base_path = r"C:\Users\Fusco\OneDrive\Escritorio\New folder"
        logo_path = os.path.join(base_path, "foto.jpg")
        logo = self.leer_imagen(logo_path, (500, 500))

        # Frame del logo
        frame_logo = tk.Frame(self.ventana, bd=0, width=400, relief=tk.SOLID, padx=10, pady=10, bg='#fcfcfc')
        frame_logo.pack(side="left", expand=tk.YES, fill=tk.BOTH)

        if logo:
            label = tk.Label(frame_logo, image=logo, bg='#fcfcfc')
            label.place(x=0, y=0, relwidth=1, relheight=1)
        else:
            label = tk.Label(frame_logo, text="Logo no disponible", bg='#fcfcfc', font=('Times', 20))
            label.pack(expand=True)

        # Frame del formulario
        frame_form = tk.Frame(self.ventana, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        frame_form.pack(side="right", expand=tk.YES, fill=tk.BOTH)

        # Frame superior del formulario
        frame_form_top = tk.Frame(frame_form, height=30, bd=0, relief=tk.SOLID, bg='black')
        frame_form_top.pack(side="top", fill=tk.X)
        title = tk.Label(frame_form_top, text="Calculadora para Simulaciones", font=('Times', 30), fg="#666a88", bg='#fcfcfc', pady=50)
        title.pack(expand=tk.YES, fill=tk.BOTH)

        # Frame inferior del formulario
        frame_form_fill = tk.Frame(frame_form, height=30, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        frame_form_fill.pack(side="bottom", expand=tk.YES, fill=tk.BOTH)

        # Botones para abrir otros programas de Python
        inicio_1 = tk.Button(frame_form_fill, text="Reaccion Quimica", font=('Times', 15, 'bold'), bg='#3a7ff6', bd=0, fg="#fff", command=self.ContinuoReaccionQuimica)
        inicio_1.pack(fill=tk.X, padx=140, pady=30)

        inicio_2 = tk.Button(frame_form_fill, text="Reactor Nuclear", font=('Times', 15, 'bold'), bg='#3a7ff6', bd=0, fg="#fff", command=self.ContinuoReactorNuclear)
        inicio_2.pack(fill=tk.X, padx=140, pady=20)

        inicio_3 = tk.Button(frame_form_fill, text="Peluqueria", font=('Times', 15, 'bold'), bg='#3a7ff6', bd=0, fg="#fff", command=self.DiscretaPeluqueria)
        inicio_3.pack(fill=tk.X, padx=140, pady=20)

        inicio_4 = tk.Button(frame_form_fill, text="Restaurante", font=('Times', 15, 'bold'), bg='#3a7ff6', bd=0, fg="#fff", command=self.DiscretaRestaurante)
        inicio_4.pack(fill=tk.X, padx=140, pady=20)

        inicio_5 = tk.Button(frame_form_fill, text="Restaurante2", font=('Times', 15, 'bold'), bg='#3a7ff6', bd=0, fg="#fff", command=self.DiscretaRestaurante2)
        inicio_5.pack(fill=tk.X, padx=140, pady=20)

        inicio_6 = tk.Button(frame_form_fill, text="Sistema Redes", font=('Times', 15, 'bold'), bg='#3a7ff6', bd=0, fg="#fff", command=self.DiscretaSistemaRedes)
        inicio_6.pack(fill=tk.X, padx=140, pady=20)

        # Botón para salir
        exit_button = tk.Button(frame_form_fill, text="Salir", font=('Times', 15, 'bold'), bg='red', bd=0, fg="#fff", command=self.ventana.quit)
        exit_button.pack(fill=tk.X, padx=140, pady=20)

        self.ventana.mainloop()

    def ContinuoReaccionQuimica(self):
        subprocess.run(["python", r"C:\Users\Fusco\OneDrive\Escritorio\New folder\ContinuoReaccionQuimica.py"])

    def ContinuoReactorNuclear(self):
        subprocess.run(["python", r"C:\Users\Fusco\OneDrive\Escritorio\New folder\ContinuoReactorNuclear.py"])

    def DiscretaPeluqueria(self):
        subprocess.run(["python", r"C:\Users\Fusco\OneDrive\Escritorio\New folder\DiscretaPeluqueria.py"])

    def DiscretaRestaurante(self):
        subprocess.run(["python", r"C:\Users\Fusco\OneDrive\Escritorio\New folder\DiscretaRestaurante.py"])

    def DiscretaRestaurante2(self):
        subprocess.run(["python", r"C:\Users\Fusco\OneDrive\Escritorio\New folder\DiscretaRestaurante2.py"])

    def DiscretaSistemaRedes(self):
        subprocess.run(["python", r"C:\Users\Fusco\OneDrive\Escritorio\New folder\DiscretaSistemaRedes.py"])

    def centrar_ventana(self, ventana, ancho, alto):
        pantalla_ancho = ventana.winfo_screenwidth()
        pantalla_alto = ventana.winfo_screenheight()
        x = int((pantalla_ancho / 2) - (ancho / 2))
        y = int((pantalla_alto / 2) - (alto / 2))
        ventana.geometry(f'{ancho}x{alto}+{x}+{y}')

    def leer_imagen(self, path, size):
        try:
            imagen = Image.open(path)
            imagen = imagen.resize(size, Image.Resampling.LANCZOS)
            return ImageTk.PhotoImage(imagen)
        except FileNotFoundError:
            print(f"Error: The file '{path}' was not found.")
            return None  # Return None or a placeholder image
        except Exception as e:
            print(f"Error loading image: {e}")
            return None

if __name__ == "__main__":
    app = Aplicacion()
