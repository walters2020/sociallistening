import tweepy
import time
from config import TWITTER_BEARER_TOKEN

client = tweepy.Client(bearer_token=TWITTER_BEARER_TOKEN)

PALABRAS_CLAVE = [
    "grupo aval", "banco de bogotá", "banco de occidente", "banco popular",
    "av villas", "dale", "corficolombiana", "porvenir"
]

def buscar_en_twitter(limit=10):
    resultados = []
    for palabra in PALABRAS_CLAVE:
        intento = 0
        max_intentos = 3
        while intento < max_intentos:
            try:
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
                # Espera corta entre términos
                time.sleep(2)
                break  # salir del ciclo si fue exitoso
            except tweepy.errors.TooManyRequests:
                intento += 1
                if intento < max_intentos:
                    print(f"[Rate limit] Esperando 15 minutos antes de reintentar '{palabra}' (intento {intento})")
                    time.sleep(15 * 60)
                else:
                    print(f"[Rate limit] Saltando término: {palabra} después de {max_intentos} intentos")
            except Exception as e:
                print(f"[Error inesperado] {palabra}: {e}")
                break
    return resultados