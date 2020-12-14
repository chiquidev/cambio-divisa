print('que quiere hacer \
1. Pasar de $ a € \
2. Pasar de € a $')
opc = input()
print("introduzca cant")
cant = input()
if(opc=="1"):
	Resultado = int(cant)*0.76
if(opc=="2"):
	Resultado = int(cant)*1.24
	
print (Resultado)