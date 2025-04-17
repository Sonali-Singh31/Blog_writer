
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# API keys
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
NEWSDATA_API_KEY = os.getenv("NEWSDATA_API_KEY")

# Gemini model configuration
GEMINI_MODEL_NAME = os.getenv("GEMINI_MODEL_NAME", "gemini-1.5-pro")
GEMINI_TEMPERATURE = float(os.getenv("GEMINI_TEMPERATURE", "0.7"))
GEMINI_TOP_P = float(os.getenv("GEMINI_TOP_P", "0.95"))
GEMINI_TOP_K = int(os.getenv("GEMINI_TOP_K", "40"))
GEMINI_MAX_OUTPUT_TOKENS = int(os.getenv("GEMINI_MAX_OUTPUT_TOKENS", "8192"))

# Blog generation settings
DEFAULT_BLOG_SECTIONS = int(os.getenv("DEFAULT_BLOG_SECTIONS", "5"))
WORDS_PER_SECTION = int(os.getenv("WORDS_PER_SECTION", "250"))
OUTPUT_DIRECTORY = os.getenv("OUTPUT_DIRECTORY", "output")

# API retry settings
MAX_RETRIES = int(os.getenv("MAX_RETRIES", "3"))
BASE_DELAY = float(os.getenv("BASE_DELAY", "1.0"))

# Content enrichment settings
MAX_NEWS_ARTICLES = int(os.getenv("MAX_NEWS_ARTICLES", "3"))
MAX_QUOTES = int(os.getenv("MAX_QUOTES", "2"))
MAX_RELATED_KEYWORDS = int(os.getenv("MAX_RELATED_KEYWORDS", "10"))

# CLI display settings
SHOW_PROGRESS = os.getenv("SHOW_PROGRESS", "True").lower() in ("true", "1", "yes")
VERBOSE_OUTPUT = os.getenv("VERBOSE_OUTPUT", "False").lower() in ("true", "1", "yes")

# Set default values for required configurations
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY is required but not set in environment variables")