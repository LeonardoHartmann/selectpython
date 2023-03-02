from menu import *
from conexao import conexao

def resposta(num: str) -> str: 
    
    sql="select * from pessoa where nascimento <= 2005-12-31"

    cursor = conexao.cursor()
    
    if num == 1:
        cursor.execute(sql)
        
        resultados = cursor.fetchall()
        
        cursor.close()
        conexao.close()
        
        num = resultados
        
    return num
        