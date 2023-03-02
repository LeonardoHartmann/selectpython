import mysql.connector as mysql 

conexao = mysql.connect(
    host="localhost",
    user="root",
    password="password",
    database="pgi_teste01",
    port=3306
)