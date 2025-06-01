"""Main configuration file for the application."""

import os
from typing import Dict, Any
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# API configuration
API_CONFIG = {
    "title": "BlogWriter CrewAI",
    "description": "A CrewAI-based blog writer application",
    "version": "0.1.0",
    "host": os.getenv("HOST", "0.0.0.0"),
    "port": int(os.getenv("PORT", 8000)),
    "debug": os.getenv("DEBUG", "False").lower() == "true",
}

# AI model configuration
MODEL_CONFIG = {
    "default_model": os.getenv("DEFAULT_MODEL", "gpt-4o"),
    "temperature": float(os.getenv("TEMPERATURE", 0.7)),
    "max_tokens": int(os.getenv("MAX_TOKENS", 4000)),
}

# Default blog parameters
BLOG_CONFIG = {
    "default_topic": "Generative AI industry",
    "default_word_count": 2000,
}

# API Keys
API_KEYS = {
    "serper": os.getenv("SERPER_API_KEY"),
}

def get_config() -> Dict[str, Any]:
    """Get the full application configuration."""
    return {
        "api": API_CONFIG,
        "model": MODEL_CONFIG,
        "blog": BLOG_CONFIG,
        "api_keys": API_KEYS,
    }
