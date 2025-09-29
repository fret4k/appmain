import time
import math
import argparse
from multiprocessing import Pool, cpu_count

def cpu_stress_task(args):
    n, factorial_size = args
    start_time = time.time()
    for _ in range(n):
        math.factorial(factorial_size)
    return time.time() - start_time

def main():
    parser = argparse.ArgumentParser(description="Prueba de estrés de la CPU")
    parser.add_argument("--iterations", type=int, default=50000, help="Iteraciones por núcleo")
    parser.add_argument("--factorial-size", type=int, default=500, help="Tamaño del factorial a calcular")
    parser.add_argument("--cores", type=int, default=cpu_count(), help="Número de núcleos a utilizar")
    args = parser.parse_args()

    print("Iniciando prueba de estrés de la CPU...")
    print(f"Número de núcleos de CPU a usar: {args.cores}")
    print(f"Iteraciones por núcleo: {args.iterations}")
    print(f"Tamaño del factorial: {args.factorial_size}")

    start_total_time = time.time()

    with Pool(processes=args.cores) as pool:
        tiempos = pool.map(cpu_stress_task, [(args.iterations, args.factorial_size)] * args.cores)

    end_total_time = time.time()
    total_time = end_total_time - start_total_time

    total_operations = args.iterations * args.cores
    operations_per_second = total_operations / total_time
    score = int(operations_per_second)

    print("\n----- Resultados de la Prueba de Estrés -----")
    print(f"Tiempo total de ejecución: {total_time:.2f} segundos")
    print(f"Puntuación de la CPU: {score} puntos")
    print(f"Tiempos individuales por núcleo: {['{:.2f}'.format(t) for t in tiempos]}")
    print("---------------------------------------------")
    print("\n(Una puntuación más alta indica un mejor rendimiento de la CPU)")

if __name__ == '__main__':
    main()