import sys
import os

# Add the backend directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../backend")))

from backend.client.app import AriaClient

# Initialize the AriaClient
client = AriaClient(output_file="./assets/output.mp3")


def ping_server():
    """
    Calls the ping_server function of AriaClient.
    """
    client.ping_server()


def send_voice_query(query):
    """
    Calls the send_voice_query function of AriaClient with the given query.
    """
    client.run()
    # client.send_voice_query(query)
