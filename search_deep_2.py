
import os
from time import sleep
from PIL import Image


def pixel_for_cm(size,dpi):
	if len(size) == 2:
		return tuple(map(lambda x: 2.54 * (x / dpi),size))


def get_size_image_and_dpi(path_file):
	try:
		i = Image.open(path_file)
		return i.size,int(i.info["dpi"][0])
	except FileNotFoundError:
		print(f"O arquivo '{path_file}' não existe")
	except Exception as err:
		print(err)



lista_arquivos = []
P =r"\\Storage-silkart\impressao"
target = "splash"
for root, dirs, files in os.walk(P):
	if len(files) > 0:
		for file in files:
			p = os.path.join(root,file)
			if target in file.lower():
				print(p)
				# sleep(0.8)
			#lista_arquivos.append(p)


# for  arquivo in lista_arquivos:
# 	img = Image.open(arquivo)
# 	size = img.size
# 	dpi = img.info["dpi"][0]
# 	tamanho = pixel_for_cm(size,dpi)
# 	print(tamanho)
# print()

