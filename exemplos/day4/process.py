import time
import concurrent.futures

def consulta_dados(): # I/O bound
    print("Consultando dados...")
    time.sleep(2) # fazendo select no DB
    return "dados"


def processa_dados(dados): # CPU  bound
    print("Processando dados...")
    time.sleep(2)

def grava_log(): #  I/O bound
    print("Gravando log...")
    time.sleep(2)


def main():
    start = time.perf_counter()
    print("Inicio")

    with concurrent.futures.ProcessPoolExecutor() as executor:
        future = executor.submit(consulta_dados)
        dados =  future.result()
        executor.submit(processa_dados, dados)
        executor.submit(grava_log)
        executor.submit(grava_log)
        executor.submit(grava_log)


    print("Fim")
    finish = time.perf_counter()
    print(f"Finished in {round(finish - start, 2)} seconds")

main()
