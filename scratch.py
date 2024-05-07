# Simple Personal Assistant Chatbot
def personal_assistant():
    print("Hello! I am your personal assistant. How can I help you today?")
    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("Goodbye! Have a great day!")
            break
        else:
            print(
                "Sorry, I am a simple chatbot and can't process requests at the moment."
            )


# Start the personal assistant
personal_assistant()
