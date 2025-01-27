from speech import tts, stt


def test_tts():
    assert tts.TTS().speak("Hello my name is Aria.") is None


def test_print_voices():
    for voice in tts.TextToSpeech().list_voices():
        print(voice)


def test_all_female_voices():
    assert tts.TextToSpeech().list_voices() is not None

    for voice in tts.TextToSpeech().list_voices():
        if voice["Gender"] == "Female":  # and "en" in voice["Locale"]:
            print(voice["Name"])
            tts.TextToSpeech().speak(
                "Hello, I am your assistant Aria inspired by Cortana.",
                voice=voice["Name"],
            )


def test_stt():
    assert stt.STT().listen() not in [
        "Sorry, the service is unavailable.",
        "Sorry, could not understand the audio.",
    ]
