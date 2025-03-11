import random
import string #Contém letras e símbolos úteis

#Função de gerar a senha
def gerar_senha(tamanho=12, incluir_numeros=True, incluir_maiusculas=True, incluir_simbolos=True):
    caracteres = string.ascii_lowercase #letras minúsculas por padrão

    if incluir_maiusculas:
        caracteres += string.ascii_uppercase
    if incluir_numeros:
        caracteres += string.digits
    if incluir_simbolos:
        caracteres += string.punctuation

    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

'''#Teste básico
print(gerar_senha(16)) #Gera uma senha de 16 caracteres'''

def main():
    tamanho = int(input("Digite o tamanho da senha: "))
    quantidade = int(input("Quantas senhas deseja gerar? "))
    incluir_numeros = input("Incluir números? (s/n): ").strip().lower() == 's'
    incluir_maiusculas = input("Incluir letras maiúsculas? (s/n): ").strip().lower() == 's'
    incluir_simbolos = input("Incluir símbolos? (s/n): ").strip().lower() == 's'

    senhas = [gerar_senha(tamanho, incluir_numeros, incluir_maiusculas, incluir_simbolos) for _ in range(quantidade)]
    
    print("\n Senhas geradas:")
    for senha in senhas:
        print(senha)
    
    return senhas

import os

def salvar_senhas(senhas):
    dir_atual = os.path.dirname(os.path.abspath(__file__))
    caminho_arquivo = os.path.join(dir_atual, "senhas.txt")

    with open(caminho_arquivo, "w") as arquivo:
        for senha in senhas:
            arquivo.write(senha + "\n")
    
    print("\n Senhas salvas em 'senhas.txt'")


if __name__ == "__main__":
    senhas = main()
    salvar_senhas(senhas)