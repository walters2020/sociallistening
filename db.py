import sqlite3
import datetime

def crear_db():
    conn = sqlite3.connect("menciones.db")
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS publicaciones (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            plataforma TEXT,
            autor TEXT,
            contenido TEXT,
            empresa TEXT,
            interacciones INTEGER,
            fecha_publicacion TEXT,
            fecha_consulta TEXT,
            url TEXT
        )
    ''')
    conn.commit()
    conn.close()

def guardar(publicaciones):
    conn = sqlite3.connect("menciones.db")
    c = conn.cursor()
    for pub in publicaciones:
        c.execute('''
            INSERT INTO publicaciones 
            (plataforma, autor, contenido, empresa, interacciones, fecha_publicacion, fecha_consulta, url)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            pub["plataforma"], pub["autor"], pub["contenido"], pub["empresa"],
            pub["interacciones"], pub["fecha_publicacion"],
            datetime.datetime.utcnow().isoformat(), pub["url"]
        ))
    conn.commit()
    conn.close()
