from princ import Pessoa, Professor, Aluno, Disciplina

disciplina = Disciplina()

professor1 = Professor(str(input('Digite o nome do professor: ')), int(input('Digite a idade do professor: ')), str(input('Digite a matéria do professor')))

aluno1 = Aluno(str(input('Digite o nome do aluno: ')), int(input('Digite a idade do aluno: ')), int(input('Digite a matricula do aluno: ')))


disciplina.adicionar_aluno(professor1)
disciplina.adicionar_aluno(aluno1)

disciplina.listar_aluno()