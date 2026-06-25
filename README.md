# french-tech
French Tech AI Engine - A Mistral AI and Hugging Face powered NLP platform for French language processing
# french-tech

French Tech AI Engine - A Mistral AI and Hugging Face powered NLP platform for French language processing

## Overview

**french-tech** is a cutting-edge Natural Language Processing (NLP) engine specifically designed for French language processing. It seamlessly integrates **Mistral AI** models with **Hugging Face** transformers to provide powerful language understanding and generation capabilities for French text.

## Features

- **Mistral AI Integration**: Leverage state-of-the-art Mistral AI models for chat and text generation
- - **Hugging Face Models**: Access to pre-trained multilingual models optimized for French
  - - **Sentiment Analysis**: Analyze sentiment in French text with high accuracy
    - - **Multi-task NLP**: Support for various NLP tasks including classification and embeddings
      - - **Configurable**: Easy-to-use configuration system for customizing models and settings
        - - **Caching**: Built-in model caching for improved performance
          - - **REST API**: Simple Flask-based API for easy integration
           
            - ## Installation
           
            - ### Prerequisites
            - - Python 3.8+
              - - pip or conda
               
                - ### Setup
               
                - 1. Clone the repository:
                  2. ```bash
                     git clone https://github.com/wecanmoove/french-tech.git
                     cd french-tech
                     ```

                     2. Create a virtual environment:
                     3. ```bash
                        python -m venv venv
                        source venv/bin/activate  # On Windows: venv\\Scripts\\activate
                        ```

                        3. Install dependencies:
                        4. ```bash
                           pip install -r requirements.txt
                           ```

                           4. Set up environment variables:
                           5. ```bash
                              cp .env.example .env
                              ```

                              5. Add your Mistral API key:
                              6. ```bash
                                 export MISTRAL_API_KEY="your-api-key-here"
                                 ```

                                 ## Quick Start

                                 ```python
                                 from src.mistral_engine import FrenchTechEngine

                                 # Initialize the engine
                                 engine = FrenchTechEngine()

                                 # Chat with the engine
                                 response = engine.chat("Bonjour, peux-tu m'aider avec le traitement du langage naturel?")
                                 print(response)

                                 # Sentiment analysis
                                 result = engine.sentiment_analysis("J'aime beaucoup ce produit!")
                                 print(result)
                                 ```

                                 ## Project Structure

                                 ```
                                 french-tech/
                                 ├── src/
                                 │   ├── mistral_engine.py      # Main Mistral AI integration
                                 │   ├── config.py               # Configuration settings
                                 │   └── __init__.py            # Package initialization
                                 ├── requirements.txt            # Python dependencies
                                 ├── .gitignore                 # Git ignore rules
                                 ├── README.md                  # This file
                                 └── .env.example               # Environment variables template
                                 ```

                                 ## Configuration

                                 Edit `src/config.py` or set environment variables:

                                 - `MISTRAL_API_KEY`: Your Mistral API key
                                 - - `MISTRAL_MODEL`: Model to use (default: mistral-small)
                                   - - `HF_MODEL_NAME`: Hugging Face model for sentiment analysis
                                     - - `DEBUG`: Enable debug mode (default: False)
                                      
                                       - ## Dependencies
                                      
                                       - - **mistral-common** >= 0.4.0 - Mistral AI common utilities
                                         - - **mistralai** >= 0.1.0 - Mistral AI API client
                                           - - **transformers** >= 4.35.0 - Hugging Face transformers
                                             - - **torch** >= 2.0.0 - PyTorch for deep learning
                                               - - **huggingface-hub** >= 0.19.0 - Hugging Face hub utilities
                                                 - - **Flask** >= 3.0.0 - Web framework for API
                                                   - - **python-dotenv** >= 1.0.0 - Environment variable management
                                                    
                                                     - ## License
                                                    
                                                     - This project is licensed under the MIT License.
                                                    
                                                     - ## Contributing
                                                    
                                                     - Contributions are welcome! Please feel free to submit a Pull Request.
                                                    
                                                     - ## Support
                                                    
                                                     - For issues, questions, or suggestions, please open an issue on GitHub.
                                                    
                                                     - ---

                                                     **Made with ❤️ by French Tech Community**
