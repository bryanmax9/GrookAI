## GrookAI

GrookAI is a simple Flask application deployed on Heroku that utilizes the GrookAI API to generate responses to user queries. This project serves as a basic implementation of an AI-powered chatbot assistant.

##Features

    AI Response Generation: Using the GrookAI API, the application generates responses to user messages.
    Flask Web Server: The backend is built with Flask, providing a simple REST API for communication.
    Asynchronous Processing: Asynchronous processing with asyncio is employed to handle the AI response generation asynchronously.
    Heroku Deployment: The application is deployed on Heroku, making it accessible via the web.

## Usage

To use the application, you can send POST requests to the /predict endpoint with a JSON payload containing the user message. The application will respond with the generated AI response.

Example POST request:

```bash
{
    "message": "Can you help me with my homework?"
}
```

Example Response:

```bash
{
    "response": "Sure, I'd be happy to help with your homework!"
}
```

## Demo

Locally:

<img src='https://i.imgur.com/ojnENJT.png' title='Video Demo' width='' alt='Video Demo' />

Deployed:

<img src='https://i.imgur.com/5ih6r3s.png' title='Video Demo' width='' alt='Video Demo' />
