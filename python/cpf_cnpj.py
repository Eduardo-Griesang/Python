from xml.dom.minidom import Document
from validate_docbr import CPF, CNPJ

class documento:
    @staticmethod
    def cria_documento(documento):
        if len(documento) == 11:
            return Cpf(documento)
        elif len(documento) == 14:
            return Cnpj(documento)
        else:
            raise ValueError ("Numero de caracteres incorreto!")


class Cpf:
    def __init__(self, documento):
        documento = str(documento)
        if self.validar_cpf(documento):
            self.cpf = documento
        else:
            raise ValueError("CPF inválido")

    
    def validar_cpf(self, cpf):
            validador = CPF()
            return validador.validate(cpf)


    def __str__(self):
        cpf = CPF()
        mascara = cpf.mask(self.cpf)
        return ("O CPF é {}".format(mascara))


class Cnpj:
    def __init__(self, documento):
        documento = str(documento)
        if self.valida_cnpj(documento):
            self.cnpj = documento
        else:
            raise ValueError("CNPJ inválido!")

    def valida_cnpj(self, cnpj):
            validador = CNPJ()
            return validador.validate(cnpj)


    def __str__(self):
        cnpj = CNPJ()
        mascara= cnpj.mask(self.cnpj)
        return ("O CNPJ é {}".format(mascara))
        


Eduardo = documento.cria_documento("04082987070")
print(Eduardo)

StarBit_enterprise = documento.cria_documento("02828446000134")
print(StarBit_enterprise)