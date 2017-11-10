import numpy as np
import cv2
import os
import tkFileDialog
import glob
from file_json import get_json

dic = get_json()

ruta = "/home/ssi/Documentos/proyecto_python/placas/placas_2/"

dir_list = os.listdir(ruta)	

values = dic.values()

empty  = [0, 0, 0, 0]
show = False

files = dir_list
for file in files:
	print file
	folder,filename = os.path.split(file)
	if filename in dic:
		val =dic[filename]
		if not os.path.exists('/home/ssi/Documentos/proyecto_python/placas/cropped_plates/' + filename):
		
			temp =val['Pos_usuario']
			if temp != empty:	
				print file
				print temp
			
				img = cv2.imread('/home/ssi/Documentos/proyecto_python/placas/cropped_plates/' + file)
				if show:
					cv2.namedWindow('imagen', cv2.WINDOW_NORMAL)
					im = cv2.resizeWindow('imagen', img.shape[1]/4, img.shape[0]/4)
					cv2.imshow('imagen', img)
					cv2.waitKey(0)

				crop = img[temp[1]:temp[1]+temp[3], temp[0]:temp[0]+temp[2]]
				if show:
					cv2.imshow("Imagen recortada", crop)
					cv2.waitKey(0)
				cv2.imwrite('/home/ssi/Documentos/proyecto_python/placas/cropped_plates/' + filename[:-4] + '.png', crop)

