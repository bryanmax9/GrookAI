from flask import Flask, request, jsonify
import os
from xai_sdk.client import Client
import asyncio

app = Flask(__name__)

# Use the API key from the environment variable for security
api_key = os.getenv('XAI_API_KEY', 'Eh97MbeIZ4p4UjhF4D8JVyTRAZm7oErMkdePDVi1jWzNYWPq47XPUFWgqcBd0Ysa7bfaAwrHZCVxK+pzGSVBaXUvHmKzZ8F34vsqwtDpI3hKBCf3rhIz/Obwir0obKZ9PQ')
client = Client(api_key=api_key)

async def generate_response(text):
    sampler = client.sampler
    prompt = f"Human: {text}\n\nAssistant: "
    response = ""
    try:
        async for token in sampler.sample(prompt=prompt, max_len=150, stop_tokens=["\n"], temperature=0.5, nucleus_p=0.95):
            response += token.token_str
    except Exception as e:
        print(f"An error occurred during response generation: {e}")
        return str(e)
    return response

@app.route('/message', methods=['POST'])
def message():
    data = request.get_json()
    text = data.get('message', '')  # Default to empty string if 'message' is not provided
    loop = asyncio.get_event_loop()  # Use get_event_loop to handle loop in production better
    response = loop.run_until_complete(generate_response(text))
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
