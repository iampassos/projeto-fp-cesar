import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from . import operacoes


# Função que será chamada ao clicar no botão de login
def realizar_login():
    usuario = entry_usuario.get()  # Obtém o nome de usuário
    senha = entry_senha.get()  # Obtém a senha

    # Validação de login simples
    if usuario == "admin" and senha == "12345":
        # Fechar a janela de login
        janela.quit()

        # Abrir a nova tela
        abrir_nova_tela()
    else:
        messagebox.showerror("Erro", "Usuário ou senha inválidos")


# Função para abrir a nova tela após login bem-sucedido
def abrir_nova_tela():
    # Criar nova janela
    nova_janela = tk.Tk()
    nova_janela.title("Tela Principal")
    nova_janela.state("zoomed")  # Maximize a nova janela

    # Cor de fundo da nova janela
    nova_janela.config(bg="#4c4f69")

    # Exemplo de conteúdo na nova janela
    titulo_principal = tk.Label(
        nova_janela,
        text="Bem-vindo à Tela Principal!",
        font=("Arial", 24, "bold"),
        bg="#4c4f69",
        fg="#ffffff",
    )
    titulo_principal.pack(pady=50)

    # Botão "Ver Metas e Desafios"
    botao_metas = tk.Button(
        nova_janela,
        text="Ver Metas e Desafios",
        font=("Arial", 14),
        bg="#ffffff",
        fg="#4c4f69",
        command=ver_metas_e_desafios,  # Função para essa opção
    )
    botao_metas.pack(pady=20)

    # Botão "Ver Registros"
    botao_registros = tk.Button(
        nova_janela,
        text="Ver Registros",
        font=("Arial", 14),
        bg="#ffffff",
        fg="#4c4f69",
        command=lambda: ver_registros(
            nova_janela
        ),  # Passando a nova janela para a função
    )
    botao_registros.pack(pady=20)

    # Botão para sair
    botao_sair = tk.Button(
        nova_janela, text="Sair", font=("Arial", 14), command=nova_janela.quit
    )
    botao_sair.pack(pady=20)

    # Inicia o loop da nova janela
    nova_janela.mainloop()


# Função que será chamada ao clicar no botão "Ver Metas e Desafios"
def ver_metas_e_desafios():
    messagebox.showinfo("Metas e Desafios", "Aqui estão suas metas e desafios.")


