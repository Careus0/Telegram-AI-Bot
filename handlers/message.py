from telegram import Update
from telegram.ext import CallbackContext
from services.openrouter import OpenRouterService
from models.conversation import ConversationManager
from utils.markdown import escape_markdown
import logging
import asyncio

logger = logging.getLogger(__name__)

class MessageHandlers:
    def __init__(self):
        self.openrouter_service = OpenRouterService()
        self.conversation_manager = ConversationManager()

    async def chat(self, update: Update, context: CallbackContext) -> None:
        try:
            user_id = update.message.from_user.id
            user_message = update.message.text

            # Animasi loading
            dots = ["Thinking", "Thinking.", "Thinking..", "Thinking..."]
            processing_message = await update.message.reply_text(dots[0])
            
            # Update pesan setiap 0.5 detik
            for i in range(1, 4):
                await processing_message.edit_text(dots[i])
                await asyncio.sleep(0.5)
                
            context_messages = self.conversation_manager.get_context(user_id)
            bot_response = self.openrouter_service.get_response(user_message, context_messages)

            self.conversation_manager.update_context(user_id, user_message, bot_response)

            await processing_message.edit_text(
                escape_markdown(bot_response),
                parse_mode="MarkdownV2",
                disable_web_page_preview=True
            )
        except Exception as e:
            logger.error(f"Error in chat handler: {e}")
            await update.message.reply_text("Maaf, terjadi kesalahan dalam memproses pesan Anda.")