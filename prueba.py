import praw

reddit = praw.Reddit(
    client_id="Howk6HRhHIFdAhCcLLfsHw",
    client_secret="_Q73Mmndfv5KBuMfxd4KqSdwqd3QDw",
    username="Eastern-Objective658",
    password="rjWzG974%utX",
    user_agent="ColombianBank script"
)

print("Autenticado como:", reddit.user.me())
