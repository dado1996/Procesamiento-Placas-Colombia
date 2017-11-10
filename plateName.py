import os

for filename in os.listdir("./placas_2/"):
	if not 'IMG_' in filename:
		newName = "IMG_" + filename[:-4].replace("IMG_","")
		os.rename("./placas_2/"+filename, "./placas_2/"+newName+".png")
