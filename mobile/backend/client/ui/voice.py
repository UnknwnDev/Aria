from speech.tts import TextToSpeech
from speech.stt import SpeachToText
import threading


class VoiceAssistantClient:
    def __init__(self, voice_query_callback, output_file=None):
        self.stt = SpeachToText()
        self.tts = TextToSpeech(output_file)
        self.listener_thread = threading.Thread(target=self.listen_for_hey_aria)
        self.listener_thread.daemon = True
        self.triggered = False
        self.send_voice_query = voice_query_callback

    def start_listening(self):
        self.listener_thread.start()

    def listen_for_hey_aria(self):
        while True:
            text = self.stt.listen()
            if "hey aria" in text.lower() and not self.triggered:
                print("Hey Aria detected!")
                self.send_voice_query(text)
                self.triggered = True

            elif "stop" == text.lower() and self.triggered:
                print("Stopping...")
                self.triggered = False
                self.send_voice_query("Goodbye!")

            elif self.triggered:
                self.send_voice_query(text)

    def speak(self, text):
        self.tts.speak(text)


# # Usage
# if __name__ == "__main__":
#     client = VoiceAssistantClient()
#     client.start_listening()
#     client.listener_thread.join()
