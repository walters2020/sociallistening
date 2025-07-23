import praw
from config import REDDIT
import datetime

reddit = praw.Reddit(
    client_id=REDDIT["client_id"],
    client_secret=REDDIT["client_secret"],
    username=REDDIT["username"],
    password=REDDIT["password"],
    user_agent=REDDIT["user_agent"]
)

PALABRAS_CLAVE = [
    "grupo aval", "banco de bogotá", "banco de occidente", "banco popular",
    "av villas", "dale", "corficolombiana", "porvenir"
]

def buscar_en_reddit(limit=10):
    resultados = []
    for palabra in PALABRAS_CLAVE:
        for post in reddit.subreddit("all").search(palabra, sort="new", limit=limit):
            resultados.append({
                "plataforma": "reddit",
                "autor": post.author.name if post.author else "unknown",
                "contenido": post.title,
                "empresa": palabra,
                "interacciones": post.score,
                "fecha_publicacion": datetime.datetime.utcfromtimestamp(post.created_utc).isoformat(),
                "url": f"https://reddit.com{post.permalink}"
            })
    return resultados
