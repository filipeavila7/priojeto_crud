from tkinter import *
from tkinter import ttk      
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

    def deletar_user(email):
        email = emailentry.get()
        services.remover_usuario(email)
    
    def listar_usuario(): 
        usuarios = services.listar_usuario()

        #criar uma janela para mostrar a lista de usuario
        janela_listar = Toplevel(janela)
        janela_listar.title('Lista de usuarios')
        janela_listar.geometry('600x300')

        # criar uma threeview, vizualização da lista de usuario, show='headings' para limpar usuario
        three = ttk.Treeview(janela_listar, columns=('id', 'nome', 'email'), show='headings')
        three.heading('id', text='id')
        three.heading('nome', text='nome')
        three.heading('email', text='email')

        #criar botao de voltar que ira fechar a lista de usuaario
        voltar = Button(janela_listar, text='voltar', width=10, command = janela_listar.destroy)
        voltar.pack(fill=BOTH, expand=True, side=BOTTOM)

        three.pack(fill=BOTH, expand=True)

        #inserir os dados dos usuarios na nossa threeview
        for usuario in usuarios:
            # end insere o item no final da tabela
            three.insert('', END, values=usuario)


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

    listar = Button(janela, text= 'Listar Usuarios', width= 15, command=listar_usuario)
    listar.place(x=200, y=200)



    remover = Button(janela, text='Remover', width=10, command=lambda: deletar_user(email))
    remover.place(x = 100, y = 230)


    janela.mainloop()

if __name__ == '__main__':
    main()
