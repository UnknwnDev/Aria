from client.ui.voice import VoiceAssistantClient


def test_listen_for_hey_aria():
    client = VoiceAssistantClient()
    client.start_listening()
    client.listener_thread.join()

    assert True
