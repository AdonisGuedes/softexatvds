class DescontoHandler:

    def __init__(self, proximo=None):

        self.proximo = proximo

    def tratar_desconto(self, percentual):

        if self.proximo:

            return self.proximo.tratar_desconto(percentual)

        else:

            print("Nenhum responsável pôde aprovar esse desconto.")


class Caixa(DescontoHandler):

    def tratar_desconto(self, percentual):

        if percentual <= 5:

            print(f"Caixa: desconto de {percentual}% aprovado.")

        else:

            print("Caixa: não posso aprovar, encaminhando ao gerente...")

            super().tratar_desconto(percentual)
            

class Gerente(DescontoHandler):

    def tratar_desconto(self, percentual):

        if percentual <= 15:

            print(f"Gerente: desconto de {percentual}% aprovado.")

        else:

            print("Gerente: não posso aprovar, encaminhando ao diretor...")

            super().tratar_desconto(percentual)
            

class Diretor(DescontoHandler):

    def tratar_desconto(self, percentual):

        print(f"Diretor: desconto de {percentual}% aprovado sem restrições.")

# Criando a cadeia: Caixa -> Gerente -> Diretor

diretor = Diretor()

gerente = Gerente(diretor)

caixa = Caixa(gerente)

# Testando

caixa.tratar_desconto(3)   # Caixa aprova

caixa.tratar_desconto(10)  # Vai pro Gerente

caixa.tratar_desconto(25)  # Vai pro Diretor
