import tkinter as tk
from tkinter import PhotoImage
from random import choice


class PiedraPapelTijeraApp:
    def __init__(self, root): #Definimos el metodo
        #Identificador ventanas
        self.root = root
        self.root.geometry("500x300")
        self.root.resizable (0,0)
        self.root.configure (background="#f8f7f2")
        self.root.title("Juego Piedra, Papel o Tijera")

        # Puntuaciones
        self.jugador_puntos = 0
        self.computadora_puntos = 0

        self.bienvenida= tk.Label(root, text="¿Jugamos juntos? \n Haz tu elección" , font=("Arial", 14), bg="#f8f7f2")
        self.bienvenida.pack()

        # Etiquetas de puntuación
        self.jugador_label = tk.Label(root, text="\n Jugador: 0", font=("Arial", 13),bg="#f8f7f2")
        self.jugador_label.pack()
        
        self.computadora_label = tk.Label(root, text="Computadora: 0", font=("Arial", 13),bg="#f8f7f2")
        self.computadora_label.pack()

        # Resultado del juego
        self.resultado_label = tk.Label(root, text="\n Elige una opción", font=("Arial", 15), fg="purple",bg="#f8f7f2")
        self.resultado_label.pack(pady=10)

        # Selección de la computadora
        self.seleccion_computadora_label = tk.Label(root, text="Computadora eligió: -", font=("Arial", 14),bg="#f8f7f2")
        self.seleccion_computadora_label.pack(pady=10)

        # Botones de opciones
        self.botones_frame = tk.Frame(root)
        self.botones_frame.configure (background="#f8f7f2")
        self.botones_frame.pack(pady=10)

        self.piedra_btn = tk.Button(self.botones_frame, text="Piedra", font=("Arial",12), bg=("beige"), command=lambda: self.jugar("Piedra"))
        self.piedra_btn.grid(row=0, column=0, padx=10)

        self.papel_btn = tk.Button(self.botones_frame, text="Papel", font=("Arial",12), bg=("beige"), command=lambda: self.jugar("Papel"))
        self.papel_btn.grid(row=0, column=1, padx=10)

        self.tijera_btn = tk.Button(self.botones_frame, text="Tijera", font=("Arial",12), bg=("beige"), command=lambda: self.jugar("Tijera"))
        self.tijera_btn.grid(row=0, column=2, padx=10)

        
    #Función para desarrollar juego 
    def jugar(self, jugador_seleccion):
        opciones = ["Piedra", "Papel", "Tijera"]
        computadora_seleccion = choice(opciones)

        # Mostrar selección de la computadora
        self.seleccion_computadora_label.config(text=f"Computadora eligió: {computadora_seleccion}")

        # Determinar el resultado mediante bucle
        if jugador_seleccion == computadora_seleccion:
           resultado = "Empate"
           self.jugador_puntos += 1
           self.computadora_puntos += 1
        elif (jugador_seleccion == "Piedra" and computadora_seleccion == "Tijera") or \
             (jugador_seleccion == "Papel" and computadora_seleccion == "Piedra") or \
             (jugador_seleccion == "Tijera" and computadora_seleccion == "Papel"):
            resultado = "Ganaste"
            self.jugador_puntos += 1
        else:
            resultado = "Perdiste"
            self.computadora_puntos += 1
    
      # Actualizar el resultado y puntuaciones
        self.resultado_label.config(text=f"{resultado}")
        self.jugador_label.config(text=f"Jugador: {self.jugador_puntos}")
        self.computadora_label.config(text=f"Computadora: {self.computadora_puntos}")

#Llamar a las funciones para que se ejecuten
if __name__ == "__main__":
    root = tk.Tk()
    app = PiedraPapelTijeraApp(root)
    root.mainloop()
