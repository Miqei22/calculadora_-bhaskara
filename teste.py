import matplotlib.pyplot as plt
import numpy as np
import math
import tkinter as tk
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

# Variáveis globais
modo_atual = "claro"

# Dicionário de modos (substitui o módulo modos.py)
MODOS = {
    "claro": {
        "bg": "#f0f0f0",
        "fg": "#000000",
        "entry_bg": "#ffffff",
        "entry_fg": "#000000",
        "text_bg": "#ffffff",
        "text_fg": "#000000",
        "button_bg": "#ffffff",
        "button_fg": "#000000"
    },
    "escuro": {
        "bg": "#2d2d2d",
        "fg": "#ffffff",
        "entry_bg": "#3d3d3d",
        "entry_fg": "#ffffff",
        "text_bg": "#3d3d3d",
        "text_fg": "#ffffff",
        "button_bg": "#ffffff",
        "button_fg": "#000000"
    }
}

def aplicar_modo(janela, widgets, modo):
    """Aplica o tema claro/escuro a todos os widgets"""
    cores = MODOS[modo]
    janela.config(bg=cores["bg"])
    
    for widget_type, widget in widgets:
        if widget_type == "frame":
            widget.config(bg=cores["bg"])
        elif widget_type == "label":
            widget.config(bg=cores["bg"], fg=cores["fg"])
        elif widget_type == "entry":
            widget.config(bg=cores["entry_bg"], fg=cores["entry_fg"],
                          insertbackground=cores["fg"])
        elif widget_type == "text":
            widget.config(bg=cores["text_bg"], fg=cores["text_fg"],
                          insertbackground=cores["fg"])
        elif widget_type == "button":
            widget.config(bg=cores["button_bg"], fg=cores["button_fg"],
                         activebackground=cores["fg"], activeforeground=cores["bg"])
        elif widget_type == "scrollbar":
            widget.config(bg=cores["button_bg"], troughcolor=cores["bg"],
                         activebackground=cores["fg"])

def alternar_modo():
    global modo_atual
    modo_atual = "escuro" if modo_atual == "claro" else "claro"
    
    widgets = [
        ("frame", frame_principal),
        ("frame", frame_historico),
        ("label", rotulo_a),
        ("label", rotulo_b),
        ("label", rotulo_c),
        ("label", resultado_delta),
        ("label", resultado_x1),
        ("label", resultado_x2),
        ("label", historico_label),
        ("entry", entrada_a),
        ("entry", entrada_b),
        ("entry", entrada_c),
        ("text", historico_text),
        ("button", botao_calcular),
        ("button", botao_limpar),
        ("button", botao_modo),
        ("button", botao_grafico),
        ("scrollbar", scrollbar),
    ]

    aplicar_modo(janela, widgets, modo_atual)
    botao_modo.config(text="Modo Claro" if modo_atual == "escuro" else "Modo Escuro")

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
        
        resultado_delta.config(text=f"Delta (Δ): {delta:.4f}")
        resultado_x1.config(text=f"x1: {x1:.4f}")
        resultado_x2.config(text=f"x2: {x2:.4f}")
        
        historico_text.config(state="normal")
        historico_text.insert(tk.END, f"Equação: {a}x² + {b}x + {c}\n")
        historico_text.insert(tk.END, f"Delta (Δ): {delta:.4f}\n")
        historico_text.insert(tk.END, f"x1: {x1:.4f}\n")
        historico_text.insert(tk.END, f"x2: {x2:.4f}\n")
        historico_text.insert(tk.END, "-"*30 + "\n")
        historico_text.config(state="disabled")
        
        if a != 0:
            botao_grafico.config(state=tk.NORMAL)
        else:
            botao_grafico.config(state=tk.DISABLED)
            
    except ValueError:
        botao_grafico.config(state=tk.DISABLED)
        messagebox.showerror("Erro", "Por favor, insira valores válidos para A, B e C.")

def limpar_historico():
    confirmacao = messagebox.askyesno("Confirmar", "Tem certeza que deseja limpar o histórico?")
    if confirmacao:
        historico_text.delete(1.0, tk.END)

def mudar_foco(event):
    widget_atual = event.widget
    proximo_widget = widget_atual.tk_focusNext()
    if proximo_widget:
        proximo_widget.focus()
    return "break"

