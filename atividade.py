


lista = []
def manipulando(caminho):
   with open(caminho,"r",encoding="utf-8") as arquivo:
    texto = arquivo.read()
    palavras = texto.split()
    contador = 0
    contador1 = 0    
    contar = 0
    for palavra in palavras:
        if palavra == ',':
            continue
        else:
            contar = contar + 1
            
    print("Quantidade:" , contar)
    
    for x in palavras:
            lista.append(len(palavras[contador]))
            contador += 1
            contador1 += 1
            
            if len(lista) > 5:
                lista.remove(min(lista))

    lista.sort(reverse=True)
    print("As maiores palavras tem respectivamente:" )
    for i in lista:
        print("Letra(s):", i)

    qtdA = 0
    qtdE = 0
    qtdI = 0
    qtdO = 0
    qtdU = 0

    for caracter in palavras:
                if "a" in caracter.lower():
                    qtdA= qtdA + 1
                elif "e" in caracter.lower():
                    qtdE = qtdE + 1
                   
                elif "i" in caracter.lower():
                    qtdI+=1
                    qtdI = qtdI + qtdI
                elif "o" in caracter.lower():
                    qtdO+=1
                    qtdO = qtdO + qtdO
                elif "u" in caracter.lower():
                    qtdU+=1
                    qtdU = qtdU + qtdU
    
    if qtdA > qtdE and qtdA > qtdI and qtdA > qtdO and qtdA > qtdU:
       print("Letra que mais aparece é a Letra: A")
    if qtdE > qtdA and qtdE > qtdI and qtdE > qtdO and qtdE > qtdU:
        print("Letra que mais aparece é a Letra:E")
    if qtdI > qtdA and qtdI > qtdE and qtdI > qtdO and qtdI > qtdU:
         print("Letra que mais aparece é a Letra:I")
    if qtdO > qtdA and qtdO > qtdE and qtdO > qtdI and qtdO > qtdU:
         print("Letra que mais aparece é a Letra:O")
    elif qtdU > qtdA and qtdU > qtdE and qtdU > qtdI and qtdU > qtdO:
        print("Letra que mais aparece é a Letra:U")
        
    def linha(pafh):
        with open(pafh,encoding="utf-8") as file:
            newdata = file.readlines()
            linhas = 0
            for x in newdata:
                try:
                    index = newdata[linhas].index("ção")
                    print(f"ção aparece na {linhas + 1} linha")
                    break

                except:
                    linhas += 1
                    pass
    linha("arquivos.txt")        

manipulando("arquivos.txt")




