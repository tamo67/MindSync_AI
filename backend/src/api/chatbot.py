def chatbot_response(input_text):
    return f"Response: {input_text}"

if __name__ == "__main__":
    user_input = input("You: ")
    print(f"Chatbot: {chatbot_response(user_input)}")
