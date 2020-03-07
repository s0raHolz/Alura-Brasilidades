from CpfCnpj import FabricaDocumento, Cpf, Cnpj

class Menu:

    @classmethod
    def menu(cls):
        cls.mostra_menu()
        inpt = cls.pega_input()
        return inpt

    @staticmethod
    def mostra_menu():
        print("[1] - Documento [CPF/CNPJ]")
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
class Registrador:

    @staticmethod
    def e_cpf_ou_cnpj(documento):
        if isinstance(documento, Cpf):
            return "CPF"
        elif isinstance(documento, Cnpj):
            return "CNPJ"

    @classmethod
    def registra_documetos(cls):

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

class Impressor:

    @staticmethod
    def imprime_documentos(documentos):
        for key, values in dict.items(documentos):
            print(f"{key} registrados: ", end="")
            for value in values:
                print(f"{value}", end=" ")
            print()

def main():

    total_documentos_cadastrados = {"CPF": [], "CNPJ": []}
    while True:
        ans = Menu.menu()
        if ans == 0:
            break
        elif ans == 1:
            documentos_cadastrados = Registrador.registra_documetos()
            total_documentos_cadastrados["CPF"].extend(documentos_cadastrados["CPF"])
            total_documentos_cadastrados["CNPJ"].extend(documentos_cadastrados["CNPJ"])
    Impressor.imprime_documentos(total_documentos_cadastrados)


main()