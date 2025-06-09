import os
from fastapi import FastAPI
from dotenv import load_dotenv
from models import ChatRequest
from chat_engine import get_response
from crisy import contains_crisis_keywords,SAFETY_MESSAGE
from logger import log_chat
from doc_engine import query_documents

from fastapi.middleware import CROSMiddleware
load_dotenv()

app = FastAPI()

app.add_middleware(
    CROSMiddleware,
    allow_origins = ["*"],
    allow_credentials = True,
    allow_method = ["*"],
    allow_headers = ["*"],
)

@app.get("/")
def read_root():
    return {"message" : "welcome to ai Powerd mental health chatbot"}


@app.post("/chat")
def chat_with_memory(request:ChatRequest):
    session_id = request.session_id
    user_query = request.query

    #crisis keyword
    if contains_crisis_keywords(user_query):
        log_chat(session_id,user_query,SAFETY_MESSAGE,is_crisis=True)
        return {"response" : SAFETY_MESSAGE}
    
    #Normal LLM REsponse
    response = get_response(session_id,user_query)
    log_chat(session_id,user_query,response,is_crisis=True)
    return{"response":response}


@app.post("/doc-chat")
def chat_with_documents(request:ChatRequest):
    response = query_documents(request.query)
    return{"response":response}
