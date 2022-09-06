class Computador_de_bordo:

    consumo_total = 0
    quilometragem_total = 0
    tempo_de_viagem = 0  # em minutos
    consumo_medio = 0  # calculado
    velocidade_media = 0  # calculado


    def __init__(self):
        self.consumo_total = int(input("\nDigite o consumo total: "))
        self.quilometragem_total = int(input("\nDigite a quilometragem total: "))
        self.tempo_de_viagem = int(input("\nDigite o tempo de viagem em minutos: "))
        self.consumo_medio = int(input("\nDigite o consumo médio do veículo: "))
        self.velocidade_media = int(input("\nDigite a velocidade média: "))

    def __repr__(self):
        return (
                "\nConsumo total: " + str(self.consumo_total) +
                "\nQuilometragem: " + str(self.quilometragem_total) +
                "\nTempo de viagem: " + str(self.tempo_de_viagem) +
                "\nConsumo médio: " + str(self.consumo_medio) +
                "\nVelocidade média: " + str(self.velocidade_media))

    def calcular_consumo_medio(self):
        self.consumo_medio = self.consumo_total / self.quilometragem_total

    def calcular_velocidade_media(self):
        self.velocidade_media = self.quilometragem_total / self.tempo_de_viagem


computador_de_bordo = Computador_de_bordo()

print(computador_de_bordo)

computador_de_bordo.calcular_consumo_medio()
print(computador_de_bordo)
computador_de_bordo.calcular_velocidade_media()
print(computador_de_bordo)
