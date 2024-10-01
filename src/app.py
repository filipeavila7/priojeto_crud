from tkinter import *
import services

def main():
    def on_enviar():
       nome = nomeentry.get()
       email = emailentry.get()
       senha = senhaentry.get()
       services.enviar_dados(nome, email, senha)

       #para limpar os campos
       nomeentry.delete(0, END)
       emailentry.delete(0, END)
       senhaentry.delete(0, END)


    janela = Tk()
    janela.geometry('400x300')
    janela.title('sistema de gerenciamento de usuario')

    titulo = Label(janela, text='CRUD', font=('Arial', 20))
    titulo.pack(pady=30)

    # componentes de entrada
    #nome
    nome = Label(janela, text='Nome:')
    nome.place(x=50,y=100 )

    global nomeentry
    nomeentry = Entry(janela, width=30)
    nomeentry.place(x = 100, y = 100)

    #email
    email = Label(janela, text= 'Email:')
    email.place(x=50, y=130)

    global emailentry
    emailentry = Entry(janela, width=30)
    emailentry.place(x = 100, y = 130)

    #senha
    senha = Label(janela, text= 'Senha:')
    senha.place(x=50, y=160)

    #show para esconder a senha
    global senhaentry
    senhaentry = Entry(janela, width= 30, show="*")
    senhaentry.place(x = 100, y = 160)


    cadastar = Button(janela, text='Cadastrar', width=10, command = on_enviar)
    cadastar.place(x = 100, y = 200)

    listar = Button(janela, text= 'Listar Usuarios', width= 15)
    listar.place(x=200, y=200)


    janela.mainloop()

if __name__ == '__main__':
    main()
