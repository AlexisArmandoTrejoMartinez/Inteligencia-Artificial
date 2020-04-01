import json
animales = [0,0,0]
pdef = [0,0,0]
porc = [0,0,0]
clase = ""
c=0
with open('animales.json') as file:
	data = json.load(file)
print(data)
if not data:
	exit
nombre = input("Nombre del animal")

for d in data['defecto']:
	print(d['nombre'])
	if d['nombre'] == nombre.lower():
			print(d['nombre'])
			pdef[0] = d['Puntaje']['Ave']
			pdef[1] = d['Puntaje']['Reptil']
			pdef[2] = d['Puntaje']['Mamifero']
		
			index = pdef.index(max(pdef, key=int))
			max_item = max(pdef, key=int)
		
			if index == 0:
				animales[index] = animales[index] + max_item
			if index == 1:
				animales[index] = animales[index] + max_item
			if index == 2:
				animales[index] = animales[index] + max_item
  
for pregunta in data['Nodo']:
	print('Tiene o puede?')
	print(pregunta[1])
	R = input("")
	if R == 'S':
		animales[0] = animales[0] + int(pregunta[2]["Ave"])
		animales[1] = animales[1] + int(pregunta[2]["Reptil"])
		animales[2] = animales[2] + int(pregunta[2]["Mamifero"])
	index = animales.index(max(animales, key=int))
	max_item = max(animales, key=int)
	porc[0] = animales[0]
	for t in pregunta[2]:
		if index == c:
			clase = t
		c=c+1
	c=0
porc[0] = (animales[0]/(animales[0]+animales[1]+animales[2]) )*100
porc[1] = (animales[1]/(animales[0]+animales[1]+animales[2]) )*100
porc[2] = (animales[2]/(animales[0]+animales[1]+animales[2]) )*100
print("Es un"+" "+clase+" Con: "+str(max_item)+ " " "puntos") 
print("PUNTOS TOTALES \n Aves :"+str(animales[0])+"\nReptiles :"+str(animales[1])+"\nMamiferos :\n"+str(animales[2]))
print("PORCENTAJE TOTAL \n Aves :"+str(porc[0])+"\n Reptiles :"+str(porc[1])+"\nMamiferos :"+str(porc[2]))
	

"""#import json

data = {"Fruteria": [  {"Fruta":   [    {"Nombre":"Manzana","Cantidad":10},    {"Nombre":"Pera","Cantidad":20},    {"Nombre":"Naranja","Cantidad":30}   ]  },  {"Verdura":   [    {"Nombre":"Lechuga","Cantidad":80},    {"Nombre":"Tomate","Cantidad":15},    {"Nombre":"Pepino","Cantidad":50}   ]  } ]}

#encoded
data_string = json.dumps(data)

#Decoded
decoded = json.loads(data_string)

print ("Tenemos" +str(decoded["Fruteria"][1]["Verdura"][0]["Cantidad"])+" Lechugas.")
"""


