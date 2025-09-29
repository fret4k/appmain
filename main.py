print('i am') 
import time
import math
from multiprocessing import Pool, cpu_count

def cpu_stress_task(n):
    """
    Función que realiza un cálculo intensivo para la CPU.
    """
    start_time = time.time()
    for i in range(n):
        math.factorial(500)  # Cálculo de factorial, una operación costosa
    return time.time() - start_time

def main():
    """
    Función principal para ejecutar la prueba de estrés y calcular la puntuación.
    """
    print("Iniciando prueba de estrés de la CPU...")

    # Número de iteraciones por núcleo
    iterations_per_core = 50000
    
    # Obtener el número de núcleos de la CPU
    num_cores = cpu_count()
    print(f"Número de núcleos de CPU detectados: {num_cores}")

    # Iniciar el temporizador
    start_total_time = time.time()

    # Crear un pool de procesos para utilizar todos los núcleos
    with Pool(processes=num_cores) as pool:
        # Distribuir la tarea entre los núcleos
        pool.map(cpu_stress_task, [iterations_per_core] * num_cores)

    # Detener el temporizador
    end_total_time = time.time()
    total_time = end_total_time - start_total_time

    # Calcular la puntuación
    total_operations = iterations_per_core * num_cores
    operations_per_second = total_operations / total_time
    score = int(operations_per_second)

    print("\n----- Resultados de la Prueba de Estrés -----")
    print(f"Tiempo total de ejecución: {total_time:.2f} segundos")
    print(f"Puntuación de la CPU: {score} puntos")
    print("---------------------------------------------")
    print("\n(Una puntuación más alta indica un mejor rendimiento de la CPU)")

# test de cpu
# Ejecutar la función principal
if __name__ == '__main__':
    main()