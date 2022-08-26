#Não funcionara se estiver dentro da pasta Phyton
from datetime import datetime
import re

class Date:
    def __init__(self):
        self.momento_cadastro = datetime.today()

    def __str__(self):
        return self.format_dia()

    def mes_cadastro(self):
        meses= ["","janeiro", "fevereiro", "março", "abril", "maio",
        "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
        mes_do_cadastro = self.momento_cadastro.month
        return meses[mes_do_cadastro]

    def format_dia(self):
        dia = self.momento_cadastro.strftime("%d/%m/%Y %H:%M:%S")
        return dia
    

hoje = Date()
print(hoje)
