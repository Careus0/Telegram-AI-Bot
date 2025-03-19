from telegram import Update
from telegram.ext import CallbackContext
from services.openrouter_service import OpenRouterService
from models.conversation import ConversationManager
from utils.markdown_utils import escape_markdown
import logging

logger = logging.getLogger(__name__)

class MessageHandlers:
    def __init__(self):
        self.openrouter_service = OpenRouterService()
        self.conversation_manager = ConversationManager()

    async def chat(self, update: Update, context: CallbackContext) -> None:
        try:
            user_id = update.message.from_user.id
            user_message = update.message.text

            context_messages = self.conversation_manager.get_context(user_id)
            bot_response = self.openrouter_service.get_response(user_message, context_messages)

            self.conversation_manager.update_context(user_id, user_message, bot_response)
            
            await update.message.reply_text(
                escape_markdown(bot_response),
                parse_mode="MarkdownV2",
                disable_web_page_preview=True
            )
        except Exception as e:
            logger.error(f"Error in chat handler: {e}")
            await update.message.reply_text("Maaf, terjadi kesalahan dalam memproses pesan Anda.")
