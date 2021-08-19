import os
def main():
    #escribe tu código abajo de esta línea

    os.system('clear')

    angulo = int(input("Angulo en grados del triangulo:"))

    if angulo < 90:
        print("Agudo")
    elif angulo == 90:
        print("Recto")
    elif (angulo > 90) and (angulo < 180):
        print("Obtuso")
    elif angulo == 180:
        print("Llano")
    else:
        print("Concavo")

if __name__=='__main__':
    main()
