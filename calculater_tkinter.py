from tkinter import *
import tkinter.font as font

root = Tk()  # Cria a janela principal
root.title("Calculadora")  # Define o título da janela
root.resizable(0,0)  # bloqueia redimensionar a janela

inp = StringVar()  # Variável para armazenar o texto de entrada na tela

# Criação da tela de entrada
screen = Entry(root, textvariable=inp, width=30, justify='right', font=("Arial", 12), bd=4)
screen.grid(row=0, column=0, columnspan=4, padx=15, pady=15, ipady=5, sticky="ew")

# Matriz de botões da calculadora
key_matrix = [["AC", u"\u221A", "/", "C"],
              ["7", "8", "9", "*"],
              ["4", "5", "6", "-"],
              ["1", "2", "3", "+"],
              ["!", "0", ".", "="]]

btn_dict = {}  # Dicionário para armazenar os botões da calculadora
ans_to_print = 0  # Variável para armazenar a resposta

# Função para calcular a expressão
def Calculate(event):
    Button = event.widget.cget("text")
    global key_matrix, inp, ans_to_print

    try:
        if Button == u"\u221A":
            ans = float(inp.get()) ** 0.5  # Cálculo da raiz quadrada
            ans_to_print = str(ans)
            inp.set(str(ans))
        elif Button == "AC":
            inp.set("")  # Limpa a entrada
        elif Button == "!":
            def fact(n):
                return 1 if n == 0 else n * fact(n-1)  # Cálculo do fatorial
            inp.set(str(fact(int(inp.get()))))
        elif Button == "C":
            inp.set(inp.get()[:-1])  # Remove o último caractere
        elif Button == "=":
            ans_to_print = str(eval(inp.get()))  # Avalia a expressão e armazena a resposta
            inp.set(ans_to_print)  # Define a resposta como entrada
        else:
            inp.set(inp.get() + str(Button))  # Concatena o texto do botão à entrada
    except:
        inp.set("Operação incorreta!")  # Exibe mensagem de erro se a operação for inválida

# Função para capturar as teclas pressionadas
def KeyInput(event):
    key = event.keysym
    if key.isdigit() or key in ['+', '-', '*', '/', '.', '!', 'Return', 'BackSpace']:
        Calculate(Button=key)


# Criação dos botões
for i in range(len(key_matrix)):
    for j in range(len(key_matrix[i])):
        # Define a cor de fundo padrão
        bg_color = "white"
        fg_color = "black"  # Cor do texto padrão   
        
        # Verifica se o botão deve ter uma cor de fundo diferente
        if key_matrix[i][j] == "AC":
            bg_color = "#FF0000"  # Vermelho para "AC"
            fg_color = "white"     # Texto branco para "AC"
        elif key_matrix[i][j] in ["C", "="]:
            bg_color = "#D3D3D3"  # Cinza claro para "C" e "="
        
        # Cria o botão com a cor de fundo e de texto definidas
        btn = Button(root, bd=1, text=str(key_matrix[i][j]), font=font.Font(size=12, weight="bold"), bg=bg_color, fg=fg_color)
        btn.grid(row=i+1, column=j, padx=5, pady=5, ipadx=5, ipady=5)
        btn.bind("<Button-1>", Calculate)

# Associa as teclas do teclado aos botões
root.bind("<KeyPress>", KeyInput) 

root.mainloop()  # Inicia o loop principal do tkinter
