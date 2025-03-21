import nltk
from nltk.chat.util import Chat, reflections
pairs = [
    (r"hi|hello|hey", ["Hello!", "Hi there!", "Hey!"]),
    (r"how are you?", ["I'm good, thanks!", "I'm doing well. How about you?"]),
    (r"what is your name?|who are you", ["I'm a chatbot built using NLTK."]),
    (r"quit", ["Goodbye!", "See you later!", "Bye!"])
]

chatbot = Chat(pairs, reflections)
def chatbot_response():
    print("Chatbot: Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            print("Chatbot: Goodbye!")
            break
        response = chatbot.respond(user_input)
        print("Chatbot:", response)

chatbot_response()
