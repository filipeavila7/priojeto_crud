import mysql 
import mysql.connector

conn = mysql.connector.connect(
  host="localhost",
  user="shipin",
  password="projeto123",
  db="projeto_crud"
  
)

if conn.is_connected():
    print('conectado mano')
else:
    print('nao conectou mano')