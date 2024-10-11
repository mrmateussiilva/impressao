import json
from os import walk
from os.path import join,split
from pprint import pprint as print
paht = r"\\Storage-silkart\IMPRESSAO\LOGS DAS MAQUINAS\ARQUIVOS_JSON"
target = "VIDATIVA - CAL-0003 - PLACA CORRIDA - OK.tif"
for r,d, files in walk(paht):

	if len(files) > 0:
		# print(files)
		for file in files:
			p = join(r,file)
			# print(p)
			with open(p,"r") as fp:
				data = json.load(fp)
				for d in data:
					for v in d.values():
						_,nome = split(v["ARQUIVO"])
						if target in nome:
							print(v["ARQUIVO"])

