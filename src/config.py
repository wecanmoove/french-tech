"""
Configuration settings for French Tech AI Engine
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Mistral Configuration
MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY", "")
MISTRAL_MODEL = os.getenv("MISTRAL_MODEL", "mistral-small")
MISTRAL_TIMEOUT = int(os.getenv("MISTRAL_TIMEOUT", "30"))

# Hugging Face Configuration
HF_MODEL_NAME = os.getenv("HF_MODEL_NAME", "distilbert-base-multilingual-cased")
HF_CACHE_DIR = os.getenv("HF_CACHE_DIR", ".cache/huggingface")
HF_TOKEN = os.getenv("HF_TOKEN", "")

# Application Settings
APP_NAME = "French Tech AI Engine"
APP_VERSION = "0.1.0"
DEBUG = os.getenv("DEBUG", "False").lower() == "true"
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

# Server Configuration
HOST = os.getenv("HOST", "0.0.0.0")
PORT = int(os.getenv("PORT", "5000"))

# Model Cache Settings
ENABLE_MODEL_CACHE = os.getenv("ENABLE_MODEL_CACHE", "True").lower() == "true"
CACHE_DIR = os.getenv("CACHE_DIR", "./model_cache")
MAX_CACHE_SIZE = int(os.getenv("MAX_CACHE_SIZE", "10"))  # GB

# French Language Specific
LANGUAGE = "fr"
LANGUAGE_CODE = "fra"

def validate_config():
      """Validate required configuration settings"""
      if not MISTRAL_API_KEY:
                raise ValueError("MISTRAL_API_KEY environment variable is required")

      return True
