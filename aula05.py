nomes = [""]*5
for x in range(len(nomes)):
    nomes[x] = str(input("Digite um nome: "))
    for y in range(len(nomes)):
        print(f"{nomes[y]} esta na posicao {y}")