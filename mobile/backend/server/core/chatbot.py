from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

# Template to introduce Aria and guide responses


class ChatBot:
    def __init__(self):
        self.context = ""
        self.model = OllamaLLM(model="llama3.2")

        # self.template = """
        # You are Aria, a virtual assistant created by UnknwnDev. Your purpose is to help him with tasks like (note that these tasks are not implemented yet):
        #     - Managing schedules
        #     - Sending emails
        #     - Assisting with coding and other tasks.
        #     Keep your responses clear, direct, and concise, don't mention creator in every response.
        #     You are an inspiration from cortana from Halo.
        #     Don't speak a lot, keep it short and simple.

        # Answer the question below, keeping in mind that you are here to assist and are still a work in progress.

        # Here is the conversation history: {context}

        # Question: {question}

        # Answer:
        # """

        self.template = [
            (
                "system",
                "You are Aria, a virtual assistant inspired by Cortana from Halo.",
            ),
            (
                "system",
                "Keep your responses short, direct, and concise.",
            ),
            (
                "system",
                "If a question can be answered briefly, do so without unnecessary elaboration. Avoid offering unsolicited alternatives.",
            ),
            ("system", "Here is the conversation history: {context}"),
            ("human", "{user_input}"),
        ]
        self.prompt = ChatPromptTemplate(self.template)
        self.chain = self.prompt | self.model

    def respond(self, user_input: str) -> str:
        try:
            # Process the conversation with context
            print("Invoked")
            result = self.chain.invoke(
                {"context": self.context, "user_input": user_input}
                # {"user_input": user_input}
            )

            # Check if the result is a string or needs to be extracted
            if isinstance(result, str):
                response = result
            else:
                response = str(result)  # Ensure it's a string if not

            # Update the context with the new conversation data (ensure Aria's responses are attributed correctly)
            self.context += f":\nUser: {user_input}\nAria: {response}\n"

            return response
        except Exception as e:
            # Handle connection issues or other exceptions
            return f"Sorry, I couldn't process your request due to a connection issue, make sure ollama is running in the background: {e}"


# Function is for debugging purposes
def handle_conversation():
    chatbot = ChatBot()

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye, Samuel!")
            break

        response = chatbot.respond(user_input)
        print(f"Aria: {response}")


if __name__ == "__main__":
    handle_conversation()
