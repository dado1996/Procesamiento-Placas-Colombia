import json

def dump_json(dic,FILE):
	reg_plac = open(FILE,'w')
	str1 = json.dumps(dic, sort_keys=True,indent=4, separators=(',', ': '))
	reg_plac.write(str1)
	reg_plac.close()


def get_json(FILE):
	reg_plac = open(FILE,'r')
	json_info = reg_plac.read()
	dic = json.loads(json_info)
	reg_plac.close()
	return dic
