import tkinter as tk
from telas import tela_hotel, tela_passagem, tela_relatorio, gerar_grafico_faturamento, tela_chatbot


def abrir_janela(func):
    for widget in painel_principal.winfo_children():
        widget.destroy()
    func(painel_principal)


root = tk.Tk()
root.title("Sistema de Reservas e Agendamentos")
root.geometry("800x600")

menu = tk.Frame(root, bg="#2c2c2c", width=200)
menu.pack(side="left", fill="y")

painel_principal = tk.Frame(root, bg="#333")
painel_principal.pack(side="right", fill="both", expand=True)


botoes = [
    ("Hotel", lambda: abrir_janela(tela_hotel)),
    ("Passagem", lambda: abrir_janela(tela_passagem)),
    ("Relatório", lambda: abrir_janela(tela_relatorio)),
    ("Chatbot", lambda: abrir_janela(tela_chatbot)),
    ("Gráfico Faturamento", gerar_grafico_faturamento)  # ✅ Correto, sem abrir_janela
]


for texto, comando in botoes:
    btn = tk.Button(menu, text=texto, bg="#2e8bcc", fg="white",
                    font=("Arial", 12), width=20, command=comando)
    btn.pack(pady=10)


root.mainloop()
