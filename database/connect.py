import psycopg2

from database.config.config import config


def connect():
    conn = None
    
    try:
        params = config()
        
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)
        
        cur = conn.cursor()
        
        print('Connected...')
        
        db_version = cur.fetchone()
        
        print(db_version)
        
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    
    
    return conn
