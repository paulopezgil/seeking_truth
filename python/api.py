from dotenv import load_dotenv, find_dotenv
from fastapi import FastAPI
from openai import AzureOpenAI
from chatbot import ChatBotManager
import os

app = FastAPI()
manager = None  # Placeholder for the game manager

# Initialize OpenAI client with environment variables
load_dotenv(find_dotenv()) # read local .env file
client = AzureOpenAI(
    api_version = os.getenv('API_VERSION'),
    azure_endpoint = os.getenv('AZURE_ENDPOINT'),
    api_key = os.getenv('API_KEY'),
)
model = os.getenv('MODEL')

@app.post("/chat/init")
def init_chat(context: str):
    global manager
    manager = ChatBotManager(client = client, model = model, context = context)
    return {"status": "Chat initialized with context", "context": context}

@app.post("/chat/system")
def chat_with_system(message: str):
    return manager.send_to_system(message.text)

@app.post("/chat/npc/{npc_id}")
def chat_with_npc(npc_id: str, message: str):
    return manager.send_to_npc(npc_id, message)