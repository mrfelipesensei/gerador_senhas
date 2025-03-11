import random
import string #Contém letras e símbolos úteis
import tkinter as tk
from tkinter import messagebox


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

def modo_terminal():
    tamanho = int(input("Digite o tamanho da senha: "))
    quantidade = int(input("Quantas senhas deseja gerar? "))
    incluir_numeros = input("Incluir números? (s/n): ").strip().lower() == 's'
    incluir_maiusculas = input("Incluir letras maiúsculas? (s/n): ").strip().lower() == 's'
    incluir_simbolos = input("Incluir símbolos? (s/n): ").strip().lower() == 's'

    senhas = [gerar_senha(tamanho, incluir_numeros, incluir_maiusculas, incluir_simbolos) for _ in range(quantidade)]
    
    print("\n Senhas geradas:")
    for senha in senhas:
        print(senha)
    
    salvar_senhas(senhas)

def gerar_senha_interface():
    try:
        tamanho = int(entry_tamanho.get())
        quantidade = int(entry_quantidade.get())
        incluir_numeros = var_numeros.get()
        incluir_maiusculas = var_maiusculas.get()
        incluir_simbolos = var_simbolos.get()

        senhas = [gerar_senha(tamanho, incluir_numeros, incluir_maiusculas, incluir_simbolos) for _ in range(quantidade)]
        resultado.delete("1.0", tk.END)
        resultado.insert(tk.END, "\n".join(senhas))

        salvar_senhas(senhas)
        messagebox.showinfo("Sucesso","Senhas geradas e salvas em 'senhas.txt'")

    except ValueError:
        messagebox.showerror("Erro", "Digite valores numéricos válidos!")


def iniciar_interface():
    global entry_tamanho, entry_quantidade, var_numeros, var_maiusculas, var_simbolos, resultado

    root = tk.Tk()
    root.title("Gerador de Senhas")

    tk.Label(root, text="Tamanho da Senha: ").grid(row=0, column=0)
    entry_tamanho = tk.Entry(root)
    entry_tamanho.grid(row=0, column=1)

    tk.Label(root, text="Quantidade de Senhas: ").grid(row=1, column=0)
    entry_quantidade = tk.Entry(root)
    entry_quantidade.grid(row=1, column=1)

    var_numeros = tk.BooleanVar()
    tk.Checkbutton(root, text="Incluir Números",variable=var_numeros).grid(row=2,column=0,columnspan=2)

    var_maiusculas = tk.BooleanVar()
    tk.Checkbutton(root, text="Incluir Maiúsculas", variable=var_maiusculas).grid(row=3, column=0, columnspan=2)

    var_simbolos = tk.BooleanVar()
    tk.Checkbutton(root, text="Incluir Símbolos",variable=var_simbolos).grid(row=4, column=0, columnspan=2)

    tk.Button(root, text="Gerar Senha", command=gerar_senha_interface).grid(row=5, column=0, columnspan=2)

    resultado = tk.Text(root, height=10, width=40)
    resultado.grid(row=6, column=0, columnspan=2)

    root.mainloop()



import os

def salvar_senhas(senhas):
    dir_atual = os.path.dirname(os.path.abspath(__file__))
    caminho_arquivo = os.path.join(dir_atual, "senhas.txt")

    with open(caminho_arquivo, "w") as arquivo:
        for senha in senhas:
            arquivo.write(senha + "\n")
    
    print("\n Senhas salvas em 'senhas.txt'")


if __name__ == "__main__":
    print("Escolha o modo de execução: ")
    print("1 - Modo Terminal")
    print("2 - Interface Gráfica")

    opcao = input("Digite o número da opção desejada: ").strip()

    if opcao == "1":
        modo_terminal()
    elif opcao == "2":
        iniciar_interface()
    else:
        print("Opção Inválida!")