import re

class TelefonesBr:
    padrao ="([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
    def __init__(self, telefone):
        if self.valida_telefone(telefone):
            self.numero = telefone
        else:
            raise ValueError("Número incorreto!!")

    def valida_telefone(self, telefone):
        resposta = re.findall(self.padrao, telefone)
        if resposta:
            return True
        else:
            return False

    def formata_numero(self):
        resp = re.search(self.padrao, self.numero)
        if not resp.group(1):
            numero_formatado = f"+55 ({resp.group(2)}) {resp.group(3)}-{resp.group(4)}"
        else:
            numero_formatado = f"+{resp.group(1)} ({resp.group(2)}) {resp.group(3)}-{resp.group(4)}"
        return numero_formatado

    def __str__(self):
        return self.formata_numero()