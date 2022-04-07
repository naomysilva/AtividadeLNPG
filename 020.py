
import math




while True:
    a = float(input(""))
    if a  == 0:
        break
    else:
        
        b = float(input(""))
        c = float(input(""))
    
    delta = (b**2) - 4 * a * c
    print(delta)
    
    if delta < 0:
        print("Não Possui raizes")
        
    elif delta == 0:
        print(delta)
    elif delta > 0:
        raiz = math.sqrt(delta)
        x1 = (-b + raiz) / 2 * a
        x2 = (- b - raiz) / 2 * a
        print("raiz x1:", x1, "raiz x2:", x2)
        

        
    
