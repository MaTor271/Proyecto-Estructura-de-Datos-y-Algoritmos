import tkinter as tk
 
# Función para mostrar la información de los jugadores en una ventana Tkinter
def mostrar_jugadores_tkinter(jugadores):
    ventana = tk.Tk()
    ventana.title("Información de Jugadores")
 
    etiqueta_titulo = tk.Label(ventana, text="Información de Jugadores", font=("Arial", 14))
    etiqueta_titulo.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
 
    # Encabezados de la tabla
    etiqueta_jugador = tk.Label(ventana, text="Jugador", font=("Arial", 12, "bold"))
    etiqueta_jugador.grid(row=1, column=0, padx=5, pady=5)
    etiqueta_region = tk.Label(ventana, text="Región", font=("Arial", 12, "bold"))
    etiqueta_region.grid(row=1, column=1, padx=5, pady=5)
    etiqueta_rango = tk.Label(ventana, text="Rango", font=("Arial", 12, "bold"))
    etiqueta_rango.grid(row=1, column=2, padx=5, pady=5)
    etiqueta_pin = tk.Label(ventana, text="PIN", font=("Arial", 12, "bold"))
    etiqueta_pin.grid(row=1, column=3, padx=5, pady=5)
 
    # Mostrar información de los jugadores
    fila = 2
    for nombre, info in jugadores.items():
        etiqueta_nombre = tk.Label(ventana, text=nombre, font=("Arial", 10))
        etiqueta_nombre.grid(row=fila, column=0, padx=5, pady=5)
        etiqueta_region = tk.Label(ventana, text=info["region"], font=("Arial", 10))
        etiqueta_region.grid(row=fila, column=1, padx=5, pady=5)
        etiqueta_rango = tk.Label(ventana, text=info["rango"], font=("Arial", 10))
        etiqueta_rango.grid(row=fila, column=2, padx=5, pady=5)
        etiqueta_pin = tk.Label(ventana, text=info["pin"], font=("Arial", 10))
        etiqueta_pin.grid(row=fila, column=3, padx=5, pady=5)
        fila += 1
 
 
 
    ventana.mainloop()