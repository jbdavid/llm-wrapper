from pydantic import BaseModel, Field
from typing import List

class Question(BaseModel):
    question: str

class Analysis(BaseModel):
    mood: str = Field(description="The mood of the customer: positive, neutral or negative")
    tags: List[str] = Field(description="List of tags associated to the ticket")
    summary: str = Field(description="A brief summary of the customer's issue")
    response: str = Field(description="A suggested response to the customer")
