import sqlite3

def init_database():
    conn=sqlite3.connect("LunaCare.db")
    cur=conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS cycle(
    id INTEGER PRIMARY KEY,
    date TEXT,
    cycle INTEGER
    )
    """)
    conn.commit()
    conn.close()