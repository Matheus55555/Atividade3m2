from tkinter import *
from tkinter import messagebox, scrolledtext
from database import conectar
from matplotlib import pyplot as plt


# ---------- Tela Hotel ----------
def tela_hotel(frame):
    Label(frame, text="Gerenciar Hotel", font=("Arial", 16, "bold"), bg="#333", fg="white").pack(pady=10)

    id_var = StringVar()
    nome_var = StringVar()
    cidade_var = StringVar()
    preco_var = StringVar()

    campos = Frame(frame, bg="#333")
    campos.pack(pady=10)

    def criar_linha(label, var, row):
        Label(campos, text=label, bg="#333", fg="white").grid(row=row, column=0, sticky="w", padx=10, pady=5)
        Entry(campos, textvariable=var, width=30).grid(row=row, column=1, pady=5)

    criar_linha("ID do Hotel (para alterar/excluir):", id_var, 0)
    criar_linha("Nome do Hotel:", nome_var, 1)
    criar_linha("Cidade:", cidade_var, 2)
    criar_linha("Preço por Noite:", preco_var, 3)

    botoes = Frame(frame, bg="#333")
    botoes.pack(pady=10)

    def salvar_hotel():
        try:
            conn = conectar()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO hoteis (nome, cidade, preco_noite) VALUES (%s, %s, %s)",
                           (nome_var.get(), cidade_var.get(), preco_var.get()))
            conn.commit()
            conn.close()
            messagebox.showinfo("Sucesso", "Hotel salvo com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao salvar hotel: {e}")

    def alterar_hotel():
        try:
            conn = conectar()
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE hoteis
                SET nome = %s, cidade = %s, preco_noite = %s
                WHERE id = %s
            """, (nome_var.get(), cidade_var.get(), preco_var.get(), id_var.get()))
            conn.commit()
            conn.close()
            messagebox.showinfo("Sucesso", "Hotel alterado com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao alterar hotel: {e}")

    def excluir_hotel():
        try:
            conn = conectar()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM hoteis WHERE id = %s", (id_var.get(),))
            conn.commit()
            conn.close()
            messagebox.showinfo("Sucesso", "Hotel excluído com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao excluir hotel: {e}")

    Button(botoes, text="Salvar Novo", command=salvar_hotel, width=15).grid(row=0, column=0, padx=10)
    Button(botoes, text="Alterar", command=alterar_hotel, width=15).grid(row=0, column=1, padx=10)
    Button(botoes, text="Excluir", command=excluir_hotel, bg="red", fg="white", width=15).grid(row=0, column=2, padx=10)


# ---------- Tela Passagem ----------
def tela_passagem(frame):
    Label(frame, text="Gerenciar Passagem", font=("Arial", 16, "bold"), bg="#333", fg="white").pack(pady=10)

    id_var = StringVar()
    origem_var = StringVar()
    destino_var = StringVar()
    data_var = StringVar()
    preco_var = StringVar()

    campos = Frame(frame, bg="#333")
    campos.pack(pady=10)

    def criar_linha(label, var, row):
        Label(campos, text=label, bg="#333", fg="white").grid(row=row, column=0, sticky="w", padx=10, pady=5)
        Entry(campos, textvariable=var, width=30).grid(row=row, column=1, pady=5)

    criar_linha("ID da Passagem (para alterar/excluir):", id_var, 0)
    criar_linha("Origem:", origem_var, 1)
    criar_linha("Destino:", destino_var, 2)
    criar_linha("Data (AAAA-MM-DD):", data_var, 3)
    criar_linha("Preço:", preco_var, 4)

    botoes = Frame(frame, bg="#333")
    botoes.pack(pady=10)

    def salvar_passagem():
        try:
            conn = conectar()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO passagens (origem, destino, data, preco) VALUES (%s, %s, %s, %s)",
                           (origem_var.get(), destino_var.get(), data_var.get(), preco_var.get()))
            conn.commit()
            conn.close()
            messagebox.showinfo("Sucesso", "Passagem salva com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao salvar passagem: {e}")

    def alterar_passagem():
        try:
            conn = conectar()
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE passagens
                SET origem = %s, destino = %s, data = %s, preco = %s
                WHERE id = %s
            """, (origem_var.get(), destino_var.get(), data_var.get(), preco_var.get(), id_var.get()))
            conn.commit()
            conn.close()
            messagebox.showinfo("Sucesso", "Passagem alterada com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao alterar passagem: {e}")

    def excluir_passagem():
        try:
            conn = conectar()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM passagens WHERE id = %s", (id_var.get(),))
            conn.commit()
            conn.close()
            messagebox.showinfo("Sucesso", "Passagem excluída com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao excluir passagem: {e}")

    Button(botoes, text="Salvar Nova", command=salvar_passagem, width=15).grid(row=0, column=0, padx=10)
    Button(botoes, text="Alterar", command=alterar_passagem, width=15).grid(row=0, column=1, padx=10)
    Button(botoes, text="Excluir", command=excluir_passagem, bg="red", fg="white", width=15).grid(row=0, column=2, padx=10)


