from tkinter import *
import random

window = Tk()
window.title('Jogo da Cobrinha')
window.resizable(False,False)

pontos = 0
direção = "baixo"
largura_jogo = 700
altura_jogo = 700
tamanho = 50

class Comida:
    
    def __init__(self): 
        x = random.randint(0, (largura_jogo // tamanho) - 1) * tamanho
        y = random.randint(0, (altura_jogo // tamanho) - 1) * tamanho 
        
        self.coordenadas = [x, y]
       
        canvas.create_oval(x,y, x + tamanho,y + tamanho, fill="red", tags="Comida")
label = Label(window, text=f"Pontuação:{pontos}",font=("consolas",40))
label.pack()
canvas = Canvas(window, bg="black", width=700, height=700)
canvas.pack()

comida = Comida()

window.mainloop()
largura_window = window.winfo_width()
altura_window = window.winfo_height()
largura_tela = window.winfo_screenwidth()
altura_tela = window.winfo_screenheight()
x = int((largura_window / 2) - (largura_tela / 2))
y = int((altura_window / 2) - (altura_tela / 2))
window.geometry(f'{largura_window}x{altura_window}+{x}+{y}')


window.update()
