def verificar(pais, paises):
    
    for i in range(0 , len(paises)):
        if pais == paises[i]:
            pais = input("ese pais ya esta registrado, ingrese otro: ")
            return verificar(pais,paises)
    return pais