import os 




p = r"C:\Users\Usuario\Desktop"
TARGET = "Scre"
exte = "jpg","jpeg","png","lnk","xlzs","html","pdf"


conjunto = set()
conjunto = list()


for data in os.listdir(p):
	conjunto.append(data)

print(conjunto)
# 	_p = os.path.join(p,data)

# 	if TARGET in data:
# 		print(_p)
# 		os.remove(_p)

# 	for ex in exte:
# 		if ex in data:
# 			os.remove(_p)
# 			print(ex)
# # 	#
# #f os.path.isdir(_p):
# # 		lista_path_clientes.append(_p)

# # for cliente in lista_path_clientes:
# # 	print(cliente)
# # 	for data in os.listdir(cliente):
# # 		print(data)
# # 	print("---------------")