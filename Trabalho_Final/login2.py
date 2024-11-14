from tkinter import *
from tkinter.messagebox import *
from tkinter import filedialog
import Ligacao25 as liga
import csv

######### Variáveis
fnt1 = ("Arial", 12)
fnt2 = ("Arial", 18, "bold")


############### Funções ###########

def leitura():
    nome = euser.get()
    senha = epass.get()
    cursor = conn.cursor()  # área de transferência de dados
    sql = f"""SELECT nome, senha FROM login WHERE nome = '{nome}' AND senha = '{senha}';"""
    cursor.execute(sql)
    dados = cursor.fetchone()

    if dados:
        showinfo("Login", "Login realizado com sucesso!")
        jan.withdraw()  # esconde a janela de login

        # Funções adicionais
        def importar(nomefich):
            conn = liga.conexao()
            cursor = conn.cursor()
            with open(nomefich, "r", encoding="UTF-8") as fich:
                conte = fich.readlines()[1:]  # Remove cabeçalho do CSV
                for elem in conte:
                    dados = elem.strip().split(';')
                    dados[2] = dados[2][:-3]  # Elimina os últimos 3 dígitos
                    dados[3] = f"{float(dados[3]):.2f}"
                    cursor.execute(
                        "INSERT INTO clientes (nome, ncont, esaldo, morada, local, codpost, zona) VALUES (?, ?, ?, ?, ?, ?, ?)",
                        (dados[0], dados[2], dados[3], dados[4], dados[5], dados[6], dados[7]))
            conn.commit()
            conn.close()
            showinfo("Importar", "Importação concluída com sucesso!")

        def exportar():
            nfich = filedialog.asksaveasfilename(title="Salvar arquivo", defaultextension=".csv",
                                                 filetypes=[("CSV files", "*.csv"), ("All files", "*.*")])
            conn = liga.conexao()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM clientes")
            rows = cursor.fetchall()
            with open(nfich, mode="w", newline='', encoding="UTF-8") as fich:
                writer = csv.writer(fich, delimiter=";")
                writer.writerows(rows)
            conn.close()
            showinfo("Exportar", "Exportação concluída com sucesso!")

        def sair():
            jan2.destroy()
            jan.deiconify()
            limpar()

        # Criação da janela principal
        jan2 = Toplevel()
        jan2.title("Janela de Import/Export")
        jan2.geometry("550x250")
        jan2.configure(bg="#f0f0f5")

        # Componentes
        Label(jan2, text="Nome do Ficheiro", font=fnt1, bg="#f0f0f5").pack(pady=10)
        efich = Entry(jan2, font=("Arial", 14), width=40, relief=GROOVE, bd=2)
        efich.pack(pady=10)

        frame_buttons = Frame(jan2, bg="#f0f0f5")
        frame_buttons.pack(pady=15)

        Button(frame_buttons, text="Importar Clientes", font=fnt1, bg="#4CAF50", fg="white",
               command=lambda: importar(efich.get()), width=15).grid(row=0, column=0, padx=5, pady=5)
        Button(frame_buttons, text="Exportar Clientes", font=fnt1, bg="#2196F3", fg="white", command=exportar,
               width=15).grid(row=0, column=1, padx=5, pady=5)
        Button(frame_buttons, text="Sair", font=fnt1, bg="#f44336", fg="white", command=sair, width=15).grid(row=0,
                                                                                                             column=2,
                                                                                                             padx=5,
                                                                                                             pady=5)

    else:
        showwarning("Login", f"Usuário '{nome}' ou senha incorretos!")


def limpar():
    euser.delete(0, END)
    epass.delete(0, END)
    euser.focus()


def cadastrar():
    nome = euser.get()
    senha = epass.get()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO login (nome, senha) VALUES (?, ?)", (nome, senha))
    conn.commit()
    conn.close()
    showinfo("Cadastro", "Cadastro realizado com sucesso.")


# Janela de Login
global conn
conn = liga.conexao()
if conn:
    jan = Tk()
    jan.title("Sistema de Login")
    jan.geometry("400x300")
    jan.configure(bg="#f0f0f5")

    Label(jan, text="Bem-vindo ao Sistema", font=fnt2, bg="#f0f0f5", fg="#333").pack(pady=10)

    # Campos de login
    frame_campos = Frame(jan, bg="#f0f0f5")
    frame_campos.pack(pady=10)

    Label(frame_campos, text="Username:", font=fnt1, bg="#f0f0f5").grid(row=0, column=0, padx=5, pady=10)
    euser = Entry(frame_campos, font=("Arial", 14), width=25, relief=GROOVE, bd=2)
    euser.grid(row=0, column=1)

    Label(frame_campos, text="Password:", font=fnt1, bg="#f0f0f5").grid(row=1, column=0, padx=5, pady=10)
    epass = Entry(frame_campos, font=("Arial", 14), width=25, relief=GROOVE, bd=2, show="*")
    epass.grid(row=1, column=1)

    # Botões de Ação
    frame_botoes = Frame(jan, bg="#f0f0f5")
    frame_botoes.pack(pady=20)

    Button(frame_botoes, text="Login", font=fnt1, bg="#4CAF50", fg="white", command=leitura, width=10).grid(row=0,
                                                                                                            column=0,
                                                                                                            padx=5)
    Button(frame_botoes, text="Limpar", font=fnt1, bg="#FF9800", fg="white", command=limpar, width=10).grid(row=0,
                                                                                                            column=1,
                                                                                                            padx=5)
    Button(frame_botoes, text="Cadastrar", font=fnt1, bg="#2196F3", fg="white", command=cadastrar, width=10).grid(row=0,
                                                                                                                  column=2,
                                                                                                                  padx=5)

    jan.mainloop()
else:
    showinfo("Conexão", "Não foi possível conectar ao banco de dados.")

