from dotenv import load_dotenv
import os

print("Loading .env...")
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("❌ API key is missing or invalid in .env!")
else:
    print(f"✅ Loaded API key: {api_key[:8]}...")  # Just showing a snippet for safety
