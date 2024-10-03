import pandas as pd
import random
from faker import Faker

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

print(df_reservas.head())


df_reservas.to_csv('reservas_turisticas.csv', index=False)
