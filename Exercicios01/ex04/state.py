import sys

def capitalCity():
    
    argumentos = sys.argv 

    estados = {
    "Oregon" : "OU",
    "Alabama": "AL",
    "Nova Jersey": "NJ",
    "Colorado" : "CO"
    }

    capitais_cidades = {
    "OU": "Salém",
    "AL": "Montgomery",
    "NJ": "Trenton",
    "CO": "Denver"
    }
    
    if len(argumentos)  != 2 :
        sys.exit()
    
    elif argumentos[1] in capitais_cidades.values():         
        for k,v in capitais_cidades.items():
            if(v == argumentos[1]):
                siglaEstado = k
                for estado,b in estados.items():
                    if(siglaEstado == b):
                        print(estado)
                        break
    else:
        print("Cidade desconhecida")   
                    

if __name__ == '__main__':  
    capitalCity()
