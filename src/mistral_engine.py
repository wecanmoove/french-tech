"""
French Tech AI Engine - Main Mistral Integration Module
Integrates Mistral AI models with Hugging Face transformers for French NLP tasks
"""

import os
from typing import Optional, List
from mistralai.client import MistralClient
from mistralai.models.chat_message import ChatMessage
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch


class FrenchTechEngine:
      """Main engine class for French language processing using Mistral AI and Hugging Face"""

    def __init__(self, api_key: Optional[str] = None, model_name: str = "mistral-small"):
              """
                      Initialize the French Tech Engine

                                      Args:
                                                  api_key: Mistral API key (if None, uses MISTRAL_API_KEY environment variable)
                                                              model_name: Mistral model to use (default: mistral-small)
                                                                      """
              self.api_key = api_key or os.getenv("MISTRAL_API_KEY")
              self.model_name = model_name
              self.client = MistralClient(api_key=self.api_key)
              self.conversation_history = []

    def chat(self, message: str, system_prompt: Optional[str] = None) -> str:
              """
                      Send a message to Mistral and get a response

                                      Args:
                                                  message: User message
                                                              system_prompt: Optional system prompt for context

                                                                                  Returns:
                                                                                              Model response as string
                                                                                                      """
              messages = []

        if system_prompt:
                      messages.append(ChatMessage(role="system", content=system_prompt))

        messages.append(ChatMessage(role="user", content=message))

        response = self.client.chat(
                      model=self.model_name,
                      messages=messages
        )

        return response.choices[0].message.content

    def sentiment_analysis(self, text: str, model_id: str = "distilbert-base-multilingual-cased") -> dict:
              """
                      Perform sentiment analysis on French text using Hugging Face

                                      Args:
                                                  text: French text to analyze
                                                              model_id: Hugging Face model ID

                                                                                  Returns:
                                                                                              Dictionary with sentiment analysis results
                                                                                                      """
              tokenizer = AutoTokenizer.from_pretrained(model_id)
              model = AutoModelForSequenceClassification.from_pretrained(model_id)

        inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=512)

        with torch.no_grad():
                      outputs = model(**inputs)

        logits = outputs.logits
        probabilities = torch.softmax(logits, dim=-1)

        return {
                      "text": text,
                      "scores": probabilities[0].tolist()
        }


if __name__ == "__main__":
      # Example usage
      engine = FrenchTechEngine()
      response = engine.chat("Bonjour, peux-tu m'aider avec le traitement du langage naturel en français?")
      print(f"Response: {response}")
