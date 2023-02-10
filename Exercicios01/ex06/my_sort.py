import sys

def mysort():

	musicos = { 
		"Hendrix": "1942",
		"Allman": "1946",
		"Rei": "1925",
		"Clapton": "1945",
		"Johnson": "1911",
		"Berry": "1926",
		"Vaughan": "1954",
		"Cooder": "1947",
		"Página": "1944",
		"Richards": "1943",
		"Hammett": "1962",
		"Cobain": "1967",
		"Garcia": "1942",
		"Beck": "1944",
		"Santana": "1947",
		"Ramone": "1948",
		"Branco": "1975",
		"Rustling": "1970",
		"Thompson": "1949",
		"Burton": "1939"
	}

	musicoOrdenados = dict(sorted(musicos.items(), key=lambda x: (x[1], x[0])))

	for k in musicoOrdenados.keys():
		print(k)
	

if __name__ == '__main__':  
    mysort()
	


