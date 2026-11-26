# lista -> [] - permite alterações
# tupla -> () - não permite alterações
# dicionário -> {}

alunos = {
    "Pedro": 5,
    "Maria": 9,
    "Vicenzo": 8,
    "Ana":6
}

for nome, nota in alunos.items():
    if nota >= 7:
        print(f"{nome} está aprovado!")
    else:
        print(f"{nome} está reprovado!")