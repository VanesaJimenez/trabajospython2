# coding: utf8
    
def GetTablero():
    global a
    template = (" "+str(a[0])+" │ "+str(a[1])+" │ "+str(a[2])+" \n───┼───┼───\n "+str(a[3])+" │ "+str(a[4])+" │ "+str(a[5])+" \n───┼───┼───\n "+str(a[6])+" │ "+str(a[7])+" │ "+str(a[8])+" ")
    return template

def JuegoContinua():
    global msg
    if msg==("Felicidades X as ganado. weeee"):
        return False
    elif msg==("Felicidades O as ganado. weeee"):
        return False
    elif msg==("Juego empatado. :("):
        return False
    else:
        return True

def IntentarTirada(casilla):
    global x,a
    if casilla>9 or casilla<1:
        return('La tirada debe de estar entre 1 y 9')
    elif a[casilla-1]=='X' or a[casilla-1]=='O':
        return ('La casilla ya esta ocupada')
    else:
        if x%2==0:
            a[casilla-1]='X'
        else:
            a[casilla-1]='O'
        x+=1
        if a[0]=='X' and a[1]=='X' and a[2]=='X':
            return ("Felicidades X as ganado. weeee")
        elif a[3]=='X' and a[4]=='X' and a[5]=='X':
            return ("Felicidades X as ganado. weeee")
        elif a[6]=='X' and a[7]=='X' and a[8]=='X':
            return ("Felicidades X as ganado. weeee")
        elif a[0]=='X' and a[3]=='X' and a[6]=='X':
            return ("Felicidades X as ganado. weeee")
        elif a[1]=='X' and a[4]=='X' and a[7]=='X':
            return ("Felicidades X as ganado. weeee")
        elif a[2]=='X' and a[5]=='X' and a[8]=='X':
            return ("Felicidades X as ganado. weeee")
        elif a[0]=='X' and a[4]=='X' and a[8]=='X':
            return ("Felicidades X as ganado. weeee")
        elif a[2]=='X' and a[4]=='X' and a[6]=='X':
            return ("Felicidades X as ganado. weeee")
        elif a[0]=='O' and a[1]=='O' and a[2]=='O':
            return ("Felicidades O as ganado. weeee")
        elif a[3]=='O' and a[4]=='O' and a[5]=='O':
            return ("Felicidades O as ganado. weeee")
        elif a[6]=='O' and a[7]=='O' and a[8]=='O':
            return ("Felicidades O as ganado. weeee")
        elif a[0]=='O' and a[3]=='O' and a[6]=='O':
            return ("Felicidades O as ganado. weeee")
        elif a[1]=='O' and a[4]=='O' and a[7]=='O':
            return ("Felicidades O as ganado. weeee")
        elif a[2]=='O' and a[5]=='O' and a[8]=='O':
            return ("Felicidades O as ganado. weeee")
        elif a[0]=='O' and a[4]=='O' and a[8]=='O':
            return ("Felicidades O as ganado. weeee")
        elif a[2]=='O' and a[4]=='O' and a[6]=='O':
            return ("Felicidades O as ganado. weeee")
        elif a[0]!=1 and a[1]!=2 and a[2]!=3 and a[3]!=4 and a[4]!=5 and a[5]!=6 and a[6]!=7 and a[7]!=8 and a[8]!=9:
            return ("Juego empatado. :(")
        else:
            return ("")
    
def IniciaJuego():
    global x,casilla,a,msg
    x=0
    casilla=0
    msg = ""
    a=[1,2,3,4,5,6,7,8,9]
    return x, casilla, msg, a

if __name__ == '__main__':
    global casilla,msg
    IniciaJuego() 
    while(JuegoContinua()):
        print(GetTablero())
        casilla = int(input("Escoge una casilla: "))
        msg = IntentarTirada(casilla)
        if msg != "":
            print(msg)
        
            
        

