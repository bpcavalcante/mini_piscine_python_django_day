import sys

def capitalCity():
    
    estados = {
    "Oregon" : "OU",
    "Alabama": "AL",
    "New Jersey": "NJ",
    "Colorado" : "CO"
    }

    capitais_cidades = {
    "OU": "Salém",
    "AL": "Montgomery",
    "NJ": "Trenton",
    "CO": "Denver"
    }

    
    listArgumentos = sys.argv
    print(listArgumentos)
    if len(listArgumentos) != 2:
        sys.exit()        
          
    argumentos = listArgumentos[1].split(',')
    

    for arg in argumentos:
        print(arg.title())
        arg = arg.title().strip()
        if arg in capitais_cidades.values() or arg in estados.keys():
            for k,v in capitais_cidades.items():
                if(v == arg):
                    print(arg)
                    siglaEstado = k
                    for a,b in estados.items():
                        if(siglaEstado == b):
                            print(arg, "é capital de " , a)
            for k,v in estados.items():
                if(k == arg):
                    siglaCapitais = v
                    for a,b in capitais_cidades.items():
                        if(siglaCapitais == a):
                            print(arg, "é o estado de " ,b)
        else:
            print(arg, "não é uma capital nem um estado")                       
                        


if __name__ == '__main__':  
    capitalCity()


        

    
