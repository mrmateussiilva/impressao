import os
import glob
import sys
import math
import functools
from PIL import Image
Image.MAX_IMAGE_PIXELS = None
LEN_PLACA = 150

@functools.lru_cache()
def pixel_for_cm(size,dpi):
	if len(size) == 2:
		return tuple(map(lambda x: 2.54 * (x / dpi),size))

@functools.lru_cache()
def get_size_image_and_dpi(path_file):
	try:
		i = Image.open(path_file)
		return i.size,int(i.info["dpi"][0])
	except FileNotFoundError:
		print(f"O arquivo '{path_file}' não existe")
	except Exception as err:
		print(err)

@functools.lru_cache()
def listar_arquivos(path,extensao_alvo=".tif"):
	lista_arquivos = []
	for arquivo in glob.glob(os.path.join(path,f"*{extensao_alvo}")):
		lista_arquivos.append(arquivo)
	return lista_arquivos

metros_linear_malha = metros_linear_tactel = 0


def somar_metros(path):
	soma = []
	arquivos = listar_arquivos(path)
	
	for arquivo in arquivos:
		try:
			dimensoes,dpi = get_size_image_and_dpi(arquivo)
			metro_linear = pixel_for_cm(dimensoes,dpi)
			if max(metro_linear) > 160 and "tac" in arquivo.lower():
				calc = round((max(metro_linear) / LEN_PLACA) )* min(metro_linear)
				soma.append(calc)
			else:
				soma.append(max(metro_linear))
		except:
			pass
	return sum(soma)






if __name__ == "__main__":
	PATH = r"\\Storage-silkart\IMPRESSAO\temp_tactel"
	
	PATH_1 = r"\\Storage-silkart\IMPRESSAO\temp_malha"

	path_tmp_adesivo = r"\\Storage-silkart\IMPRESSAO\TEMP_ADESIVO"
	malha = somar_metros(PATH_1)
	tactel =somar_metros(PATH)
	adesivo =somar_metros(path_tmp_adesivo)
	print(f"TACTEL: {tactel / 100:.2f}")
	print(f"MALHA: {malha / 100:.2f}")
	print(f"ADESIVO: {adesivo / 100:.2f}")
	
	