# Função que será chamada ao clicar no botão "Ver Registros"
def ver_registros(nova_janela):
    # Dados de exemplo para os registros (uma matriz de strings)
    # registros = [
    #     ["ID", "Nome", "Idade", "Cidade"],
    #     ["1", "Carlos", "29", "São Paulo"],
    #     ["2", "Ana", "34", "Rio de Janeiro"],
    #     ["3", "Lucas", "23", "Belo Horizonte"],
    #     ["4", "Maria", "25", "Curitiba"],
    #     ["5", "João", "31", "Fortaleza"],
    # ]

    reg = operacoes.ler_registro()
    registros = [r.__str__().split(", ") for r in reg]

    # Nova janela para exibir a tabela de registros
    janela_registros = tk.Toplevel(nova_janela)  # Toplevel cria uma nova janela
    janela_registros.title("Registros")
    janela_registros.geometry("800x400")  # Definir o tamanho da janela

    # Criar a Treeview (tabela)
    tree = ttk.Treeview(
        janela_registros,
        columns=("Modo", "Data", "Distância", "Tempo", "Local", "Clima"),
        show="headings",
    )
    tree.pack(fill="both", expand=True, padx=5, pady=10)

    # Definir os cabeçalhos das colunas
    tree.heading("Modo", text="Modo")
    tree.heading("Data", text="Data")
    tree.heading("Distância", text="Distância")
    tree.heading("Tempo", text="Tempo")
    tree.heading("Local", text="Local")
    tree.heading("Clima", text="Clima")

    # Adicionar os dados à tabela
    for registro in registros[1:]:  # Ignorando a primeira linha (cabeçalho)
        tree.insert("", tk.END, values=registro)

    # Função para adicionar um novo registro à tabela
    def adicionar_registro():
        def salvar_novo_registro():
            # Obtém os valores do formulário de entrada
            id_registro = entry_id.get()
            nome_registro = entry_nome.get()
            idade_registro = entry_idade.get()
            cidade_registro = entry_cidade.get()

            # Adiciona o novo registro à tabela
            tree.insert(
                "",
                tk.END,
                values=(id_registro, nome_registro, idade_registro, cidade_registro),
            )

            # Limpa os campos de entrada
            entry_id.delete(0, tk.END)
            entry_nome.delete(0, tk.END)
            entry_idade.delete(0, tk.END)
            entry_cidade.delete(0, tk.END)

        # Janela para adicionar um novo registro
        janela_adicionar = tk.Toplevel(janela_registros)
        janela_adicionar.title("Adicionar Registro")
        janela_adicionar.geometry("400x250")

        # Campos de entrada para o novo registro
        tk.Label(janela_adicionar, text="Modo").pack(pady=5)
        entry_id = tk.Entry(janela_adicionar)
        entry_id.pack(pady=5)

        tk.Label(janela_adicionar, text="Data").pack(pady=5)
        entry_nome = tk.Entry(janela_adicionar)
        entry_nome.pack(pady=5)

        tk.Label(janela_adicionar, text="Distância").pack(pady=5)
        entry_idade = tk.Entry(janela_adicionar)
        entry_idade.pack(pady=5)

        tk.Label(janela_adicionar, text="Tempo").pack(pady=5)
        entry_cidade = tk.Entry(janela_adicionar)
        entry_cidade.pack(pady=5)

        tk.Label(janela_adicionar, text="Local").pack(pady=5)
        entry_cidade = tk.Entry(janela_adicionar)
        entry_cidade.pack(pady=5)

        tk.Label(janela_adicionar, text="Clima").pack(pady=5)
        entry_cidade = tk.Entry(janela_adicionar)
        entry_cidade.pack(pady=5)

        # Botão para salvar o novo registro
        botao_salvar = tk.Button(
            janela_adicionar, text="Salvar", command=salvar_novo_registro
        )
        botao_salvar.pack(pady=20)

    # Função para remover o registro selecionado
    def remover_registro():
        selected_item = tree.selection()
        if selected_item:
            tree.delete(selected_item)
        else:
            messagebox.showwarning("Seleção", "Selecione um registro para remover.")

    # Botão para adicionar novo registro
    botao_adicionar = tk.Button(
        janela_registros, text="Adicionar Registro", command=adicionar_registro
    )
    botao_adicionar.pack(pady=20)

    # Botão para remover registro
    botao_remover = tk.Button(
        janela_registros, text="Remover Registro", command=remover_registro
    )
    botao_remover.pack(pady=20)

    # Botão para fechar a janela de registros
    botao_fechar = tk.Button(
        janela_registros, text="Fechar", command=janela_registros.destroy
    )
    botao_fechar.pack(pady=20)


# Criando a janela principal (tela de login)
janela = tk.Tk()
janela.title("Tela de Login")

# Maximiza a janela
janela.state("zoomed")

# Cor de fundo da janela de login
janela.config(bg="#4c4f69")

# Frame para organizar os elementos da tela de login
frame = tk.Frame(janela, bg="#ffffff", width=300, height=200, relief="solid", bd=2)
frame.place(relx=0.5, rely=0.5, anchor="center")  # Centraliza o frame na janela

# Título do login
titulo = tk.Label(frame, text="Login", font=("Arial", 24, "bold"), bg="#ffffff")
titulo.grid(row=0, column=0, columnspan=2, pady=10)

# Label e entrada para o nome de usuário
label_usuario = tk.Label(frame, text="Usuário", font=("Arial", 12), bg="#ffffff")
label_usuario.grid(row=1, column=0, padx=10, pady=5, sticky="w")
entry_usuario = tk.Entry(frame, font=("Arial", 12), width=20, bd=2)
entry_usuario.grid(row=1, column=1, padx=10, pady=5)

# Label e entrada para a senha
label_senha = tk.Label(frame, text="Senha", font=("Arial", 12), bg="#ffffff")
label_senha.grid(row=2, column=0, padx=10, pady=5, sticky="w")
entry_senha = tk.Entry(
    frame, font=("Arial", 12), width=20, bd=2, show="*"
)  # A senha aparece como "*"
entry_senha.grid(row=2, column=1, padx=10, pady=5)

# Botão de login
botao_login = tk.Button(
    frame,
    text="Entrar",
    font=("Arial", 12, "bold"),
    bg="#4c4f69",
    fg="#ffffff",
    command=realizar_login,
)
botao_login.grid(row=3, column=0, columnspan=2, pady=20)

# Inicia o loop principal da janela de login
janela.mainloop()
