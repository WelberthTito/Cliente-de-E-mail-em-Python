from tkinter import *

from sqlalchemy import false

# Função do login :

def close_window():
    janela.destroy()

def login ():
    if (usuario.get()=="123" and senha.get()=="123"):
        lb["text"] = "Login efetuado com sucesso!"
        import estrutura
        close_window
    else:
        lb["text"] = "Login inválido!"


# Interface Grafica :

janela = Tk()

usuario = Entry(janela,)
usuario.place(x=100,y=100)
label_usuario = Label(janela,text="Usuário: ")
label_usuario.place(x=30,y=100)

senha = Entry(janela,)
senha.place(x=100,y=140)
label_usuario = Label(janela,text="Senha: ")
label_usuario.place(x=30,y=140)



bt= Button(janela,text="Fazer Login",command=login)
bt.place(x=40,y=190)

lb = Label (janela,text="Aguardando dados...")
lb.place(x=40,y=250)



janela.geometry("300x300+200+200")
janela.title("Login")
janela.mainloop()