# Faça um programa que peça uma nota de 0 a 10. 
# Mostre uma mensagem caso o valor seja inváldo
# e continue pedindo até que o usuário informe 
# um valor válido.


nota = 0

while nota <= 10:
    nota = int(input("Digite uma nota de 0 a 10: "))
else:
    print("Nota inválida")