from DatasBr import DatasBr
from TelefonesBr import TelefonesBr
from DocumentosBr import FabricaDocumento

class Cadastrador:

    @classmethod
    def cadastra_usuario(cls):
        documento = cls.cadastra_documeto()
        telefone = cls.cadastra_telefone()
        momento_do_cadastro = DatasBr()
        return Usuario(documento, telefone, momento_do_cadastro)

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

class Usuario:

    def __init__(self, documento, telefone, momento_do_cadastro):
        self._documento = documento
        self._telefone = telefone
        self._momento_do_cadastro = momento_do_cadastro

    @property
    def documento(self):
        return str(self._documento)

    @property
    def telefone(self):
        return str(self._telefone)

    @property
    def momento_do_cadastro(self):
        return str(self._momento_do_cadastro)

    def __str__(self):
        return f"CPF/CNPJ: {self._documento} TEL: {self._telefone} Cadastrado em: {self._momento_do_cadastro}"