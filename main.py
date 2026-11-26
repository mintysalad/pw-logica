alunos = ["Pedro", "João", "Ana", "Davi", "Lucas"]

print(alunos[2])

alunos.append("Erick")
print(alunos)
quantidade = len(alunos)
print(f"Temos {quantidade} alunos cadastrados.")

for aluno in alunos:
    print(f"Olá {aluno}!")

for contador in range(5):
    print(alunos[contador])