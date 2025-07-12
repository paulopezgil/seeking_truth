from fastapi import FastAPI
from chatbot import ChatBotManager
app = FastAPI()

manager = None  # Placeholder for the game manager

@app.post("/chat/init")
def init_chat(context: str):
    global manager
    manager = ChatBotManager(context)
    return {"status": "Chat initialized with context", "context": context}
"""
@app.post("/chat/system")
def chat_with_system(message: str):
    return system_bot.respond(message.text)

@app.post("/chat/npc/{npc_id}")
def chat_with_npc(npc_id: str, message: str):
    if npc_id not in npc_registry:
        npc_registry[npc_id] = NPCChatBot(npc_id)
    return npc_registry[npc_id].respond(message.text)
"""

