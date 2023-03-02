from menu import *
from conexao import conexao

def resposta(num: str) -> str: 
    
    sql="select * from cidade"
    
    cursor = conexao.cursor()
    
    if num == 2:
        cursor.execute(sql)
        
        resultados = cursor.fetchall()
        
        cursor.close()
        conexao.close()

        num = resultados
        
    return num
        