# esta kata la tome prestada de ricky XD 
"""
    Any live cell with fewer than two live neighbours dies, as if caused by under-population.
    Any live cell with two or three live neighbours lives on to the next generation.
    Any live cell with more than three live neighbours dies, as if by overcrowding.
    Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
"""


def NextOfspring(u):
    changes = []
    h = int(u[0])
    w = int(u[1])
    for xxxx in range (0, h*w):
        changes.append(" ")
    u = list(u[2:])
    for x in range (0, h*w):
        alive = []
        if x == h*w-w:
            if u[x+1] == "*":
                alive.append(x+1)
            for y in range (x-w, x-w+2):
                if u[y] == "*":
                    alive.append(y)
        elif x == w-1:
            if u[x-1] == "*":
                alive.append(x-1)
            for y in range (x+w-1, x+w+1):
                if u[y] == "*":
                    alive.append(y)
        elif x == 0:
            if u[x+1] == "*":
                alive.append(x+1)
            for y in range (x+w, x+w+2):
                if u[y] == "*":
                    alive.append(y)
        elif x == h*w-1:
            if u[x-1] == "*":
                alive.append(x-1)
            for y in range (x-w-1, x-w+1):
                if u[y] == "*":
                    alive.append(y)
        #ya se acaban kas esquinas
        elif x % w == 0:
            for y in range (x-w, x-w+2):
                if u[y] == "*":
                    alive.append(y)
            for z in range (x+w, x+w+2):
                if u[z] == "*":
                    alive.append(z)
            if u[x+1] == "*":
                alive.append(x+1)
        elif (x+1) % w == 0:
            for y in range (x-w-1, x-w+1):
                if u[y] == "*":
                    alive.append(y)
            for z in range (x+w-1, x+w+1):
                if u[z] == "*":
                    alive.append(z)
            if u[x-1] == "*":
                alive.append(x-1)
        elif x < w:
            for y in range (x+w-1, x+w+2):
                if u[y] == "*":
                    alive.append(y)
            if u[x-1] == "*":
                alive.append(x-1)
            if u[x+1] == "*":
                alive.append(x+1)
        elif x >= h*w-w:
            for y in range (x-w-1, x-w+2):
                if u[y] == "*":
                    alive.append(y)
            if u[x-1] == "*":
                alive.append(x-1)
            if u[x+1] == "*":
                alive.append(x+1)
        else:
            for y in range (x-w-1, x-w+2):
                if u[y] == "*":
                    alive.append(y)
            for z in range (x+w-1, x+w+2):
                if u[z] == "*":
                    alive.append(z)
            if u[x-1] == "*":
                alive.append(x-1)
            if u[x+1] == "*":
                alive.append(x+1)
        if u[x] == "." and len(alive) == 3:
            changes[x] = "*"
        elif u[x] == "*":
            if len(alive)<2 or len(alive)>3:
                changes[x] = "."
    for zzz in range (0, h*w):
        if changes[zzz]!=" ":
            u[zzz] = changes[zzz]
    u.insert(0,w)
    u.insert(0,h)
    return(u)

    """
        Esta funcion recibe un universo y regresa la siguiente generacion segun las reglas
        Nota: La funcion recibe la cadena el el formato establecido y lo regresa en el mismo formato
    """
    raise NotImplementedError

def GetUniverse(u):
    h = int(u[0])
    w = int(u[1])
    u = list(u[2:])
    for x in range (0, h):
        u.insert((x+1)*w+x, "\n")
    return "".join(u)
    raise NotImplementedError

if __name__ == '__main__':
    print("Captura un universo (Linea por linea segun el formato y vacio para terminar)")
    u = ""
    line = input()
    while(line != ""):
        u += line
        line = input()
    option = input("Teclee n para ver la siguiente generacion y s para deter la simulacion")
    while(option == "n"):
        u = NextOfspring(u)
        print(GetUniverse(u))
        option = input()
    
