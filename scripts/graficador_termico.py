import pandas as pd
import matplotlib.pyplot as plt

# Cargar datos del sensor
ruta_datos = "../data/temp_test.csv"

def generar_grafica():
    try:
        df = pd.read_csv(ruta_datos)

        # 1. Configurar el tamaño de la imagen
        plt.figure(figsize=(10, 6))

        # 2. Dibujar la linea roja con los puntos
        plt.plot(df['timestamp'], df['temp_c'], marker='o', color='red', linestyle='-')

        # --- NUEVA LÍNEA DE REFERENCIA METALÚRGICA ---
        plt.axhline(y=500, color='green', linestyle='--', linewidth=2, label='Límite Crítico (500°C)')
        # ---------------------------------------------

        # 3. LIMPIEZA DEL EJE X (Aquí está el truco)
        # Saltamos de 3 en 3 etiquetas y las rotamos para que no se choquen
        plt.xticks(ticks=df['timestamp'][::3], rotation=45)

        # 4. Personalizacion tecnica
        plt.title("Curva de Enfriamiento - Monitoreo de Soldadura")
        plt.xlabel("Tiempo de registro")
        plt.ylabel("Temperatura (°C)")
        plt.grid(True, linestyle='--', alpha=0.6)
        
        # 5. Ajustar margenes para que no se corte el texto rotado
        plt.tight_layout()

        # 6. Guardar el archivo
        ruta_salida = "../reports/curva_enfriamiento.png"
        plt.savefig(ruta_salida)
        print(f"--- [OK] Grafica legible generada en: {ruta_salida} ---")

    except Exception as e:
        print(f"--- [ERROR] No se pudo generar la grafica: {e} ---")

if __name__ == "__main__":
    generar_grafica()
