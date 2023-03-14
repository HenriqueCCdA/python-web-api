import time

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

    dados = consulta_dados()
    processa_dados(dados)
    grava_log()

    print("Fim")
    finish = time.perf_counter()
    print(f"Finished in {round(finish - start, 2)} seconds")

main()
