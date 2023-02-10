import sys
def capitalCity(estado):
    
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
    "O QUÊ": "Denver"
    }

    for chave in estados.keys():
        if(estado == chave):
            siglaEstado = estados[estado] 
            for cidade in capitais_cidades.keys():
                if(siglaEstado == cidade):
                    print(capitais_cidades[cidade])
        else:
            print("Estado desconhecido")
        break
        

if __name__ == '__main__':  
    capitalCity("Oregon")
