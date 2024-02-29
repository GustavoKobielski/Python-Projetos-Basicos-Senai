from veiculo import Veiculo, Carro, Moto, Frota

frota = Frota()

carro1 = Carro(str(input('Digite a marca do carro: ')), str(input('Digite o modelo do carro: ')), int(input('Digite o ano do carro: ')), str(input("Digite a cor do carro: ")), int(input("Digite quantas portas o carro tem: ")))
print("\n-------------------------------------------")
moto1 = Moto(str(input('Digite a marca da moto: ')), str(input('Digite o modelo da moto: ')), int(input('Digite o ano da moto: ')), str(input("Digite a cor da moto: ")), int(input("Digite quantas cilindradas a moto tem: ")) )

print("\n-------------------------------------------")
frota.adicionar_veiculo(moto1)
frota.adicionar_veiculo(carro1)

frota.listar_veiculo()