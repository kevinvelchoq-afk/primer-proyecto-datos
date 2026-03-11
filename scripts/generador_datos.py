import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Configuración: 20 lecturas cada 2 minutos
n_lecturas = 20
inicio_temp = 800  # Temperatura de soldeo en °C
tiempo_actual = datetime.now()

tiempos = []
temperaturas = []

for i in range(n_lecturas):
    # Simula enfriamiento exponencial (Física real)
    temp = inicio_temp * np.exp(-0.05 * i) + np.random.normal(0, 2)
    tiempos.append(tiempo_actual.strftime("%H:%M:%S"))
    temperaturas.append(round(temp, 2))
    tiempo_actual += timedelta(minutes=2)

# Crear el DataFrame y guardarlo
df = pd.DataFrame({'timestamp': tiempos, 'temp_c': temperaturas})
df.to_csv("../data/temp_test.csv", index=False)

print(f"--- [OK] Se han generado {n_lecturas} nuevas mediciones en data/temp_test.csv ---")