def plotar_grafico():
    try:
        a = float(entrada_a.get())
        b = float(entrada_b.get())
        c = float(entrada_c.get())
        
        if a == 0:
            messagebox.showerror("Erro", "O coeficiente 'a' não pode ser zero!")
            return
        
        top = tk.Toplevel(janela)
        top.title(f"Gráfico: {a}x² + {b}x + {c}")
        top.geometry("800x600")
        
        fig = Figure(figsize=(8, 6), dpi=100)
        ax = fig.add_subplot(111)
        
        delta = b**2 - 4*a*c
        x_range = max(5, abs(-b/(2*a))) + 2
        x = np.linspace(-x_range, x_range, 400)
        y = a*x**2 + b*x + c
        
        line_color = '#1f77b4' if modo_atual == "claro" else '#4ec9b0'
        ax.plot(x, y, label=f'f(x) = {a}x² + {b}x + {c}', color=line_color, linewidth=2)
        ax.set_title('Gráfico da Função Quadrática', pad=20)
        ax.set_xlabel('x')
        ax.set_ylabel('f(x)')
        ax.grid(True, linestyle='--', alpha=0.7)
        ax.axhline(0, color='red' if modo_atual == "claro" else 'white', linewidth=0.5)
        ax.axvline(0, color='red' if modo_atual == "claro" else 'white', linewidth=0.5)
        ax.legend()
        
        if delta >= 0:
            x1 = (-b + math.sqrt(delta))/(2*a)
            x2 = (-b - math.sqrt(delta))/(2*a)
            ax.scatter([x1, x2], [0, 0], color='red', s=100, label='Raízes')
            ax.annotate(f'({x1:.2f}, 0)', (x1, 0), textcoords="offset points", xytext=(0,10), ha='center')
            ax.annotate(f'({x2:.2f}, 0)', (x2, 0), textcoords="offset points", xytext=(0,10), ha='center')
        
        xv = -b/(2*a)
        yv = a*xv**2 + b*xv + c
        ax.scatter(xv, yv, color='green', s=100, label='Vértice')
        ax.annotate(f'Vértice\n({xv:.2f}, {yv:.2f})', (xv, yv), 
                   textcoords="offset points", xytext=(0,-15), ha='center')
        
        canvas = FigureCanvasTkAgg(fig, master=top)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        
        btn_fechar = tk.Button(top, text="Fechar", command=top.destroy)
        btn_fechar.pack(side=tk.BOTTOM, pady=10)
        
    except ValueError:
        messagebox.showerror("Erro", "Valores inválidos para plotar o gráfico")

# Configuração da janela principal
janela = tk.Tk()
janela.title("Calculadora de Bhaskara")
janela.geometry("700x800")

# Estilo dos widgets
estilo_botao = {
    "activebackground": "#555555",
    "activeforeground": "#ffffff",
    "borderwidth": 1,
    "relief": "raised",                
    "padx": 10,
    "pady": 5,
    "font": ("Arial", 10)
}

# Configuração de grid
janela.columnconfigure(0, weight=1)
janela.rowconfigure(0, weight=1)
janela.rowconfigure(1, weight=1)

# Frame principal
frame_principal = tk.Frame(janela)
frame_principal.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
frame_principal.columnconfigure(1, weight=1)

# Componentes da interface
botao_modo = tk.Button(frame_principal, text="Modo Escuro", command=alternar_modo, **estilo_botao)
botao_modo.grid(row=0, column=2, padx=10, pady=10, sticky="e")

rotulo_a = tk.Label(frame_principal, text="Valor de A:")
rotulo_a.grid(row=0, column=0, padx=10, pady=10, sticky="w")
entrada_a = tk.Entry(frame_principal)
entrada_a.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
entrada_a.bind("<Return>", mudar_foco)

rotulo_b = tk.Label(frame_principal, text="Valor de B:")
rotulo_b.grid(row=1, column=0, padx=10, pady=10, sticky="w")
entrada_b = tk.Entry(frame_principal)
entrada_b.grid(row=1, column=1, padx=10, pady=10, sticky="ew")
entrada_b.bind("<Return>", mudar_foco)

rotulo_c = tk.Label(frame_principal, text="Valor de C:")
rotulo_c.grid(row=2, column=0, padx=10, pady=10, sticky="w")
entrada_c = tk.Entry(frame_principal)
entrada_c.grid(row=2, column=1, padx=10, pady=10, sticky="ew")
entrada_c.bind("<Return>", lambda e: calcular_raizes())

botao_calcular = tk.Button(frame_principal, text="Calcular Raízes", command=calcular_raizes, **estilo_botao)
botao_calcular.grid(row=3, column=0, columnspan=2, pady=10, sticky="ew")

botao_grafico = tk.Button(frame_principal, text="Mostrar Gráfico", command=plotar_grafico, **estilo_botao)
botao_grafico.grid(row=3, column=2, pady=10, sticky="ew")
botao_grafico.config(state=tk.DISABLED)

resultado_delta = tk.Label(frame_principal, text="Delta (Δ): ")
resultado_delta.grid(row=4, column=0, columnspan=3, pady=10, sticky="w")

resultado_x1 = tk.Label(frame_principal, text="x1: ")
resultado_x1.grid(row=5, column=0, columnspan=3, pady=10, sticky="w")

resultado_x2 = tk.Label(frame_principal, text="x2: ")
resultado_x2.grid(row=6, column=0, columnspan=3, pady=10, sticky="w")

# Frame de histórico
frame_historico = tk.Frame(janela)
frame_historico.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
frame_historico.columnconfigure(0, weight=1)
frame_historico.rowconfigure(1, weight=1)

historico_label = tk.Label(frame_historico, text="Histórico de Resultados:")
historico_label.grid(row=0, column=0, sticky="w")

historico_text = tk.Text(frame_historico, height=10, width=50)
historico_text.grid(row=1, column=0, sticky="nsew")
historico_text.config(state="disabled")

scrollbar = tk.Scrollbar(frame_historico, command=historico_text.yview)
scrollbar.grid(row=1, column=1, sticky="ns")
historico_text.config(yscrollcommand=scrollbar.set)

botao_limpar = tk.Button(frame_historico, text="Limpar Histórico", command=limpar_historico, **estilo_botao)
botao_limpar.grid(row=2, column=0, pady=5, sticky="ew")

# Inicialização
alternar_modo()
janela.mainloop()