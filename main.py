import os
from fastapi import FastAPI
from dotenv import load_dotenv
from models import ChatRequest
from chat_engine import get_response
from crisy import contains_crisis_keywords,SAFETY_MESSAGE