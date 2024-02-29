class Veiculo:
    def __init__(self, marca, modelo, ano, cor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor

    def detalhes(self):
        print("Marca: "+self.marca)
        print("Modelo: "+self.modelo)
        print("Ano: "+self.ano)
        print("Cor: "+self.cor)

class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, cor, numero_portas):
        super().__init__(marca, modelo, ano, cor)
        self.numero_portas = numero_portas


    def detalhes(self):
        print("Marca: "+self.marca)
        print("Modelo: "+self.modelo)
        print("Ano: "+str(self.ano))
        print("Cor: "+self.cor)
        print("Portas: "+str(self.numero_portas))

class Moto(Veiculo):
    def __init__(self,marca, modelo, ano, cor, cilindrada):
        super().__init__(marca,modelo, ano, cor)
        self.cilindrada = cilindrada

    def detalhes(self):

        print("Marca: "+self.marca)
        print("Modelo: "+self.modelo)
        print("Ano: "+str(self.ano))
        print("Cor: "+self.cor)
        print("Cilindrada: "+str(self.cilindrada))
        print("\n-------------------------------------------\n")


class Frota:
    def __init__(self):
        self.veiculos = []

    def adicionar_veiculo(self,veiculo):
        self.veiculos.append(veiculo)

    def listar_veiculo(self):
        for veiculo in self.veiculos:
            print(veiculo.detalhes())