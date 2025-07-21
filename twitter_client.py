import tweepy
from config import TWITTER_BEARER_TOKEN

client = tweepy.Client(bearer_token=TWITTER_BEARER_TOKEN)

PALABRAS_CLAVE = [
    "grupo aval", "banco de bogotá", "banco de occidente", "banco popular",
    "av villas", "dale", "corficolombiana", "porvenir"
]

def buscar_en_twitter(limit=10):
    resultados = []
    for palabra in PALABRAS_CLAVE:
        respuesta = client.search_recent_tweets(
            query=palabra,
            max_results=limit,
            tweet_fields=["created_at", "author_id", "public_metrics"]
        )
        if respuesta.data:
            for t in respuesta.data:
                resultados.append({
                    "plataforma": "twitter",
                    "autor": str(t.author_id),
                    "contenido": t.text,
                    "empresa": palabra,
                    "interacciones": t.public_metrics.get("like_count", 0),
                    "fecha_publicacion": str(t.created_at),
                    "url": f"https://twitter.com/i/web/status/{t.id}"
                })
    return resultados
