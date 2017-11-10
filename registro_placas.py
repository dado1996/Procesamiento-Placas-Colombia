from openalpr import Alpr
import sys
from argparse import ArgumentParser
import numpy as np
import cv2
import os
import atexit
from placa_dia import placa_dia
import file_json
from clean_exit import exit_handler

FILE = "registro_placas_3.txt"
DIR = "./placas_2/"

try:
	dic = file_json.get_json(FILE)
except:
	print "no se pudo cargar el diccionario"
	reg_plac = open(FILE,'w')
	dic = {}

dir_list = os.listdir(DIR)
dir_list.sort()

acier = 0
totl = 0

for dir_a in dir_list:
	files = dir_a 

	if files in dic:
		continue
	else:
		try:
			alpr = Alpr("co", "/usr/share/openalpr/config/openalpr.defaults.conf", "/home/ssi/openalpr/runtime_data")
			alpr.set_top_n(7)
			alpr.set_default_region("wa")
			alpr.set_detect_region(False)

			print "Registro de imagen "+files+"\n"
			img = cv2.imread(DIR + files)
			img_size = os.stat(DIR + files)
			a = 4
			if img_size.st_size < 1500000:
				a = 1

			cv2.namedWindow('imagen', cv2.WINDOW_NORMAL)
			cv2.resizeWindow('imagen', img.shape[1]/a, img.shape[0]/a)
			pos_us = 0
			pos_us = cv2.selectROI('imagen',img)
			jpeg_bytes = open(DIR + files, "rb").read()
			results = alpr.recognize_array(jpeg_bytes)
			# Uncomment to see the full results structure
			# import pprint
			# pprint.pprint(results)
			print("Image size: %dx%d" %(results['img_width'], results['img_height']))
			print("Processing Time: %f" % results['processing_time_ms'])

			if not results['results']:
				usr_plac = str(raw_input("Ingrese la placa en la imagen. Si no hay placa, ingrese 0:\n"))
				dic[files] = {'Placa_usuario':usr_plac.upper(),'Placa_sistema':0,'Pos_usuario':pos_us,'Pos_sistema':0}
			else:
				usr_plac = str(raw_input("Ingrese la placa en la imagen: \n"))


			for pos in results['results']:
				pos_sis = pos['coordinates']

			i= 0

			for plate in results['results']:
				placa_dia(i)   
				for candidate in plate['candidates']:
					prefix = "-"
					print("  %s %12s%12f" % (prefix, candidate['plate'], candidate['confidence']))

					es_val = None
					while es_val == None:
						es_val = str(raw_input("Coincide la placa con la imagen? (s=si/n=no): "))

						if es_val == 's':
							dic[files] = {'Placa_usuario':usr_plac.upper(),'Placa_sistema':candidate['plate'],'Pos_usuario':pos_us,'Pos_sistema':pos_sis}
						elif es_val == 'n':
							pass
						else:
							print "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
							es_val = None

					if es_val == 's':
						break

				if es_val == 'n':
					dic[files] = {'Placas_usuario':usr_plac.upper(),'Placa_sistema':0,'Pos_usuario':pos_us,'Pos_sistema':pos_sis}
				elif es_val == 's' and es_val != 'n':
					print "Soy ElRubiusOMG"
			
			
			cv2.destroyAllWindows()
		except KeyboardInterrupt:	
			file_json.dump_json(dic,FILE)
			sys.exit()
			
		finally:
			if alpr:
			    alpr.unload()

		file_json.dump_json(dic,FILE)

			
			
		print "\n\n"
print "Termino!!!!!!!!!!!!!!!!!!!"
