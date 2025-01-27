import requests


class ServerRequest:
    def __init__(self, server_url):
        self.server_url = server_url

    def send_query(self, query):
        response = requests.post(f"{self.server_url}/query", json={"query": query})
        return response.json().get("response", "No response from server")
