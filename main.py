from fastapi import FastAPI
from app.models_manager import get_model
from app.ask_types import Question, Analysis
from pydantic import BaseModel, Field
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

# Charger les variables d'environnement depuis .env
load_dotenv()

app = FastAPI()

@app.post("/ask")
async def ask(question: Question):
    # Create a parser for structured output based on the Analysis model
    parser = PydanticOutputParser(pydantic_object=Analysis)
    # Create a prompt template that includes format instructions from the parser
    prompt = ChatPromptTemplate.from_template(
        "Analyze the following customer question.\n{format_instructions}\nQuestion: {question}"
    )
    prompt = prompt.partial(format_instructions=parser.get_format_instructions())
    # Initialize the language model
    model = get_model()
    chain = prompt | model | parser
    ## Result : a pydantic object, not a string
    resultat = chain.invoke({"question": question.question})

    return resultat

