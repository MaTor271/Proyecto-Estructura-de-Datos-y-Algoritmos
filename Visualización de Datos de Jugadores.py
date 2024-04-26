from flask import Flask
 
app = Flask(__name__)
 
# Datos de los jugadores
jugadores = {
    "Jugador1": {"region": "América del Norte", "rango": "Platino", "pin": 1234},
    "Jugador2": {"region": "Europa", "rango": "Diamante", "pin": 5678},
    "Jugador3": {"region": "Asia", "rango": "Oro", "pin": 9012},
    "Jugador4": {"region": "América del Sur", "rango": "Plata", "pin": 3456},
    "Jugador5": {"region": "Oceanía", "rango": "Bronce", "pin": 7890},
    "Jugador6": {"region": "América del Norte", "rango": "Platino", "pin": 2468},
    "Jugador7": {"region": "Europa", "rango": "Diamante", "pin": 1357},
    "Jugador8": {"region": "Asia", "rango": "Oro", "pin": 7891},
    "Jugador9": {"region": "América del Sur", "rango": "Plata", "pin": 3579},
    "Jugador10": {"region": "Oceanía", "rango": "Bronce", "pin": 8023},
    "Jugador11": {"region": "América del Norte", "rango": "Platino", "pin": 6420},
    "Jugador12": {"region": "Europa", "rango": "Diamante", "pin": 7531},
    "Jugador13": {"region": "Asia", "rango": "Oro", "pin": 2345},
    "Jugador14": {"region": "América del Sur", "rango": "Plata", "pin": 9087},
    "Jugador15": {"region": "Oceanía", "rango": "Bronce", "pin": 6754},
    "Jugador16": {"region": "América del Norte", "rango": "Platino", "pin": 9786},
    "Jugador17": {"region": "Europa", "rango": "Diamante", "pin": 5432},
    "Jugador18": {"region": "Asia", "rango": "Oro", "pin": 2109},
    "Jugador19": {"region": "América del Sur", "rango": "Plata", "pin": 8654},
    "Jugador20": {"region": "Oceanía", "rango": "Bronce", "pin": 1236},
    "Jugador21": {"region": "América del Norte", "rango": "Platino", "pin": 9876},
    "Jugador22": {"region": "Europa", "rango": "Diamante", "pin": 4567},
    "Jugador23": {"region": "Asia", "rango": "Oro", "pin": 3210},
    "Jugador24": {"region": "América del Sur", "rango": "Plata", "pin": 6543},
    "Jugador25": {"region": "Oceanía", "rango": "Bronce", "pin": 7891}
}
 
# Ruta para mostrar la información de los jugadores en una ventana Tkinter
@app.route('/')
def mostrar_jugadores_web():
    from gui import mostrar_jugadores_tkinter
    mostrar_jugadores_tkinter(jugadores)
    return "Información de jugadores mostrada en la ventana Tkinter"
 
if __name__ == '__main__':
    app.run(debug=True)