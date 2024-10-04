import pandas as pd
import re
import random
from faker import Faker
from flask import Flask, request, jsonify, render_template

fake = Faker()

destinos = ['París', 'Nueva York', 'Roma', 'Tokio', 'Barcelona']
servicios = ['Hotel', 'Vuelo', 'Tour', 'Alquiler de coche', 'Crucero']
estados = ['Confirmada', 'Pendiente', 'Cancelada']

data = []

for _ in range(100):
    nombre = fake.name()
    email = fake.email()
    fecha_reserva = fake.date_this_year()
    destino = random.choice(destinos)
    servicio = random.choice(servicios)
    estado_reserva = random.choice(estados)
    precio = round(random.uniform(100, 1000), 2)  # Precio entre 100 y 1000
    data.append([nombre, email, fecha_reserva, destino, servicio, estado_reserva, precio])

df_reservas = pd.DataFrame(data, columns=['Nombre', 'Email', 'Fecha de reserva', 'Destino', 'Servicio', 'Estado', 'Precio'])

df_reservas.to_csv('reservas_turisticas.csv', index=False)

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('chatbox.html')


@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.form['message'].lower()

    if re.search(r'destino|ciudad', user_message):
        destinos_unicos = df_reservas['Destino'].unique()
        response = f'Los destinos disponibles son: {", ".join(destinos_unicos)}.'
    elif re.search(r'estado', user_message):
        estados_unicos = df_reservas['Estado'].unique()
        response = f'Los estados posibles de reserva son: {", ".join(estados_unicos)}.'
    elif re.search(r'precio|costo promedio', user_message):
        precio_promedio = df_reservas['Precio'].mean()
        response = f'El precio promedio de las reservas es: {round(precio_promedio, 2)} euros.'
    elif re.search(r'servicio', user_message):
        servicios_unicos = df_reservas['Servicio'].unique()
        response = f'Los servicios disponibles son: {", ".join(servicios_unicos)}.'
    else:
        response = 'Lo siento, no entiendo tu pregunta. Puedes preguntar sobre destinos, servicios, estados de reserva o el precio promedio.'

    return jsonify({'response': response})


if __name__ == "__main__":
    app.run(debug=True)
