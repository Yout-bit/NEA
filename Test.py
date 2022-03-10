from pygame.math import Vector2 
import numpy as np

def perpendicular( a ) :
    b = np.empty_like(a)
    b[0] = -a[1]
    b[1] = a[0]
    return b


def perp(a):
    b = Vector2(0,0)
    b.x = a.y
    b.y = a.x
    return b

def normalize(a):
    a = np.array(a)
    return a/np.linalg.norm(a)

if __name__ == "main__":   
    dir = Vector2(1,0) 
    a = [-1,0]
    print (type(perp(dir)))
    print (perpendicular(dir))

#126 080 080 999 999 S720560999999N
x = "126080080999999S720560999999N"
print(len(x))

playerlocs = []
for i in range(int(x[1])):
    playerlocs.append([int(x[3 + (13 * i):6 + (13 * i)]), int(x[6 + (13 * i):9 + (13 * i)]), x[15 + (13 * i)]])

print (playerlocs)
