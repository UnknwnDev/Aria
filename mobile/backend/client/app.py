import requests
from client.ui.voice import VoiceAssistantClient
from client.connectivity.request import ServerRequest

SERVER_URL = "http://localhost:5002"


class AriaClient:
    def __init__(self, server_url=SERVER_URL, output_file=None):
        self.voice_assistant = VoiceAssistantClient(
            self.send_voice_query, output_file=output_file
        )
        self.server = ServerRequest(server_url)

    def ping_server(self):
        """
        The `ping_server` function sends a GET request to a server URL and prints the JSON response.
        """
        response = requests.get(f"{SERVER_URL}/ping")
        print(response.json())

    def send_voice_query(self, query):
        """
        The `send_voice_query` function captures the client's voice query, sends it to the server's /chatbot endpoint, and prints the response.
        """

        response = requests.post(f"{SERVER_URL}/chatbot", json={"query": query})
        print(response.json())
        self.voice_assistant.speak(response.json()["response"])
        return response.json()["response"]

    def run(self):
        """
        The `run` method starts the voice assistant and listens for the wake word.
        """
        self.voice_assistant.start_listening()
        self.voice_assistant.listener_thread.join()


if __name__ == "__main__":
    client = AriaClient(SERVER_URL)
    client.ping_server()
    # Example usage of send_voice_query
    # client.send_voice_query()
    client.run()
