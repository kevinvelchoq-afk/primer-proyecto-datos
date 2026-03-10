import pandas as pd
import os

# Definir la ruta del archivo de datos
ruta_datos = "../data/temp_test.csv"

def analizar_soldadura():
    if not os.path.exists(ruta_datos):
        print("Error: No se encuentra el archivo de datos en /data")
        return

    # Leer el CSV con Pandas
    df = pd.read_csv(ruta_datos)
    
    print("--- INFORME DE ESTADO TERMICO ---")
    print(df) # Esto muestra la tabla en terminal
    
    # Lógica técnica: Si la temperatura es > 200C, el material sigue crítico
    ultima_temp = df['temp_c'].iloc[-1]
    
    if ultima_temp > 200:
        print(f"\nALERTA: Temperatura actual {ultima_temp}C. Zona de riesgo de fisuracion.")
    else:
        print(f"\nESTADO: Temperatura de seguridad alcanzada ({ultima_temp}C).")

if __name__ == "__main__":
    analizar_soldadura()
