import sqlite3
from os import system

def main():
    id=0
    for i in range(0,8):
        id = id+1
        print("ingrese los datos del estudiante numero " + str(id))
        nombre = input("Ingrese en el nombre del estudiante ")
        apellido = input("Ingrese el apellido del estudiante ")

        registrar(id,nombre,apellido)
        system("cls")
  

    mostrar()

def registrar(id,nombre,apellido):
    con = sqlite3.connect('mibase.db')
    cursor = con .cursor()

    query = '''INSERT INTO usuarios(id,nombres,apellido) VALUES(?,?,?)'''
    rows= cursor.execute(query, (id, nombre, apellido))
    con.commit()
    cursor.close()
    con.close()

def mostrar():
    con = sqlite3.connect('mibase.db')
    cursor = con .cursor()
    rows = cursor.execute('SELECT * FROM usuarios')
    for row in rows:
        print(row)
    cursor.close()
    con.close()

if __name__ == '__main__':
    main()