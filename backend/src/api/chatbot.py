def chatbot_response(input_text):
    if input_text.lower() == "exit":
        return "Goodbye!"
    return f"Chatbot: {input_text}"

def run_chatbot():
    print("Chatbot is running! Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        response = chatbot_response(user_input)
        print(response)
        if user_input.lower() == "exit":
            break

if __name__ == "__main__":
    run_chatbot()
