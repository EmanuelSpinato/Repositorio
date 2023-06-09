alunos = []

while True:

    nome = input("Digite o nome do aluno: ")
    if nome == "":
        break
    g1 = float(input("Digite a nota da G1: "))
    g2 = float(input("Digite a nota da G2: "))
    aluno = {
        "nome": nome,
        "g1": g1,
        "g2": g2
    }
    alunos.append(aluno)
print(alunos)

count = 0
for aluno in alunos:
    media = (aluno['g1'] + aluno['g2']) / 2
    if media >= 7.0:
        count += 1
print("Numero de alunos aprovados", count)

count = 0
for aluno in alunos:
    media = (aluno['g1'] + aluno['g2']) / 2
    if media < 7.0:
        count += 1
print("Numero de alunos Reprovados", count)

# Abaixo da media na g1
count = 0
for aluno in alunos:
    if aluno['g1'] < 7.0:
        count += 1
print("Alunos abaixo da media na G1", count)

# Acima da media na g1
count = 0
for aluno in alunos:
    if aluno['g1'] >= 7.0:
        count += 1
print("Alunos acimna da media na G1", count)

# Abaixo da media na g2
count = 0
for aluno in alunos:
    if aluno['g2'] < 7.0:
        count += 1
print("Alunos abaixo da media na G2", count)

# Acima da media na g2
count = 0
for aluno in alunos:
    if aluno['g2'] >= 7.0:
        count += 1
print("Alunos acima da media na G2", count)

# acima da media no semestre
count = 0
for aluno in alunos:
    media = (aluno['g1'] + aluno['g2']) / 2
    if media >= 7.0:
        count += 1
print("Alunos acima da media no semestre", count)

# abaixo da media no semestre
count = 0
for aluno in alunos:
    media = (aluno['g1'] + aluno['g2']) / 2
    if media < 7.0:
        count += 1
print("Alunos acima da media no semestre", count)

# Media da turma na G1
if len(alunos) > 0:
    soma = 0.0
    for aluno in alunos:
        soma += aluno['g1']
        resultadoG1 = soma / len(alunos)
    print("Media da turma na G1", resultadoG1)

# Media da turma na G2
if len(alunos) > 0:
    soma = 0.0
    for aluno in alunos:
        soma += aluno['g2']
        resultadoG2 = soma / len(alunos)
    print("Media da turma na G2", resultadoG2)

# Media da turma no semestre
    if len(alunos) > 0:
        soma = 0.0
    for aluno in alunos:
        media = (aluno['g1'] + aluno['g2']) / 2
    print("Media da turma no semestre", media)

# Maior e menor nota G1
notas_g1 = []
for aluno in alunos:
    notas_g1.append(aluno['g1'])
notas_g1.sort()
print(f'menor:{notas_g1[0]} - maior:{notas_g1[len(notas_g1) - 1]}')

# Maior e menor nota G2
notas_g2 = []
for aluno in alunos:
    notas_g2.append(aluno['g2'])
notas_g2.sort()
print(f'menor:{notas_g2[0]} - maior:{notas_g2[len(notas_g2) - 1]}')

# Maior e menor nota do semestre
for aluno in alunos:
    if notas_g1[len(notas_g1) - 1] >= notas_g2[len(notas_g2) - 1]:
        print("Maior nota da turma: ", notas_g1[len(notas_g1) - 1])
    else:
        print("Maior nota da turma: ", notas_g2[len(notas_g2) - 1])

    if notas_g1[0] <= notas_g2[0]:
        print("Menor nota da turma: ", notas_g1[0])
    else:
        print("Menor nota da turma: ", notas_g2[0])

MyName = input("Digite seu nome: ")
for aluno in alunos:
    if aluno['g1'] == MyName:
        print(aluno)
    if aluno['g2'] == MyName:
        print(aluno)

alunos.clear
exit
