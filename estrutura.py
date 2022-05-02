import email
from tkinter import *
from tkinter.tix import Tree
from turtle import width
from tkinter.filedialog import askopenfilename

# Interface Grafica :


def enviar():
        pass

def anexar():
    Tk().withdraw() # Isto torna oculto a janela principal
    filename = askopenfilename() # Isto te permite selecionar um arquivo
    print(filename) # printa o arquivo selecionado

def sair():
    pass

janela = Tk()
botao= Button(janela,text="sair",command=sair)
botao.place(x=40,y=15)

destinatario = Entry(janela,)
destinatario.place(x=100,y=100)
label_destinatario = Label(janela,text="Destinatario: ")
label_destinatario.place(x=30,y=100)

assunto = Entry(janela,)
assunto.place(x=100,y=140)
label_assunto = Label(janela,text="Assunto: ")
label_assunto.place(x=30,y=140)

mensagem = Entry(janela,)
mensagem.place(x=100,y=190)
label_mensagem = Label(janela,text="mensagem: ")
label_mensagem.place(x=30,y=190)

bt= Button(janela,text="Enviar",command=enviar)
bt.place(x=160,y=250)

bt= Button(janela,text="Anexar Arquivo",command=anexar)
bt.place(x=40,y=250)

janela.geometry("300x300+200+200")
janela.title("Novo E-mail:")
janela.mainloop()

