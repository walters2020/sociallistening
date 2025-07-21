from reddit_client import buscar_en_reddit
from twitter_client import buscar_en_twitter
from db import crear_db, guardar
import schedule
import time
import datetime

def tarea():
    print(f">> Ejecutando búsqueda: {datetime.datetime.utcnow().isoformat()}")
    reddit = buscar_en_reddit()
    twitter = buscar_en_twitter()
    guardar(reddit + twitter)
    print(f">> Guardado exitoso: {len(reddit)} Reddit | {len(twitter)} Twitter")

if __name__ == "__main__":
    crear_db()
    tarea()  # Ejecutar una vez al inicio
    schedule.every(6).hours.do(tarea)

    print(">> Escuchando menciones cada 6 horas")
    while True:
        schedule.run_pending()
        time.sleep(60)
