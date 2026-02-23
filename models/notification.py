from pydantic import BaseModel

class EmailSentRequest(BaseModel):
    to: str
    subject: str
    message: str