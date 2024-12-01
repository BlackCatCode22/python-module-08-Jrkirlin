import OpenAI

def generate_response(user_input):
    try:
        completion = openai.ChatCompletion.create(
            model ="gpt-3.5-turbo",
            messages = [{"role": "system", "content": "You are a Fungi herew to talk to whoever opens this app."},
                        {"role": "user", "content": user_input}]
        )

        response_text = completion["choices"][0]["message"]["content"]
        return response_text
    except Exception as e:
        print("Error generating response", e)
        return "I'm sorry, I couldn't generate a response"

def main():
    openai.api_key = "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"
    print("\nWelcome to the Jordan's Fungi Bot! Type 'quit' to exit.\n")

    while True:
        user_input = input("Nerd student question: ")

        if user_input.lower() == "quit":
            print("Adios, Muchacho.")
            break

        response = generate_response(user_input)

        print("Fungi Bot:", response)

if __name__ == "__main__":
    main()