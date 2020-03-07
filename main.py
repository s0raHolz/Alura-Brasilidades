from TelefonesBr import TelefonesBr
from CpfCnpj import FabricaDocumento, Cpf, Cnpj


class Menu:

    @classmethod
    def menu(cls):
        cls.mostra_menu()
        inpt = cls.pega_input()
        return inpt

    @staticmethod
    def mostra_menu():
        print("[1] - Documentos [CPF/CNPJ]")
        print("[2] - Nºs de Telefone")
        print("[0] - Sair")

    @staticmethod
    def pega_input():
        while True:
            try:
                ans = int(input("O que deseja cadastrar?"))
                if ans == 0:
                    break
            except:
                print("Desculpe, não entendi.")
                continue
            break
        return ans


class Cadastrador:

    @staticmethod
    def e_cpf_ou_cnpj(documento):
        if isinstance(documento, Cpf):
            return "CPF"
        elif isinstance(documento, Cnpj):
            return "CNPJ"

    @classmethod
    def cadastra_documetos(cls):

         documentos_cadastrados = {"CPF": [], "CNPJ": []}
         while True:
            doc_num = input("Digite o número do CPF/CNPJ: ")
            documento = FabricaDocumento.fabrica_documento(doc_num)
            print(f"Seu {documento.__class__.__name__.upper()} de código {documento} foi cadastrado com sucesso!")

            tipo = cls.e_cpf_ou_cnpj(documento)
            documentos_cadastrados[tipo].append(documento)

            ans = input("Quer continuar? [S/N]")
            if ans.upper().strip() == 'N':
                break

         return documentos_cadastrados

    @staticmethod
    def cadastra_telefone():
        telefones_cadastrados = []
        while True:
            tel_num = input("Digite o nº de telefone: ").strip()
            telefone = TelefonesBr(tel_num)
            telefones_cadastrados.append(telefone)
            print(f"Seu {telefone.__class__.__name__.upper()} de código {telefone} foi cadastrado com sucesso!")
            ans = input("Quer continuar? [S/N]")
            if ans.upper().strip() == 'N':
                break

        return telefones_cadastrados

class Impressor:

    @staticmethod
    def imprime_documentos(documentos):
        for key, values in dict.items(documentos):
            print(f"{key} registrados: ", end="")
            for value in values:
                print(f"{value}", end=" ")
            print()

    @staticmethod
    def imprime_telefones(telefones):
        print(f"Telefones registrados: ", end="")
        for tel in telefones:
            print(tel, end=" ")
        print()


class Programa(Menu):

    @classmethod
    def menu(cls):
        todos_documentos_cadastrados = {"CPF": [], "CNPJ": []}
        todos_telefones_cadastrados = []
        while True:
            ans = super().menu()
            if ans == 0:
                break
            elif ans == 1:
                documentos_cadastrados = Cadastrador.cadastra_documetos()
                todos_documentos_cadastrados["CPF"].extend(documentos_cadastrados["CPF"])
                todos_documentos_cadastrados["CNPJ"].extend(documentos_cadastrados["CNPJ"])
            elif ans == 2:
                todos_telefones_cadastrados.extend(Cadastrador.cadastra_telefone())
        return (todos_documentos_cadastrados, todos_telefones_cadastrados)


def main():
    doc_e_tel = Programa.menu()
    Impressor.imprime_documentos(doc_e_tel[0])
    Impressor.imprime_telefones(doc_e_tel[1])


main()
