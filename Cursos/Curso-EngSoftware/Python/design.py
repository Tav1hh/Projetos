# from tkinter import * #Importando a Biblioteca

# janela = Tk() #Criando a nossa janela principal tkinter

# texto = Label(master= janela, text='Olá, Mundo!')
# texto.place(x =50,y=100)

# janela.mainloop() #Inicializando a nossa janela

from tkinter import *

def funcClicar():
    print("IP: 192.168.01.00")

janela = Tk()

texto = Label(master=janela, text='Posso te HAckear?')
texto.pack()

botao = Button(master=janela, text="SIM", command=funcClicar)
botao.pack()

botao = Button(master=janela, text="Não", command=funcClicar)
botao.pack()

janela.mainloop()