# Desenvolva sua classe Recipiente aqui.

class Recipiente():
    def __init__(self, tamanho: float = 0, conteudo: float = 0, limpo: bool =  True):

        if tamanho < 0:
            self.tamanho = 0
        else:
            self.tamanho = tamanho

        self.conteudo = conteudo

        self.limpo = limpo
    
    def esvaziar(self):
        self.conteudo = 0

    def esta_vazio(self):
        if self.conteudo == 0:
            return True
        return False

    def lavar(self):
        self.limpo = True
        self.conteudo = 0

    def esta_limpo(self): 
        return self.limpo

    def estado(self):
        if self.limpo:
            return "limpo"
        return "sujo"

    def sujar(self):
        self.limpo = False

    def __repr__(self) -> str:
        return f"Um recipiente {self.estado()} não especificado"

    def __str__(self) -> str:
        return f"Um recipiente {self.estado()} não especificado"

