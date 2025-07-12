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