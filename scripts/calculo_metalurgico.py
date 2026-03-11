import pandas as pd

ruta_datos = "../data/temp_test.csv"

def calcular_t85():
    try:
        df = pd.read_csv(ruta_datos)
        
        # Buscamos el momento en que baja de 800 y cuando llega a 500
        t800 = df[df['temp_c'] <= 800].iloc[0]
        t500 = df[df['temp_c'] <= 500].iloc[0]
        
        # Calculamos la diferencia de tiempo (asumiendo intervalos de 2 min)
        # Esto es una simplificación para tu bitácora inicial
        idx_800 = df[df['temp_c'] <= 800].index[0]
        idx_500 = df[df['temp_c'] <= 500].index[0]
        
        tiempo_segundos = (idx_500 - idx_800) * 120 # 2 minutos = 120 seg
        
        print("-" * 40)
        print("RESUMEN METALÚRGICO DE ENFRIAMIENTO")
        print(f"Punto 800°C detectado en: {t800['timestamp']}")
        print(f"Punto 500°C detectado en: {t500['timestamp']}")
        print(f"Tiempo t8/5 calculado: {tiempo_segundos} segundos")
        print("-" * 40)
        
        if tiempo_segundos < 10:
            print("AVISO: Enfriamiento muy rápido. Riesgo de dureza excesiva.")
        else:
            print("ESTADO: Velocidad de enfriamiento dentro de rangos normales.")

    except Exception as e:
        print(f"Error en el cálculo: {e}")

if __name__ == "__main__":
    calcular_t85()
