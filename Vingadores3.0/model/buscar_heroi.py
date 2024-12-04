from database import Database

def verificar_heroi_no_banco(nome_heroi):
    try:
        db = Database()
        db.connect()
        
        query = "SELECT heroi_id FROM heroi WHERE nome_heroi = %s"
        resultado = db.select(query, (nome_heroi,))
        
        db.disconnect()
        
        if resultado:
            return resultado[0][0]
        else:
            return None
    
    except Exception as e:
        print(f"Erro ao consultar herói no banco: {e}")
        return None
