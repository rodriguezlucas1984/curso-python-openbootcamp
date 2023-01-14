def contar (desde,hasta):
    incremento=1;
    if desde==hasta:
        raise ValueError(str(desde)+" igual a " + str(hasta))
    if desde>hasta:
        incremento=-1;  
    
    while desde!=hasta+incremento:
        print(desde)
        desde+=incremento
    

def main ():
    contar(100,1)


if __name__=="__main__":
    main()

