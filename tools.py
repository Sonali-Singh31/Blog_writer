import os
from typing import Any
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

def setup_gemini_model(model_name: str = None) -> Any:
   
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("❌ GEMINI_API_KEY not found in .env file.")

    # Get model name from .env if not provided
    if not model_name:
        model_name = os.getenv("GEMINI_MODEL_NAME", "gemini-1.5-pro")

    print(f"✅ Using Gemini model: {model_name}")

    genai.configure(api_key=api_key)
    return genai.GenerativeModel(model_name)

def clean_text(text: str) -> str:
    return text.strip()

def validate_markdown(text: str) -> str:
    return text
