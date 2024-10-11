import os
import glob
import time
import argparse
import shutil
#from PIL import Image

caminho_base =  r"\\Storage-silkart\IMPRESSAO\CLIENTES\RAMONES GARCIA\02 05 24"



arquivos_antigos = []
NOME_DE_CLIENTES = (
	"KAMILA VERGNA - ", #0
	"BARCHE (IMPRESSAO TEX) - ", #1
	"GILCIMAR-(IMPRESSAO)-",#2
	"RAMONES GARCIA-(IMPRESSAO)-",#3
	"DUELO - (IMPRESSAO)-",#4
	"RE INDUSTRIA - (IMPRESSAO)-",#5
	"DANIELA -(IMPRESSÃO)-",#6
	"CASA FELIZ -(SUBLIMAÇÃO)-CANGA-",#7
	"YAMOH -(SUBLIMAÇÃO) - ",#8
	"DESTACK -(IMPRESSAO)",#9
	"MARGARETE ALVES -(SUBLIMAÇÃO)",#10
	"LILIANE GONÇALVES -(IMPRESSAO)",#11
	"BEATRIZ VICTOR -(SUBLIMAÇÃO)",#12
	"JOERLAINE -(SUBLIMAÇÃO)",#13
	"ESCOLA POLIVALENTE - ",#14
	"ESDRAS -(SUBLIMAÇÃO)",#15
	"NUBIA NUNES -(SUBLIMAÇÃO)",#16
	"CRISTIANE FERNADES -(SUBLIMAÇÃO)",#17
	"ROMULO -(SUBLIMAÇÃO LOCAL)",#18
	"IZAURA -(SUBLIMAÇÃO)",#19
	"IVANIA BORANA - (SUBLIMAÇÃO)", #20
	"ALEXANDRE - (SUBLIMAÇÃO)", #21
	"OK PRINT - ", #22
	"INFORGRAPH - ", #23
	"DRK EVENTOS - " #23
	)

PREFIXO = NOME_DE_CLIENTES[3]
FLAG_TECIDO = ""

def renomar_arquivos(path,extensao_alvo,flag,destino):
	os.chdir(path)
	for arquivo in glob.glob(f"*.{extensao_alvo}"):
		# if PREFIXO in arquivo:
		# 	name,exte = os.path.splitext(arquivo)
		# 	lista_nome = name.split(PREFIXO)
		# 	nome_novo = lista_nome.pop()  + ".tif"
		# 	print(nome_novo)
		# 	os.rename(arquivo,nome_novo)

			#print(lista_nome.pop())

		if PREFIXO not in arquivo:
			name,exte = os.path.splitext(arquivo)
			if "painel" in name.lower():
				nome_novo = PREFIXO + name.upper() + FLAG_TECIDO + ".tif"		
			else:
				nome_novo = PREFIXO + name.upper() + FLAG_TECIDO + ".tif"		


			os.rename(arquivo,nome_novo)
			# shutil.copy2(src=arquivo,dst=os.path.join(destino,nome_novo))
		else:
		 	print("Esse arquivo já foi renomeado")

renomar_arquivos(
	caminho_base,
	"pdf",
	PREFIXO,
	None
	)


