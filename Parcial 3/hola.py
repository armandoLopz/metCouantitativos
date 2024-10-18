import subprocess
import tkinter as tk

class SimuladorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simulador de Procesos")

        # Crear botones para abrir cada programa
        self.boton1 = tk.Button(root, text="Descomposición", command=self.abrir_descomposicion)
        self.boton1.pack(pady=10)

        self.boton2 = tk.Button(root, text="Programa 2", command=self.abrir_programa2)
        self.boton2.pack(pady=10)

        self.boton3 = tk.Button(root, text="Programa 3", command=self.abrir_programa3)
        self.boton3.pack(pady=10)

        self.boton4 = tk.Button(root, text="Programa 4", command=self.abrir_programa4)
        self.boton4.pack(pady=10)

        self.boton5 = tk.Button(root, text="Programa 5", command=self.abrir_programa5)
        self.boton5.pack(pady=10)

        self.boton6 = tk.Button(root, text="Programa 6", command=self.abrir_programa6)
        self.boton6.pack(pady=10)

    def abrir_descomposicion(self):
        subprocess.run(["python", r"C:\Users\Fusco\OneDrive\Escritorio\New folder\ContinuoReaccionQuimica.py"])

    def abrir_programa2(self):
        subprocess.run(["python", r"C:\ruta\completa\a\ContinuoReactorNuclear.py"])  # Cambia la ruta

    def abrir_programa3(self):
        subprocess.run(["python", r"C:\ruta\completa\a\DiscretaPeluqueria.py"])  # Cambia la ruta

    def abrir_programa4(self):
        subprocess.run(["python", r"C:\ruta\completa\a\DiscretaRestaurante.py"])  # Cambia la ruta

    def abrir_programa5(self):
        subprocess.run(["python", r"C:\ruta\completa\a\DiscretaRestaurante2.py"])  # Cambia la ruta

    def abrir_programa6(self):
        subprocess.run(["python", r"C:\ruta\completa\a\DiscretaSistemaRedes.py"])  # Cambia la ruta

if __name__ == "__main__":
    root = tk.Tk()
    app = SimuladorApp(root)
    root.mainloop()
