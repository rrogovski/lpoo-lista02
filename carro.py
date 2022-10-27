class Carro:
    consumo: 0
    quantidade_combustivel: 0
    
    def __init__(self, consumo):
        self.consumo = consumo
        self.quantidade_combustivel = 0
    
    def andar(self, km):
        if self.quantidade_combustivel * self.consumo < km:
            print("Não é possível andar essa distância. Não há combustível suficiente.")
        else:
            self.quantidade_combustivel -= km / self.consumo
        
    def adicionar_gasolina(self, litros):
        self.quantidade_combustivel += litros
        
    def obter_gasolina(self):
        print (f"O carro tem {self.quantidade_combustivel:.2f} litros de combustível.")