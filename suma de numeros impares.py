from functools import reduce

def main():
    lista = list(range(50))
    impares= listimpar(lista)
    sumadeimpares(impares)

def listimpar(lista):
    impar = list(filter((lambda x: x % 2), lista))
    return impar

def sumadeimpares(impares):
    resultado = reduce((lambda x, y: x + y), impares) 
    print(resultado)



if __name__ == '__main__':
    main()
