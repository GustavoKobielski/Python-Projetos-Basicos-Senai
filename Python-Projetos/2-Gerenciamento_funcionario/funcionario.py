class Funcionario():

    def __init__(self,nome, idade, salario):
        self.nome = nome
        self.idade = idade
        self.salario = salario

    def mostrar_info(self):
        print("Nome:", self.nome)
        print("Idade: ", self.idade)
        print("Salario: ", self.salario)


class Diretor(Funcionario):

    def __init__(self, nome, idade, salario, acoes):
        Funcionario.__init__(self, nome, idade, salario)
        self.acoes = acoes

    def calcular_salario(self):
        self.salario += self.acoes
        return self.salario

    def mostrar_info(self):
        print("Nome:", self.nome)
        print("Idade: ", self.idade)
        print("Salario: ", self.calcular_salario())

class Gerente(Funcionario):
    def __init__(self, nome, idade, salario, bonus):
        Funcionario.__init__(self, nome, idade,salario)
        self.bonus = bonus

    def calcular_salario(self):
        self.salario += self.bonus
        return self.salario

    def mostrar_info(self):
        print("Nome:",self.nome)
        print("Idade: ",self.idade)
        print("Salario: ",self.calcular_salario())

