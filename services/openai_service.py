import openai

def generate_ai_response(user_message, data=None):
    # Construct the messages list for the chat model
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": user_message}
    ]

    # If additional data is provided, include it in the conversation
    if data:
        messages.append({"role": "system", "content": f"Here is some relevant data: {data}"})

    # Create a chat completion with the constructed messages
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=messages,
        max_tokens=150
    )

    return response.choices[0].message['content'].strip()