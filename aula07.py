notas = [""]*5
soma=0
cont=0
for x in range(len(notas)):
    notas[x] = float(input("Digite suas notas: "))
for y in range(len(notas)):
    soma+=notas[y]
media = soma / len(notas)
for i in range(len(notas)):
    if notas[i]> media:
        cont+=1
print(cont)