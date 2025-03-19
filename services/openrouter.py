import requests
import logging
from langdetect import detect
from config import constants, settings

logger = logging.getLogger(__name__)

class OpenRouterService:
    def get_response(self, prompt: str, context: list = None) -> str:
        try:
            user_language = detect(prompt)
            system_prompt = constants.LANGUAGE_PROMPTS.get(user_language, constants.DEFAULT_PROMPT)
            
            messages = [{"role": "system", "content": system_prompt}]
            if context:
                messages.extend(context)
            messages.append({"role": "user", "content": prompt})
            
            headers = {
                "Authorization": f"Bearer {settings.Settings.OPENROUTER_API_KEY}",
                "Content-Type": "application/json",
                "HTTP-Referer": "https://github.com/hilman120111111/Telegram-AI-Bot",
                "X-Title": "Telegram Bot"
            }
            
            data = {
                "model": "deepseek/deepseek-chat:free",
                "messages": messages
            }
            
            logger.info(f"Sending request to OpenRouter with prompt: {prompt}")
            response = requests.post(settings.Settings.OPENROUTER_API_URL, headers=headers, json=data, timeout=10)
            response.raise_for_status()
            
            return response.json()["choices"][0]["message"]["content"]
        
        except requests.exceptions.HTTPError as e:
            logger.error(f"HTTP Error: {e.response.status_code} - {e.response.text}")
            return "Maaf, saya sedang sibuk. Silakan coba lagi nanti." if e.response.status_code == 429 else "Maaf, terjadi kesalahan saat menghubungi API."
        except requests.exceptions.Timeout:
            logger.error("Request to OpenRouter timed out")
            return "Maaf, waktu permintaan ke API habis. Silakan coba lagi nanti."
        except Exception as e:
            logger.error(f"Error: {e}")
            return "Maaf, terjadi kesalahan tak terduga." 