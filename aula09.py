numeros = [""] * 5
for x in range(5):
    numeros[x] = int(input(f"Digite o {x+1}º número: "))
print("Números na ordem inversa:")
for x in range(4, -1, -1):
    print(numeros[x], end=" ")



    