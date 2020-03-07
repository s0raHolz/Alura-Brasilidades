from Cadastrador import Cadastrador

class Menu:

    def menu(self):
        self._mostra_menu()
        inpt = self._recolhe_input()
        return inpt

    def _mostra_menu(self):
        print("Deseja cadastrar um usuário [S/N]? ", end="")

    def _recolhe_input(self):
        while True:
            try:
                inpt = self._valida_input(input())
            except ValueError:
                continue
            break
        return inpt

    def _valida_input(self, inpt):
        inpt = inpt.strip().upper()
        if inpt == 'S':
            return True
        elif inpt == 'N':
            return False
        else:
            raise ValueError("Opção Inválida")

class Programa(Menu):

    def __init__(self):
        self.usuarios_cadastrados = []
        while True:
            if self.menu():
                self.usuarios_cadastrados.append(self._cadastro())
                continue
            else:
                for usuario in self.usuarios_cadastrados:
                    print(f"Registrado o Usuário com {usuario}")
                break

    def _cadastro(self):
        return Cadastrador.cadastra_usuario()