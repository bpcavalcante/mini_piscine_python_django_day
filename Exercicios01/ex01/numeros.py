def printArquivo():
    arquivo = open('numbers.txt', 'r')

    for linha in arquivo:
        conteudo = linha.split(',')
        for i in conteudo:
            print(i)

if __name__ == '__main__':      
    printArquivo()