print("=== CALCULADORA DE DESCONTO ===")
produto = input("Nome do produto: ")
preco = float(input("Preço: R$ "))
desconto = float(input("Desconto (%): "))

valordesconto = preco * (desconto / 100)
precofinal = preco - valordesconto

print(f"\nProduto: {produto}")
print(f"Preço original: R$ {preco:.2f}")
print(f"Desconto: R$ {valordesconto:.2f}")
print(f"Preço final: R$ {precofinal:.2f}")
