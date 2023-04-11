class Aluno:
    def __init__(self, nome, nota1, nota2):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
        self.media = 0.0

    def calcular_media(self):
        self.media = (self.nota1 + self.nota2) / 2
        return self.media

    def mostra_dados(self):
        print(f'Nome: {self.nome}')
        print(f'Nota 1: {self.nota1}')
        print(f'Nota 2: {self.nota2}')
        print(f'Média: {self.media}')

    def resultado(self):
        if self.media >= 7:
            print ("Aprovada (o)")
        else:
            print("Reprovada (o)")

aluno1 = Aluno('Carol', 9.0, 8.7)
aluno2 = Aluno('Paula', 9.0, 8.5)
aluno3 = Aluno('Clara', 9.0, 9.0)

aluno2.calcular_media()
aluno2.mostra_dados()
aluno2.resultado() 