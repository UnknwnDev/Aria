import logging
from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from utils.helpers import ping_server, send_voice_query

# Configure logging
logging.basicConfig(level=logging.DEBUG)


class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super(HomeScreen, self).__init__(**kwargs)
        logging.debug("Initializing HomeScreen")
        layout = BoxLayout(orientation="vertical")

        ping_button = Button(text="Ping Server")
        ping_button.bind(on_press=self.ping_server)

        query_button = Button(text="Send Voice Query")
        query_button.bind(on_press=self.send_voice_query)

        layout.add_widget(ping_button)
        layout.add_widget(query_button)

        hello_label = Label(text="Hello, World!")
        layout.add_widget(hello_label)

        self.add_widget(layout)

    def ping_server(self, instance):
        try:
            logging.debug("Pinging server...")
            ping_server()
            logging.debug("Ping successful")
        except Exception as e:
            logging.error(f"Error pinging server: {e}")

    def send_voice_query(self, instance):
        try:
            query = "Hello, Aria!"  # Replace with actual query
            logging.debug(f"Sending voice query: {query}")
            send_voice_query(query)
            logging.debug("Voice query sent successfully")
        except Exception as e:
            logging.error(f"Error sending voice query: {e}")
