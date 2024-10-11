import os
from PIL import Image
from os.path import join,isfile,splitext
Image.MAX_IMAGE_PIXELS = None



def pixel_for_cm(size,dpi):
	if len(size) == 2:
		return tuple(map(lambda x: 2.54 * (x / dpi),size))


def get_size_image_and_dpi(i):
	try:
		return i.size,int(i.info["dpi"][0])
	except FileNotFoundError:
		print(f"O arquivo '{path_file}' não existe")
	except Exception as err:
		print(err)



path = r"\\Storage-silkart\IMPRESSAO\18 07 2024\BOLSINHAS"
for file in os.listdir(path):
	p = join(path,file)
	if isfile(p) and "tif" in file:
		i = Image.open(p)
		dpi = get_size_image_and_dpi(i)
		size_cm = pixel_for_cm(i.size,dpi[1])
		if sum(size_cm) >= 620:
			print(file,"------Bolsinha GRANDE")
		else:
			print(file,"------Bolsinha PEQUENA")

		

		# print(file,"==",size_cm)