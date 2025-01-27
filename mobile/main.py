import logging
from kivy.app import App
from screens.HomeScreen import HomeScreen  # Import the HomeScreen class

# Configure logging
logging.basicConfig(level=logging.DEBUG)


class MyApp(App):
    def build(self):
        logging.debug("Building HomeScreen")
        return HomeScreen()  # Return an instance of HomeScreen

    def run(self):
        self.build()


if __name__ == "__main__":
    logging.debug("Starting MyApp")
    MyApp().run()
