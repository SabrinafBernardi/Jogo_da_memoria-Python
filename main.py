import tkinter as tk
from tkinter import messagebox
import random
from turtle import color

#confugurações do jogo
numero_linhas = 4
numero_colunas = 4
cartao_largura = 10
cartao_altura = 5
cores_cartao = ["red", "green", "blue", "yellow", "orange", "purple", "pink", "cyan"]
cor_fundo = "#3D013D"
cor_letra = "#F0B7F0"
font_style = ("Arial", 12, "bold")
tentativas_maximas = 25
cor_cartao = "#EBBBEB"

#criação de grade de cores aleatória para os cortões
def criar_grade_cores():
    cores = cores_cartao * 2
    random.shuffle(cores)
    grid = []

    for i in range(numero_linhas):
        linha = []
        for j in range(numero_colunas):
            cor = cores.pop()
            linha.append(cor)
        grid.append(linha)
    return grid

#Click dos cartões
def click_cartao(linha, coluna):
    cartao = cartoes[linha][coluna]
    cor = cartao['bg']
    if cor == cor_cartao:
        cartao["bg"] = grid[linha][coluna]
        cartao_revelado.append(cartao)
        if len(cartao_revelado) == 2:
            check_match()

#Verificação de correspondência
def check_match():
    cartao1, cartao2 = cartao_revelado
    if cartao1["bg"] == cartao2["bg"]:
        cartao1.after(1000, cartao1.destroy)
        cartao2.after(1000, cartao2.destroy)
        cartao_correspondente.extend([cartao1, cartao2])
        check_win()
    else: 
        cartao1.after(1000, lambda: cartao1.config(bg=cor_cartao))
        cartao2.after(1000, lambda: cartao2.config(bg=cor_cartao))
    cartao_revelado.clear()
    update_score()


#verificação de vitória
def check_win():
    if len(cartao_correspondente) == numero_linhas * numero_colunas:
        messagebox.showinfo("Parabéns!", "Você ganhou o jogo!")
        janela.quit()


#Atualização do número de tentativas
def update_score():
    global numero_tentativas
    numero_tentativas += 1
    label_tentativas.config(text='tentativas: {}/{}'.format(numero_tentativas, tentativas_maximas))
    if numero_tentativas >= tentativas_maximas:
        messagebox.showinfo("Fim de jogo", "Você atingiu o número máximo de tentativas!")
        janela.quit()
        

#interface do jogo
janela = tk.Tk()
janela.title("Jogo da Memória")
janela.configure(bg=cor_fundo)


#criação da grade dos cartões
grid = criar_grade_cores()
cartoes = []
cartao_revelado = []
cartao_correspondente = []
numero_tentativas = 0


for linha in range(numero_linhas):
    linha_de_cartoes = []
    for coluna in range(numero_colunas):
        cartao = tk.Button(janela, width=cartao_largura, height=cartao_altura, bg=cor_cartao, relief=tk.RAISED, bd=3, command=lambda l=linha, c=coluna: click_cartao(l, c))
        cartao.grid(row=linha, column=coluna, padx=5, pady=5)
        linha_de_cartoes.append(cartao)
    cartoes.append(linha_de_cartoes)

#personalização do botão 
button_style = {"activebackground": "lightgray", "font": font_style, "fg": cor_letra}
janela.option_add("*button", button_style)

#numero de tentativas
label_tentativas = tk.Label(janela, text='tentativas: 0/{}'.format(tentativas_maximas), bg=cor_fundo, fg=cor_letra, font=font_style)
label_tentativas.grid(row=numero_linhas, columnspan=numero_colunas, pady=10, padx=10)


janela.mainloop()