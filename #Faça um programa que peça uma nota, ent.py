#Faça um programa que peça uma nota, entre zero e dez. Mostre a mensagem caso 
# o valor seja inválido e continue pedindo até que o usuário informe um valor
#válido.

notas = int(input("São quantas notas? "))
aluno = input("Digite o nome do aluno: ")

count = 1; soma = 0.0

while count <= notas:
    print("Nota do aluno ", count, ":")
    nota = float(input())
    if nota >= 0 and nota <= 10:
        print("--------------")
        soma += nota
        count += 1
    else:
        print("Nota errada ", nota, ":")
        print("Digite novamente a nota do aluno: ", count, ":")
        nota = float(input())
        soma += nota
        count += 1

print("Média do aluno: ", aluno, "-", (soma/notas))