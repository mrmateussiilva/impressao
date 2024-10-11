
import os
from time import sleep
from PIL import Image
from os.path import join
from functools import lru_cache
import json
# from pprint import pprint as print
import PySimpleGUI as sg

@lru_cache()
def search_deep_files(path:str) -> list:
	t = []
	for root,dirs,files in os.walk(path):
		if len(dirs) > 1:
			for d in dirs:
				for data in os.listdir(join(root,d)):
					p =join(root,d,data)
					if os.path.isfile(p):
						t.append(p)
	return t

def search_in_files(files,target) -> any:
	results = []
	for file in files:
		with open(file,"r") as fp:
			data = json.load(fp)
			for keys,values in data.items():
				nome = values.get("ARQUIVO").lower()
				if target in nome:
					# print(values)
					# print("\n")
					results.append(values)
	return results


if __name__ == "__main__":
	files = search_deep_files(r"\\Storage-silkart\IMPRESSAO\LOGS DAS MAQUINAS\ARQUIVOS_JSON")
	term = "guilerme".lower()
	results = search_in_files(files,term)
	for result in results:
		for v in result.values():
			print(f"\t{v}")
		print("\n\n")

		# print(f'{result.get("ARQUIVO")} ,{result.get("INÍCIO, DATA E HORA DO RIP")}')
		# print("\n\n")
	# print(results)
					
