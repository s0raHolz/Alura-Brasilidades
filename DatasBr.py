from datetime import datetime, timedelta

class DatasBr:

    def __init__(self):
        self.momento_cadastro = datetime.today()

    def mes_cadastro(self):
        meses_do_ano = {"1": "Janeiro", "2": "Fevereiro", "3": "Março", "4": "Abril",
                        "5": "Maio", "6": "Junho", "7": "Julho", "8": "Agosto",
                        "9": "Setembro", "10": "Outubro", "11": "Novembro", "12": "Dezembro"}
        mes = str(self.momento_cadastro.month)
        return meses_do_ano[mes]


cadastro = DatasBr()
print(cadastro.mes_cadastro())