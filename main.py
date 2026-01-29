from groq import Groq
from dotenv import load_dotenv
import os

def main():
    # Load variables from .env
    load_dotenv()

    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise ValueError("GROQ_API_KEY not found in .env file")

    # Create Groq client with API key
    client = Groq(api_key=api_key)

    print("🤖 Groq Chatbot (.env based)")
    print("Type 'exit' to quit\n")

    messages = [
        {"role": "system", "content": "You are a helpful AI assistant."}
    ]

    while True:
        user_input = input("You: ").strip()
        if user_input.lower() == "exit":
            print("Bot: Goodbye 👋")
            break

        messages.append({"role": "user", "content": user_input})

        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages,
            temperature=0.7,
            max_completion_tokens=1024,
            top_p=1,
            stream=True
        )

        print("Bot:", end=" ")
        assistant_reply = ""

        for chunk in completion:
            token = chunk.choices[0].delta.content or ""
            assistant_reply += token
            print(token, end="", flush=True)

        print("\n")
        messages.append({"role": "assistant", "content": assistant_reply})


if __name__ == "__main__":
    main()
