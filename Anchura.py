"""
Cada funcion recibe la Carteta donde
empezara a buscar y el archivo a buscar

La funcion retorna True si encuentra 
el archivo, e imprime la ruta

en caso contrario retorna falso

def primeroProfundidad(Carpeta,Archivo):
	pass
def primeroAnchura(Carpeta,Archivo):
	pass
"""

import json
with open('base3.json') as file:
	data = json.load(file)
cola = []
colaux = []

def anchura(inicio,busqueda):
	cola.append(inicio)
	if inicio == busqueda: 
		return busqueda
	for L in data:
		cola.append(L[1])
		nodo = cola.pop(0) 
		if nodo not in colaux:
			colaux.append(nodo)
			vecinos = nodo
		print(nodo)
		if vecinos == busqueda:
			print("/////Archivo encontrado///// \n")
			return 0
		else: 
			print("-----No encontrado----------")
	return colaux
resultado = anchura('Imagenes','Perfiltinder.jpg')

"""print(cola)"""
print("Cola de regorrido primero enterar y primero en salir \n")

print(cola)
print("")
print("Recorrido del algoritmo nodo a nodo (Cola de acarreo)\n")
print(colaux)


"""for l in data:
		cola.append(l[0])
	cola.pop(0)
resultado = anchura('1','2')
print(cola)"""
"""
def busqueda(cuspide,valorbusqueda):
	camino.append(cuspide)
	
	if cuspide == valorbusqueda:
		return valorbusqueda
		
	for k,v in data:
		if v == cuspide:
			resultado=busqueda(k,valorbusqueda)
			if resultado:
				return resultado
	camino.pop()
	return 0
resultado=busqueda("C:","MemoriaRam.exe")
if resultado:
	print ("Archivo encontrado")
	print(camino)
else:
	print("no encontrado")
"""


