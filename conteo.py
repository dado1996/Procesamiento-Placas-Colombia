import file_json
from intersection_over_union import bb_intersection_over_union

dic = file_json.get_json()

values = dic.values()
placas_encontradas = 0
placas_acertadas = 0
posicion_encontrada = 0
posicion_acertada = 0
total_placas = 0

for name in values:
	temp1 = name['Pos_usuario']
	temp2 = name['Pos_sistema']
	
	if name['Pos_sistema'] == 0:
		continue
	else:
		a = [temp1[1],temp1[1] + temp1[3], temp1[0], temp1[0] + temp1[2]]
		b = [temp2[0]['y'],temp2[2]['y'],temp2[0]['x'],temp2[2]['x']]
		if name['Placa_usuario'].upper() == name['Placa_sistema']:
			placas_acertadas = placas_acertadas + 1
		porc = bb_intersection_over_union(a,b)
		if porc >= 0.6:
			posicion_acertada = posicion_acertada + 1
		total_placas = total_placas + 1

print "Posiciones acertadas: " + str(posicion_acertada)
print "Placas acertadas: " + str(placas_acertadas)
print "Porcentaje de aciertos: " + str((float(placas_acertadas)/float(posicion_acertada))*100) + "%"
print "Total placas: " + str(total_placas)
print "Posiciones acertadas sobre total placas: " + str((float(posicion_acertada)/float(total_placas))*100) + "%"
