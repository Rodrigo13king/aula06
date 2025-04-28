nomes = ["Joao","Carlos","Ana","Maria","Pitomba"]
nome = str(input("Digite um nome: "))
for x in range(len(nomes)):
    if nome == nomes[x]:
        print(f"o nome {nomes[x]} esta na posicao {x}")
