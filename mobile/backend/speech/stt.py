import speech_recognition as sr


class SpeachToText:
    def __init__(self):
        self.recognizer = sr.Recognizer()  # recognizer for speech to text
        self.response = ""
        self.listening = False

    def listen(self):
        """Listen to the audio and return the recognized text."""
        self.listening = True

        with sr.Microphone() as source:  # use the default microphone as the audio source
            print("Listening...")
            while self.listening:
                # listen for the first phrase and extract it into audio data
                audio = self.recognizer.listen(source)

                try:
                    # recognize speech using Google Speech Recognition
                    self.response = self.recognizer.recognize_google(audio)
                    break
                except sr.UnknownValueError:
                    self.response = "Sorry, I could not understand what you said."
                except sr.RequestError:
                    self.response = "Sorry, my speech service is down."
                    break

        return self.get_text()

    def stop_listening(self):
        """Stop listening to the audio."""
        self.listening = False

    def start_listening(self):
        """Start listening to the audio."""

        self.listening = True

    def get_text(self):
        return self.response


# if __name__ == "__main__":
#     stt = STT()
#     print(stt.listen())
