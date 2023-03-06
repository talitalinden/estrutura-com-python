#Faça um programa que leia um nome de usuário e a sua senha e não 
#aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações. 

usuario = "igual"
senha = "igual"

while (usuario == senha):
    print("Usuário e senha não podem ser iguais.")
    usuario = str(input("Digite o nome de usuário: "))
    senha = str(input("Digite sua senha com letras: "))

print("Está correto.")