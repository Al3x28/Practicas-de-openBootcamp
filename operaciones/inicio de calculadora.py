import operaciones as op

def main():
    suma1 = op.Suma(2,6)
    print(suma1)

    resta1 = op.Resta(3,5)
    print(resta1)

    multiplicar1 = op.Multiplicar(2,4)
    print(multiplicar1)

    dividir1 = op.Dividir(4,2)
    print(int(dividir1))

if __name__ == '__main__':
    main()