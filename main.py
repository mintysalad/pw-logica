peso = float(input("Digite seu peso : "))
altura = float(input("Digite sua altura (ex: 1.70): "))

imc = peso / (altura * altura)

if imc < 18.5:
    print(f"Abaixo do peso: {imc}")

elif imc < 25:
    print(f"Peso normal: {imc}")

elif imc < 30:
    print(f"Acima do peso: {imc}")

else:
    print(f"Obesidade: {imc}" )