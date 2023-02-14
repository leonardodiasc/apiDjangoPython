import re

def cpf_valido(numero_do_cpf):
    return len(numero_do_cpf) == 11

def nome_valido(nome):
    if(nome.isalpha() or nome.isspace):
        return nome
    else:
        return False

def rg_valido(numero_do_rg):
    return len(numero_do_rg) == 9

def celular_valido(numero_celular):
    """Verifica se o celular é valido"""
    modelo = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    resposta = re.findall(modelo, numero_celular)
    return resposta