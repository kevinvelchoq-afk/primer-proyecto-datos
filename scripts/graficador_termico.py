import pandas as pd
import matplotlib.pyplot as plt

# Cargar datos del sensor
ruta_datos = "../data/temp_test.csv"

def generar_grafica():
    try:
        df = pd.read_csv(ruta_datos)
        
        # Crear la gráfica
        plt.figure(figsize=(8, 5))
        plt.plot(df['timestamp'], df['temp_c'], marker='o', color='red', linestyle='-')
        
        # Personalización técnica
        plt.title("Curva de Enfriamiento - Monitoreo de Soldadura")
        plt.xlabel("Tiempo de registro")
        plt.ylabel("Temperatura (°C)")
        plt.grid(True, linestyle='--', alpha=0.6)
        
        # Guardar el reporte visual en la carpeta correcta
        ruta_salida = "../reports/curva_enfriamiento.png"
        plt.savefig(ruta_salida)
        print(f"--- [OK] Gráfica generada exitosamente en: {ruta_salida} ---")
        
    except Exception as e:
        print(f"--- [ERROR] No se pudo generar la gráfica: {e} ---")

if __name__ == "__main__":
    generar_grafica()
