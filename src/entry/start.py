from src.discord.client import Client
from src.entry.firebase.initialize import initialize

initialize_firebase = initialize


def start():
    bot_client = Client()
    bot_client.launch()

    initialize_firebase()
