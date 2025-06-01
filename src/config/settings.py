"""Application settings and configuration."""
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# API Keys
SERPER_API_KEY = os.getenv("SERPER_API_KEY")

# Application settings
DEBUG = os.getenv("DEBUG", "False").lower() == "true"
ENV = os.getenv("ENV", "development")

# Model settings
DEFAULT_MODEL = os.getenv("DEFAULT_MODEL", "gpt-4o")

# Define configuration based on environment
def get_config():
    """Return configuration based on current environment."""
    return {
        "debug": DEBUG,
        "environment": ENV,
        "model": DEFAULT_MODEL,
        "serper_api_key": SERPER_API_KEY,
    }
