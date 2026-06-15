class AdicionarLivros:
    def __init__(self, nome, data, doador):
        self.nome = nome
        self.data = data
        self.doador = doador

    def nomeLivro(self):
        self.nome = input("Qual o nome do livro? ")

    def dataDeAdicao(self):
        self.data = input("Qual a data de adição do novo livro? ")

    def quemDoou(self):
        self.doador = input("Quem foi o doador do novo livro? ")


class PegarEmprestado:
    def __init__(self, nome, quemPegou, data, devolvido):
        self.nome = nome
        self.quemPegou = quemPegou
        self.data = data
        self.devolvido = devolvido

    def nomeLivro(self):
        self.nome = input("Qual o nome do livro que você quer pegar? ")

    def emprestimo(self):
        self.quemPegou = input(f"Qual o nome de quem pegou o livro {self.nome}? ")

    def quandoPegou(self):
        self.data = input("Qual a data do emprestimo? ")


class Devolver:
    def __init__(self, nome, quemPegou):
        self.nome = nome
        self.quemPegou = quemPegou

    def devolvendo(self):
        self.nome = input("Qual o nome do livro que você pegou? ")

    def quempegou(self):
        self.quemPegou = input(f"Qual o nome de quem pegou o livro {self.nome}? ")
