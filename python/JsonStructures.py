from pydantic import BaseModel

class ChatInitRequest(BaseModel):
    context: str