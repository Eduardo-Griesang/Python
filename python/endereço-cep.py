import requests
class BuscaEnderoco:
    def __init__(self, cep):
        cep = str(cep)
        if self.cep_validate(cep):
            self.cep = cep
        else:
            raise ValueError ("Cep inválido!")

    def __str__(self):
        return self.cep_format()
        
    def cep_validate(self, cep):
        if len(cep) == 8:
            return True
        else:
            return False

    def cep_format(self):
        first = self.cep [:5]
        second = self.cep [5:]
        return ("{}-{}".format(first, second))

cep = BuscaEnderoco(93990000)
print(cep)
morro = requests.get('https://viacep.com.br/ws/01001000/json/')