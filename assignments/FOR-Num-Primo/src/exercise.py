import os
def main():
#==================================================================
    os.system('clear')

    num = int(input("Dame el número que deseas analizar:"))
    bandera = True

    for x in range(2,num):
        
        if (num % x == 0):
            bandera = False

    if bandera == True:
        print('El número '+str(num)+' SI es número primo')
    else:
        print('El número '+str(num)+' NO es número primo')
    
#==================================================================
if __name__=='__main__':
    main()
