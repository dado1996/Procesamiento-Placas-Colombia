from file_json import get_json

dic = get_json()

img_name = dic.keys()

placas = []
posiciones = []
placas_us = []
posiciones_us = []
values = dic.values()

for val in values:
	placas.append(val['Placa_sistema'])
	posiciones.append(val['Pos_sistema'])
	placas_us.append(val['Placa_usuario'])
	posiciones_us.append(val['Pos_usuario'])

#print ("Imagen\t\t\t|Placa\t|\tPosicion\t\t")
#print "-----------------------------------------------------------"
#for val in range(len(img_name)):
#	print str(img_name[val]) + "\t|" + str(placas[val]) + "\t|" + str(posiciones[val])
