from tkinter import *
import random

window = Tk()
window.title('Jogo da Cobrinha')
window.resizable(False,False)

pontos = 0
direção = "Direita"
largura_jogo = 700
altura_jogo = 700
tamanho = 30
partes = 3



class Cobra:
    
    def __init__(self):
        self.partes = partes
        self.coordenadas = []
        self.quadrados = []
        
        for i in range(0, partes):
            self.coordenadas.append([0, 0])
        
        for x, y in self.coordenadas:
            quadrado =canvas.create_rectangle(x, y, x + tamanho, y + tamanho, fill="green", tags="Cobra")
            self.quadrados.append(quadrado)

class Comida:
    
    def __init__(self): 
        x = random.randint(0, (largura_jogo // tamanho) - 1) * tamanho
        y = random.randint(0, (altura_jogo // tamanho) - 1) * tamanho 
        
        self.coordenadas = [x, y]
       
        canvas.create_oval(x,y, x + tamanho,y + tamanho, fill="red", tags="Comida")
        
def mudar_direcao(x):
    
    global direção
    
    if x == 'Esquerda':
        if direção != 'Direita':
            direção = x
    elif x == 'Direita':
        if direção != 'Esquerda':
            direção = x
    elif x == 'Cima':
        if direção != 'Baixo':
            direção = x
    elif x == 'Baixo':
        if direção != 'Cima':
            direção = x
        
def turno(comida,cobra):
    
        x, y = cobra.coordenadas[0]
        
        if direção == "Cima":
            y -= tamanho
            
        elif direção == "Baixo":
            y += tamanho
            
        elif direção == "Esquerda":
            x -= tamanho
            
        elif direção == "Direita":  
            x += tamanho
            
         
        cobra.coordenadas.insert(0, (x, y))    
        
        quadrado = canvas.create_rectangle(x, y, x + tamanho, y + tamanho, fill="green")
        cobra.quadrados.insert(0, quadrado)
        
        if x == comida.coordenadas[0] and y == comida.coordenadas[1]:
            
            global pontos
            pontos += 1
            
            label.config(text=f"Pontuação:{pontos}")
            
            canvas.delete("Comida")    

            comida = Comida()
        else:    
            del cobra.coordenadas[-1]
            
            canvas.delete(cobra.quadrados[-1])
            
            del cobra.quadrados[-1]
        if colisao(cobra):
            game_over()
        else:
            window.after(100, turno, comida, cobra)

def colisao(cobra):
    x, y = cobra.coordenadas[0]
    
    if x < 0 or x >= largura_jogo:
        return True
    elif y < 0 or y >= altura_jogo:
        return True
    
    for partes in cobra.coordenadas[1:]:
        if x == partes[0] and y == partes[1]:
            return True   
       
    return False

def game_over():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width() / 2, 
                       canvas.winfo_height() / 2,
                       font=('Consolas', 70), 
                       text='GAME OVER', 
                       fill='red', 
                       tags='Game_Over')
        
window.bind('<Left>',lambda event: mudar_direcao("Esquerda"))
window.bind('<Right>',lambda event: mudar_direcao("Direita"))
window.bind('<Up>',lambda event: mudar_direcao("Cima"))
window.bind('<Down>',lambda event: mudar_direcao("Baixo"))      
        
        
label = Label(window, text=f"Pontuação:{pontos}",font=("consolas",40))
label.pack()

canvas = Canvas(window, bg="black", width=largura_jogo, height=altura_jogo)
canvas.pack()

cobra = Cobra()
comida = Comida()
turno(comida,cobra)


window.mainloop()


largura_window = window.winfo_width()
altura_window = window.winfo_height()
largura_tela = window.winfo_screenwidth()
altura_tela = window.winfo_screenheight()
x = int((largura_window / 2) - (largura_tela / 2))
y = int((altura_window / 2) - (altura_tela / 2))


window.geometry(f'{largura_window}x{altura_window}+{x}+{y}')



window.update()
