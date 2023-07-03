def main():
    paises = []
    paises.append(agregapais(paises))
    
    dato = "s"

    dato2=input("desea agregar otro pais: ")

    while dato == dato2:
        paises.append(agregapais(paises))

        dato2=input("desea agregar otro pais: ")

    orden = set(paises)
    
    print(sorted(orden))
     


def agregapais(paises):
    if paises == []:
        pais = input("Ingrese un pais: ")

        return pais
    else:
        pais = input("Ingrese otro pais: ")
        return pais


    
    

if __name__ == '__main__':
    main()