import requests as rq


class EnderecoBr:

    def __init__(self, cep):
        self._endereco = BuscaEndereco.busca_endereco(cep)

    def __getitem__(self, item):
        return self._endereco[item]

    def __str__(self):
        return str(self._endereco)


class Cep:

    def __init__(self, cep):
        cep = str(cep)
        if self.cep_e_valido(cep):
            self.cep = cep
        else:
            raise ValueError("CEP inválido!!")

    def cep_e_valido(self, cep):
        if len(cep) == 8:
            return True
        else:
            return False

    def formata_cep(self):
        return f"{self.cep[:4]}-{self.cep[4:]}"

    def __str__(self):
        return self.formata_cep()


class BuscaEndereco:

    @classmethod
    def busca_endereco(cls, cep):
        resposta = cls.acessa_api(Cep(cep))
        endereco = cls.formata_resposta(resposta)
        return endereco

    @staticmethod
    def acessa_api(cep):
        return rq.get(f'https://viacep.com.br/ws/{cep.cep}/json/')

    @staticmethod
    def formata_resposta(resposta):
        dados = resposta.json()
        dados_filtrados = {'CEP': dados['cep'], 'Bairro': dados['bairro'], 'Cidade': dados['localidade'], 'UF': dados['uf']}
        return dados_filtrados