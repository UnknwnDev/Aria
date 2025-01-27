from doctest import OutputChecker
import edge_tts
import asyncio
import os


class TextToSpeech:
    def __init__(self, output_file=None):
        self.engine = edge_tts  # engine for text to speech
        self.voices = asyncio.run(self.engine.list_voices())  # list of vioces
        if output_file:
            self.output_file = output_file
        else:
            self.output_file = "speech/assets/output.mp3"  # output file path

    def speak(self, text: str, voice="en-US-AvaMultilingualNeural"):
        """Speak the given text using the given voice.

        Args:
            text (str): The text to speak.
            voice (str, optional): Voice to use. Defaults to "en-US-AvaMultilingualNeural".
        """
        print("Aria is speaking...")

        asyncio.run(self.save(text, voice))
        if os.name == "nt":  # Windows
            os.system(f"start /min wmplayer {self.output_file}")
        elif "darwin" in os.sys.platform:  # macOS
            os.system(f"afplay {self.output_file}")
        else:  # Linux
            os.system(f"mpg123 {self.output_file}")

    async def save(self, text: str, voice="en-US-AvaMultilingualNeural"):
        """Save the given text to the output file.

        Args:
            text (str): text to save.
            voice (str, optional): Voice to use. Defaults to "en-US-AvaMultilingualNeural".
        """
        # print(self.output_file)
        # with open(self.output_file + "test.txt", "a") as f:
        #     f.write("TEST")
        await self.engine.Communicate(text, voice=voice).save(self.output_file)

    def list_voices(self, _print=True) -> list:
        """List all available voices."""
        return self.voices


# if __name__ == "__main__":
#     tts = TTS()

#     tts.speak("Hello my name is Aria.")
