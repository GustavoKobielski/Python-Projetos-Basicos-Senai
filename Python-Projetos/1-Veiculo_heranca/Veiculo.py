class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, numero_portas):
        Veiculo.__init__(self, marca, modelo, ano, )
        self.numero_portas = numero_portas

class Moto(Veiculo):
    def __init__(self, marca, modelo, ano, cilindrada):
        Veiculo.__init__(self, marca, modelo, ano)
        self.cilindrada = cilindrada

def imprimir_veiculo(veiculo):
    print(veiculo.marca, veiculo.modelo, veiculo.ano)

carro = Carro(str(input("Diga a marca do carro:")), str(input("Diga o modelo do carro: ")), int(input("Diga o ano do carro: ")), int(input("Diga quantas portas tem: ")))
#carro = Carro("Toyota", "Corolla", 2020, 4)
moto = Moto(str(input("Diga a marca do moto:")), str(input("Diga o modelo da moto: ")), int(input("Diga o ano da moto: ")), int(input("Diga quantas cilindradas tem: ")))
#moto = Moto("Honda", "CBR600RR", 2019, 599)

imprimir_veiculo(carro)
imprimir_veiculo(moto)