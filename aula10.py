vetor = [0, 0, 0, 0, 0]
for x in range(5):
    vetor[i] = int(input(f"Digite o {x+1}º número: "))
print("Números na ordem inversa:")
for x in range(4, -1, -1):
    print(vetor[x])
