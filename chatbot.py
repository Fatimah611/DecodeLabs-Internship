# Rule-Based AI Chatbot
# Project 1 - DecodeLabs Internship
# Developer: Fatimah

responses = {
    "hello": "Hi there! How can I help you?",
    "hi": "Hey! Welcome to DecoBot!",
    "how are you": "I am a bot, but I am doing great!",
    "what is ai": "AI stands for Artificial Intelligence — machines that think!",
    "what can you do": "I can answer basic questions. Try asking about AI!",
    "what is your name?": "My name is DecoBot!",
    "who made you?": "I was built by Fatimah using Python!",
    "bye": "Goodbye! Have a great day!",
    "help": "Ask me anything! Try: hello, what is ai, bye"
}

print("=" * 40)
print("   Welcome to DecoBot ")
print("   Type 'exit' to quit")
print("=" * 40)

while True:
    raw_input_text = input("\nYou: ")
    clean_input = raw_input_text.lower().strip()

    if clean_input == "exit":
        print("DecoBot: Goodbye! See you next time! 👋")
        break

    reply = responses.get(clean_input, "Sorry, I do not understand. Type 'help' for options!")
    print("DecoBot:", reply)