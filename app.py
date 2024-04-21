import os
import asyncio
from flask import Flask, request, jsonify
from xai_sdk.client import Client

app = Flask(__name__)

# Set your API key for XAI services securely
os.environ['XAI_API_KEY'] = 'Eh97MbeIZ4p4UjhF4D8JVyTRAZm7oErMkdePDVi1jWzNYWPq47XPUFWgqcBd0Ysa7bfaAwrHZCVxK+pzGSVBaXUvHmKzZ8F34vsqwtDpI3hKBCf3rhIz/Obwir0obKZ9PQ'

async def generate_response(text):
    client = Client()
    sampler = client.sampler

    prompt = f"Human: {text}\n\nAssistant: "

    response = []
    async for token in sampler.sample(
        prompt=prompt,
        max_len=150,
        stop_tokens=["\n"],
        temperature=0.5,
        nucleus_p=0.95
    ):
        response.append(token.token_str)
    
    return ''.join(response)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        text = data['message']

        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        response = loop.run_until_complete(generate_response(text))

        return jsonify({'response': response})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
