from dotenv import load_dotenv, find_dotenv
from fastapi import FastAPI
from openai import AzureOpenAI
from chatbot import ChatBotManager
import JsonStructures as JS
import os

app = FastAPI()
managers = {}  # Placeholder for the game manager
manager_last_id = 0

# Initialize OpenAI client with environment variables
load_dotenv(find_dotenv()) # read local .env file
client = AzureOpenAI(
    api_version = os.getenv('API_VERSION'),
    azure_endpoint = os.getenv('AZURE_ENDPOINT'),
    api_key = os.getenv('API_KEY'),
)
model = os.getenv('MODEL')

@app.post("/chat/init")
def init_chat(chatInitRequest : JS.ChatInitRequest):
    global managers
    global manager_last_id
    managers[manager_last_id] = ChatBotManager(client = client, model = model, context = chatInitRequest.context)
    manager_last_id += 1
    return {"chatId": f"{manager_last_id}"}

@app.post("/chat/{chat_id}/system")
def chat_with_system(chat_id : int, message: str):
    return managers[chat_id].send_to_system(message.text)

@app.post("/chat/{chat_id}/npc/{npc_id}")
def chat_with_npc(chat_id : int, npc_id: str, message: str):
    return managers[chat_id].send_to_npc(npc_id, message)