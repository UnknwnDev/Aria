from flask import Flask, request, jsonify
from server.core.chatbot import ChatBot

app = Flask(__name__)
chatbot = ChatBot()


@app.route("/ping", methods=["GET"])
def ping():
    """
    The function `ping` returns a JSON response indicating that the server is alive.
    :return: The `ping` function is returning a JSON response with the message "Server is alive!".
    """
    return jsonify({"message": "Server is alive!"})


@app.route("/chatbot", methods=["POST"])
def chat_bot():
    """
    The function `chat_bot` receives a POST request with a JSON payload containing the user's message.
    The function then processes the message and returns a JSON response with the chatbot's response.
    :return: The `chat_bot` function is returning a JSON response with the chatbot's response.
    """

    data = request.get_json()
    if not data or "query" not in data:
        return jsonify({"error": "Invalid input"}), 400

    user_message = str(data["query"])
    try:

        chatbot_response = chatbot.respond(user_message)
        if "goodbye" in user_message.lower():
            chatbot.context = ""
        return jsonify({"response": chatbot_response}), 200
    except Exception as e:
        # Log the error
        print(f"Error processing chatbot request: {e}")
        return jsonify({"error": "Internal server error"}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
