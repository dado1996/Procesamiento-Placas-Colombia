from file_json import get_json
import os
import cv2

FILE = 'registro_placas_2.txt'
ROUTE = '/home/ssi/Documentos/proyecto_python/placas/placas_2/' 
DEST = '/home/ssi/Documentos/proyecto_python/placas/cropped_plates/'

json = get_json(FILE)
json_values = json.values()

for img_list in os.listdir(ROUTE):
	folder,filename = os.path.split(img_list)
	if filename in json:
		val = json[filename]
		values = val['Pos_usuario']

		if not os.path.exists(DEST + img_list):
			print filename
			print values
			img = cv2.imread(ROUTE + filename)
			crop = img[values[1]:values[1]+values[3],values[0]:values[0]+values[2]]
			cv2.imwrite(DEST + filename,crop)