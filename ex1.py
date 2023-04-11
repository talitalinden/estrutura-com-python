# Faça um programa para leitura de três notas parciais de 
# um aluno e sua disciplina. O programa deve calcular
# a média alcançada por aluno e apresentar:

disc = input("Digite a disciplina: ")
nota1 = float(input("Digite a sua primeira nota: "))
nota2 = float(input("Digite a sua segunda nota: "))
nota3 = float(input("Digite a sua terceira nota: "))
media = (nota1 + nota2 + nota3)/3

print("Sua média é: " , media)

if media >= 7:
    print ("Aprovado")
elif media <= 4:
    print ("Reprovado")
else:
    print ("Você está na final")