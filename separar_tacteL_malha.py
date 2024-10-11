import os
from os.path import join

from json import load, dump 

class PyJson:
    def __init__(self):
        pass

    def ler_json(self, nome_arquivo_json) -> dict:
        with open(nome_arquivo_json, "r") as file:
            data = load(file)
        return data

    def escrever_json(self, dados, nome_arquivo) -> bool:
        try:
            fp = open(nome_arquivo, "w+")
            dump(dados, fp)
        except:
            return False

        finally:
            fp.close()

        return True



PATH = r"\\Storage-silkart\IMPRESSAO\LOGS DAS MAQUINAS\MAQUINAS"
MAQUINA = "1904"
PATH_DESTINO = r"\\Storage-silkart\IMPRESSAO\LOGS DAS MAQUINAS\ARQUIVOS_JSON\{MAQUINA}"

for mes in os.listdir(PATH_DESTINO):
    print(mes)
    


