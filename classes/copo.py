# Desenvolva sua classe Copo aqui.
from classes.recipiente import Recipiente


class Copo(Recipiente):
    def __init__(self, tamanho: float = 0):
        super().__init__(tamanho)

        

    def encher(self, bebida: str = "água"):

        if self.limpo == False:
            return "Não se pode encher um copo sujo"

        self.limpo = False
        self.conteudo = float(self.tamanho)

        self.bebida = bebida

    def beber(self, quantidade: float = 0):
        if quantidade < 0:
            return "Quantidade deve ser positiva"
        if quantidade > self.conteudo:
            return "Não há bebida suficiente no copo"
            # testar para descobrir se é preciso diminuir ou igualar
        self.conteudo -= quantidade

    def lavar(self):
        self.bebida = None
        self.conteudo = 0
        self.limpo = True
        
    def __repr__(self) -> str:
        if self.conteudo == 0:
            return f"Um copo vazio de {float(self.tamanho)}ml"
        return f"Um copo de {float(self.tamanho)}ml contendo {float(self.conteudo)}ml de {self.bebida}"

    def __str__(self) -> str:
        if self.conteudo == 0:
            return f"Um copo vazio de {float(self.tamanho)}ml"
        return f"Um copo de {float(self.tamanho)}ml contendo {float(self.conteudo)}ml de {self.bebida}"

c = Copo(300)
c.encher("café")
c.beber(30)
c.lavar()

print(c.esta_limpo())
print(c.__dict__)