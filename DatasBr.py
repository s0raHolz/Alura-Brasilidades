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

    def dia_semana_cadastro(self):
        dias_semana = {"6": "Domingo", "0": "Segunda-feira", "1": "Terça-feira", "2": "Quarta-feira",
                      "3": "Quinta-feira", "4": "Sexta-feira", "5": "Sábado"}
        dia = str(self.momento_cadastro.weekday())
        return dias_semana[dia]

    def tempo_cadastro(self):
        return datetime.today() + timedelta(days=32, hours=13) - self.momento_cadastro

    def __str__(self):
        return  self.momento_cadastro.strftime("%d/%m/%Y %H:%M")


cadastro = DatasBr()
print(cadastro.mes_cadastro(), cadastro.dia_semana_cadastro())
print(cadastro, cadastro.tempo_cadastro())