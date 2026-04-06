# Conversão de tempo

print("1 - Segundos para h/m/s")
print("2 - h/m/s para segundos")

opcao = input("Escolha a opção: ")

if opcao == "1":
    total_segundos = int(input("Digite os segundos: "))

    horas = total_segundos // 3600
    minutos = (total_segundos % 3600) // 60
    segundos = total_segundos % 60

    print(f"{horas}h {minutos}m {segundos}s")

elif opcao == "2":
    horas = int(input("Horas: "))
    minutos = int(input("Minutos: "))
    segundos = int(input("Segundos: "))

    total = horas * 3600 + minutos * 60 + segundos

    print("Total em segundos:", total)

else:
    print("Opção inválida!")