# ---------- Tela Relatório ----------
def tela_relatorio(frame):
    Label(frame, text="Relatório de Hotéis", font=("Arial", 16, "bold"), bg="#333", fg="white").pack(pady=10)

    text = Text(frame, height=20, width=80)
    text.pack(pady=10)

    def gerar_relatorio():
        try:
            text.delete(1.0, END)
            conn = conectar()
            cursor = conn.cursor()
            cursor.execute("SELECT id, nome, cidade, preco_noite FROM hoteis")
            for row in cursor.fetchall():
                text.insert(END, f"ID: {row[0]} | Nome: {row[1]} | Cidade: {row[2]} | Preço: R${row[3]}\n")
            conn.close()
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao gerar relatório: {e}")

    Button(frame, text="Gerar Relatório", command=gerar_relatorio, width=20).pack(pady=10)


# ---------- Tela Gráfico ----------
def gerar_grafico_faturamento():
    try:
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("SELECT nome, preco_noite FROM hoteis")
        dados = cursor.fetchall()

        nomes = [item[0] for item in dados]
        faturamentos = [float(item[1]) for item in dados]

        plt.figure(figsize=(10, 6))
        plt.bar(nomes, faturamentos, color='skyblue')
        plt.title('Faturamento dos Hotéis (Preço por Noite)')
        plt.xlabel('Hotéis')
        plt.ylabel('Preço (R$)')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

        conn.close()

    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao gerar gráfico: {e}")


# ---------- Tela Chatbot ----------
def tela_chatbot(frame):
    Label(frame, text="Chatbot - Assistente de Viagem", font=("Arial", 16, "bold"), bg="#333", fg="white").pack(pady=10)

    chat_area = scrolledtext.ScrolledText(frame, wrap="word", width=70, height=20, bg="white")
    chat_area.pack(pady=10)
    chat_area.config(state="disabled")

    user_input = StringVar()

    def enviar_msg():
        msg = user_input.get()
        if msg.strip() == "":
            return

        chat_area.config(state="normal")
        chat_area.insert("end", f"Você: {msg}\n")
        resposta = responder_chatbot(msg)
        chat_area.insert("end", f"Bot: {resposta}\n\n")
        chat_area.config(state="disabled")
        chat_area.see("end")
        user_input.set("")

    def responder_chatbot(pergunta):
        pergunta = pergunta.lower()
        if "hotel" in pergunta:
            return "Para reservar ou editar um hotel, use a aba 'Hotel'."
        elif "passagem" in pergunta:
            return "Vá na aba 'Passagem' para gerenciar as passagens."
        elif "relatório" in pergunta:
            return "Use a aba 'Relatório' para visualizar os hotéis cadastrados."
        elif "gráfico" in pergunta:
            return "Clique no botão 'Gráfico Faturamento' no menu."
        elif "oi" in pergunta or "olá" in pergunta:
            return "Olá! Como posso te ajudar na sua viagem?"
        else:
            return "Desculpe, não entendi. Pergunte sobre hotel, passagem, relatório ou gráfico."

    entrada = Entry(frame, textvariable=user_input, width=60)
    entrada.pack(pady=5, side="left", padx=10)

    Button(frame, text="Enviar", command=enviar_msg, width=10).pack(pady=5, side="left")
