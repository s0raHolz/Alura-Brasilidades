from validate_docbr import CPF, CNPJ

class FabricaDocumento:

    @classmethod
    def fabrica_documento(cls, documento):
        if cls.cpf_ou_cnpj(documento).upper().strip() == "CPF":
            return Cpf(documento)
        elif cls.cpf_ou_cnpj(documento).upper().strip() == "CNPJ":
            return Cnpj(documento)
        else:
            raise ValueError("Tipo de documento inválido!!")

    @staticmethod
    def cpf_ou_cnpj(documento):
        if len(documento) == 11:
            return "CPF"
        elif len(documento) == 14:
            return "CNPJ"
        else:
            raise ValueError("Quantidade de Dígitos inválida!")

class Cpf(CPF):

    def __init__(self, cpf):
        super().__init__()
        cpf = str(cpf)
        if self.cpf_e_valido(cpf):
            self.cpf = cpf
        else:
            raise ValueError("CPF Inválido!!")

    def cpf_e_valido(self, cpf):
        return self.validate(cpf)

    def formata_cpf(self):
        return self.mask(self.cpf)

    def __str__(self):
        return self.formata_cpf()

class Cnpj(CNPJ):

    def __init__(self, cnpj):
        super().__init__()
        cnpj = str(cnpj)
        if self.cnpj_e_valido(cnpj):
            self.cnpj = cnpj
        else:
            raise ValueError("CNPJ Inválido!!")

    def cnpj_e_valido(self, cnpj):
        return self.validate(cnpj)

    def formata_cnpj(self):
        return self.mask(self.cnpj)

    def __str__(self):
        return self.formata_cnpj()