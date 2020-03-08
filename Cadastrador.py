from DatasBr import DatasBr
from TelefonesBr import TelefonesBr
from DocumentosBr import FabricaDocumento
from EnderecosBr import EnderecoBr


class Cadastrador:

    @classmethod
    def cadastra_usuario(cls):
        documento = cls.cadastra_documeto()
        telefone = cls.cadastra_telefone()
        endereco = cls.cadastra_endereco()
        momento_do_cadastro = DatasBr()
        return Usuario(documento, telefone, endereco, momento_do_cadastro)

    @staticmethod
    def cadastra_documeto():
        doc_num = input("Digite o número do CPF/CNPJ: ")
        documento = FabricaDocumento.fabrica_documento(doc_num)
        return documento

    @staticmethod
    def cadastra_telefone():
        tel_num = input("Digite o nº de telefone: ").strip()
        telefone = TelefonesBr(tel_num)
        return telefone

    @staticmethod
    def cadastra_endereco():
        cep = input("Digite o CEP: ").strip()
        endereco = EnderecoBr(cep)
        return endereco

class Usuario:

    def __init__(self, documento, telefone, endereco, momento_do_cadastro):
        self._documento = documento
        self._telefone = telefone
        self._endereco = endereco
        self._momento_do_cadastro = momento_do_cadastro
        self._dados = {"CPF/CNPJ": f"{self.documento}", "Telefone": f"{self.telefone}",
                       "CEP": f"{self._endereco['CEP']}", "Bairro": f"{self._endereco['Bairro']}",
                       "Cidade": f"{self._endereco['Cidade']}", "UF": f"{self._endereco['UF']}" }
        print(self)

    @property
    def dados(self):
        return self._dados

    @property
    def documento(self):
        return str(self._documento)

    @property
    def telefone(self):
        return str(self._telefone)

    @property
    def endereco(self):
        return str(self._endereco)

    @property
    def momento_do_cadastro(self):
        return str(self._momento_do_cadastro)

    def __str__(self):
        return str(self._dados)