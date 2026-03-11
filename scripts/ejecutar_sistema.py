import os
import subprocess

def ejecutar_todo():
    print("=== INICIANDO SISTEMA DE MONITOREO TERMICO ===")
    
    # 1. Generar nuevos datos de sensor
    print("\n[1/3] Generando datos de enfriamiento...")
    subprocess.run(["python3", "generador_datos.py"])
    
    # 2. Realizar calculo metalurgico t8/5
    print("\n[2/3] Ejecutando analisis metalurgico...")
    subprocess.run(["python3", "calculo_metalurgico.py"])
    
    # 3. Actualizar el grafico de reporte
    print("\n[3/3] Actualizando graficos en /reports...")
    subprocess.run(["python3", "graficador_termico.py"])
    
    print("\n=== PROCESO COMPLETADO EXITOSAMENTE ===")
    print("Revisa la carpeta /reports para ver la nueva curva.")

if __name__ == "__main__":
    ejecutar_todo()
