from src.discord.client import Client
from src.entry.firebase.initialize import initialize

initialize_firebase = initialize


def start():
    initialize_firebase()

    bot_client = Client()
    bot_client.launch()
