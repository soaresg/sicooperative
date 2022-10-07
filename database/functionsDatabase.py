from database.connect import connect

conn = connect()

def executeInsertQuery(query):
    
    cur = conn.cursor()
    
    cur.execute(query)
    conn.commit()
    
    cur.close()

def executeSelectQuery(query):
    
    cur = conn.cursor()
    
    cur.execute(query)
    
    return cur.fetchall()

def closeConnection():
    conn.close()
