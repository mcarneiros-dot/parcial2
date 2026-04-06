# Juros simples

capital = float(input("Digite o capital: "))
taxa = float(input("Digite a taxa (ex: 0.05 para 5%): "))
tempo = float(input("Digite o tempo: "))

juros = capital * taxa * tempo
montante = capital + juros

print("Juros:", juros)
print("Montante:", montante)
