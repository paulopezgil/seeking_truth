class ChatBot:
    def __init__(self, context: str = "", temperature: float = 0, model: str = os.getenv('MODEL')):
        self.model = model
        self.messages = [{'role': 'system', 'content': context}]
        self.temperature = temperature

    def get_response(self, prompt: str):
        # Add the user prompt to the conversation history
        self.messages.append({'role': 'user', 'content': prompt})

        # Call the OpenAI API to get a response
        response = client.chat.completions.create(
            model=self.model,
            messages=self.messages,
            temperature=self.temperature, # this is the degree of randomness of the model's output
        ).choices[0].message.content

        # Add the assistant's response to the conversation history and return it
        self.messages.append({'role': 'assistant', 'content': response})
        return response
    
class ChatBotManager:
    def __init__(self, context : str):
        self.system_bot = ChatBot(context)
        self.npc_bots = {}  # Dictionary to store NPC bots by ID

    def get_or_create_npc(self, npc_id: str, message: str = None) -> ChatBot:
        if npc_id not in self.npc_bots:
            self.npc_bots[npc_id] = ChatBot(npc_id, personality)
        return self.npc_bots[npc_id]

    def send_to_system(self, message: str) -> str:
        return self.system_bot.respond(message)

    def send_to_npc(self, npc_id: str, message: str, personality: str = None) -> str:
        npc_bot = self.get_or_create_npc(npc_id, personality)
        return npc_bot.respond(message)

    def get_npc_history(self, npc_id: str) -> list:
        if npc_id in self.npc_bots:
            return self.npc_bots[npc_id].message_history
        return []

    def reset_all(self):
        self.system_bot.reset()
        self.npc_bots.clear()