def main():
    lista=[
    'Muy buenas.\n'
    'Esto crea.\n'
    'Un archivo.\n'
    ]
    crear('texto.txt', lista)
    escribir('texto.txt', lista)
    datos = leer('texto.txt', lista)



def crear(archivo, info):
    f = open(archivo, 'w')

    for linea in info:
        f.write(linea)

    f.close

def escribir(archivo, info):
    f = open(archivo, 'a')
    f.write('Y agrega nuevo contenido.\n')

def leer(archivo, info):
    f= open(archivo, 'r')
    contenido = f.readlines()
    f.close 
    lineas= []
    for linea in contenido:
        print(linea)
        
        
        
  

if __name__ == '__main__':
    main()
