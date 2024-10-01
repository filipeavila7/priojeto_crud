from conexao import*

def enviar_dados(nome, email, senha):
   criar_usuario(nome, email, senha)


def criar_usuario(nome, email, senha):
   if conn.is_connected():
        print('conectado')
        cursor = conn.cursor()
        sql = 'insert into usuario (nome, email, senha) values (%s, %s, %s)'
        values = (nome, email, senha)

        cursor.execute(sql, values)
        conn.commit()
        print('usuario cadastrado com sucesso')
        conn.close()
        cursor.close()
   else:
       print('nao conectou')



