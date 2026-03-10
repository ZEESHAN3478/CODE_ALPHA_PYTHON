def get_response(user_input):

    if user_input == "hello" or user_input == "hi":
        return "Hi!"

    elif user_input == "how are you":
        return "I'm fine, thanks!"

    elif user_input == "what is your name":
        return "I am a simple Python chatbot."

    elif user_input == "bye":
        return "Goodbye!"

    else:
        return "Sorry, I don't understand."


def chatbot():

    print("🤖 Chatbot: Hello! Type 'bye' to exit.")

    while True:
        user = input("You: ").lower()

        response = get_response(user)
        print("Chatbot:", response)

        if user == "bye":
            break


chatbot()