# Lista de 5 nomes

nomes = []

for i in range(5):
    nome = input(f"Digite o {i+1}º nome: ")
    nomes.append(nome)

print("\nLista de nomes:")
for nome in nomes:
    print(nome)
