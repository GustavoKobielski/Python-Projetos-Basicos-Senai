class Material:
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao


    def detalhes(self):
        print("\n-------------------------------------------")
        print("Titulo: " + self.titulo)
        print("Autor: " + self.autor)
        print("Ano Publicacao: " + str(self.ano_publicacao))
class Livro(Material):
    def __init__(self,titulo, autor, ano_publicacao,isbn):
        super().__init__(titulo, autor,ano_publicacao)
        self.isbn = isbn

    def detalhes(self):

        print("Titulo: " + self.titulo)
        print("Autor: " + str(self.autor))
        print("Ano Publicacao: " + str(self.ano_publicacao))
        print("ISBN:",self.isbn)

class Revista(Material):
    def __init__(self, titulo, autor, ano_publicacao,edicao):
        super().__init__(titulo, autor, ano_publicacao)
        self.edicao = edicao

    def detalhes(self):
        print("\n-------------------------------------------")
        print("Titulo: " + self.titulo)
        print("Autor: " + str(self.autor))
        print("Ano Publicacao: " + str(self.ano_publicacao))
        print("Edição da revista: ",self.edicao)



class Biblioteca:
    def __init__(self):
        self.materials = []

    def adicionarMaterial(self,material):
        self.materials.append(material)

    def listarMaterial(self):
        for material in self.materials:
            print(material.detalhes())

    def buscar_por_autor(self, autor):
        return [material for material in self.materials if material.autor == autor]

    def buscar_por_ano(self, ano):
        return [material for material in self.materials if material.ano_publicacao == ano]

biblioteca = Biblioteca()

livro1 = Livro("O Pequeno Príncipe", "Antoine de Saint-Exupéry", 1943, "978-3-16-148410-0")
revista1 = Revista("Science", "Edição 1", 2022, 1)
revista2 = Revista("Science", "Edição 2", 2022, 2)

biblioteca.adicionarMaterial(livro1)
biblioteca.adicionarMaterial(revista1)
biblioteca.adicionarMaterial(revista2)

biblioteca.listarMaterial()

materiais_autor = biblioteca.buscar_por_autor("Antoine de Saint-Exupéry")
for material in materiais_autor:
    print("\n-------------------------------------------")
    print("Livros encontrado pelo autor!")
    print("-------------------------------------------")
    print(material.detalhes())

materiais_ano = biblioteca.buscar_por_ano(2022)
for material in materiais_ano:
    print("\n-------------------------------------------")
    print("Livros encontrado pelo ano!")
    print("-------------------------------------------")
    print(material.detalhes())