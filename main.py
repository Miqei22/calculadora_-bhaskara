import math
import tkinter as tk
from tkinter import messagebox

def calcular_raizes():
    try:
        a = float(entrada_a.get())
        b = float(entrada_b.get())
        c = float(entrada_c.get())
        
        delta = b**2 - 4*a*c
        
        if delta > 0:
            x1 = (-b + math.sqrt(delta)) / (2*a)
            x2 = (-b - math.sqrt(delta)) / (2*a)
        elif delta == 0:
            x1 = x2 = -b / (2*a)
        else:
            real = -b / (2*a)
            imaginario = math.sqrt(-delta) / (2*a)
            x1 = complex(real, imaginario)
            x2 = complex(real, -imaginario)
        
        resultado_delta.config(text=f"Delta (Δ): {delta}")
        resultado_x1.config(text=f"x1: {x1}")
        resultado_x2.config(text=f"x2: {x2}")
        
        # armazenando o resultado na aba de histórico
        historico_text.insert(tk.END, f"Equação: {a}x² + {b}x + {c}\n")
        historico_text.insert(tk.END, f"Delta (Δ): {delta}\n")
        historico_text.insert(tk.END, f"x1: {x1}\n")
        historico_text.insert(tk.END, f"x2: {x2}\n")
        historico_text.insert(tk.END, "-"*30 + "\n")
        
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores válidos para A, B e C.")

def limpar_historico():
    confirmacao = messagebox.askyesno("Confirmar", "Tem certeza que deseja limpar o histórico?")
    if confirmacao:
        historico_text.delete(1.0, tk.END)

janela = tk.Tk()
janela.title("Calculadora de Bhaskara")

# responsividade da janela
janela.columnconfigure(0, weight=1)  # coluna 0 se expande
janela.rowconfigure(0, weight=1)     # linha 0 se expande

frame_principal = tk.Frame(janela)
frame_principal.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

# responsividade do frame principal
frame_principal.columnconfigure(1, weight=1)  # coluna 1 do frame se expande

rotulo_a = tk.Label(frame_principal, text="Valor de A:")
rotulo_a.grid(row=0, column=0, padx=10, pady=10, sticky="w")
entrada_a = tk.Entry(frame_principal)
entrada_a.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

rotulo_b = tk.Label(frame_principal, text="Valor de B:")
rotulo_b.grid(row=1, column=0, padx=10, pady=10, sticky="w")
entrada_b = tk.Entry(frame_principal)
entrada_b.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

rotulo_c = tk.Label(frame_principal, text="Valor de C:")
rotulo_c.grid(row=2, column=0, padx=10, pady=10, sticky="w")
entrada_c = tk.Entry(frame_principal)
entrada_c.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

botao_calcular = tk.Button(frame_principal, text="Calcular", command=calcular_raizes)
botao_calcular.grid(row=3, column=0, columnspan=2, pady=10, sticky="ew")

resultado_delta = tk.Label(frame_principal, text="Delta (Δ): ")
resultado_delta.grid(row=4, column=0, columnspan=2, pady=10, sticky="w")

resultado_x1 = tk.Label(frame_principal, text="x1: ")
resultado_x1.grid(row=5, column=0, columnspan=2, pady=10, sticky="w")

resultado_x2 = tk.Label(frame_principal, text="x2: ")
resultado_x2.grid(row=6, column=0, columnspan=2, pady=10, sticky="w")

frame_historico = tk.Frame(janela)
frame_historico.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

# responsividade do frame de histórico
frame_historico.columnconfigure(0, weight=1)
frame_historico.rowconfigure(1, weight=1)

historico_label = tk.Label(frame_historico, text="Histórico de Resultados:")
historico_label.grid(row=0, column=0, sticky="w")

historico_text = tk.Text(frame_historico, height=10, width=50)
historico_text.grid(row=1, column=0, sticky="nsew")

# barra de rolagem ao histórico
scrollbar = tk.Scrollbar(frame_historico, command=historico_text.yview)
scrollbar.grid(row=1, column=1, sticky="ns")
historico_text.config(yscrollcommand=scrollbar.set)

botao_limpar = tk.Button(frame_historico, text="Limpar Histórico", command=limpar_historico)
botao_limpar.grid(row=2, column=0, pady=5, sticky="ew")

# responsividade da janela principal
janela.columnconfigure(0, weight=1)
janela.rowconfigure(0, weight=1)
janela.rowconfigure(1, weight=1)

janela.mainloop()