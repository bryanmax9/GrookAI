from flask import Flask, request, jsonify
import os
from xai_sdk.client import Client
import asyncio

app = Flask(__name__)

# Use the API key from the environment variable for security
api_key = os.getenv('XAI_API_KEY', 'default_api_key_if_not_set')  # Fallback default can be provided
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
    try:
        data = request.get_json()
        text = data['message']
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        response = loop.run_until_complete(generate_response(text))
        return jsonify({"response": response})
    except Exception as e:
        print(f"Error handling message: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # For local development with Flask's development server
    app.run(debug=True, host='0.0.0.0', port=8080)
