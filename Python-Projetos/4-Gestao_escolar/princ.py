class Pessoa:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade


    def apresentar(self):
        print("Nome: "+self.nome)
        print("Idade: "+self.idade)


class Professor(Pessoa):
    def __init__(self,nome, idade, materia):
        super().__init__(nome,idade)
        self.materia = materia

    def apresentar(self):
        print("Nome do professor: " + self.nome)
        print("Idade do professor: " + str(self.idade))
        print("Materia do professor: "+self.materia)


class Aluno(Pessoa):
    def __init__(self,nome, idade, matricula):
        super().__init__(nome, idade)
        self.matricula = matricula

    def apresentar(self):
        print("\n-------------------------------------------\n")
        print("Nome do aluno: " + self.nome)
        print("Idade do aluno: " + str(self.idade))
        print("Materia do aluno: "+ str(self.matricula))


class Disciplina:
    def __init__(self, nome_disciplina = None, professor = None):
        self.nome_disciplina = nome_disciplina
        self.professor = professor
        self.alunos = []

    def adicionar_aluno(self,aluno):
        self.alunos.append(aluno)

    def listar_aluno(self):
        for aluno in self.alunos:
            print(aluno.apresentar())
