import re

class Telefonesbr:
    def __init__(self,texto):
        if self.valida_telefone(texto):
            self.telefone = texto
        else:
            raise ValueError ("Numero de telefone invalido")

    
    def valida_telefone(self, texto):
        padrao = "([0-9]{2,3})?([0-9]{2})([0-9]{5})-([0-9]{4})"
        telefone = re.search(padrao, texto)
        if telefone:
            return True
        else:
            return False

    def numero_format(self):
         padrao = "([0-9]{2,3})?([0-9]{2})([0-9]{5})-([0-9]{4})"
         resposta = re.search(padrao, self.telefone)
         mask = "+{}({}){}-{}".format(resposta.group(1), resposta.group(2), resposta.group(3), resposta.group(4))
         return mask


    def __str__(self):
        return self.numero_format



any = Telefonesbr("555199703-5187")

print(any.numero_format())