import time

def cpu_benchmark(iterations=100_000_000):
    print("Iniciando benchmark de CPU...")
    start = time.time()
    result = 0
    for i in range(iterations):
        result += (i % 10) * (i % 5)
    end = time.time()
    print(f"Resultado: {result}")
    print(f"Tiempo transcurrido: {end - start:.2f} segundos")

if __name__ == "__main__":
    cpu_benchmark()