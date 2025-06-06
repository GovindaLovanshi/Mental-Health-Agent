import os
from fastapi import FastAPI
from dotenv import load_dotenv
from models import ChatRequest


load_dotenv()
OPEN_API_KEY = os.getenv("OPEN_API_KEY")
if not OPEN_API_KEY:
    raise ValueError("OPEN API KEY is not set")

#initilize llm
llm  = OpenAI(open_api_key = OPEN_API_KEY,tempreture = 0.7)

#store per user memory seson

session_memory_map = {}

def get_response(session_id:str,user_query:str):

    if session_id not in session_memory_map:
        memory = ConversationBufferMemory()
        session_memory_map[session_id] = ConversationChain(llm=llm,memory = memory,verbose = True)
    
    conversation  = session_memory_map[session_id]
    return conversation.predict(input = user_query)

