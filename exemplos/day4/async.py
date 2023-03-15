import asyncio
import time

async def consulta_dados(): # I/O bound
    print("Consultando dados...")
    await asyncio.sleep(2) # fazendo select no DB
    return "dados"


async def processa_dados(dados): # CPU  bound
    print("Processando dados...")
    await asyncio.sleep(2)

async def grava_log(): #  I/O bound
    print("Gravando log...")
    await asyncio.sleep(2)


async def main():


    # dados = await consulta_dados() # Futuro/Promesa
    # await processa_dados(dados)
    # await grava_log()

    dados = asyncio.create_task(consulta_dados())
    asyncio.create_task(processa_dados(await dados))
    asyncio.create_task(grava_log())


start = time.perf_counter()
print("Inicio")
asyncio.run(main()) # eventloop
print("Fim")
finish = time.perf_counter()
print(f"Finished in {round(finish - start, 2)} seconds")
