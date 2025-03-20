from telegram import Update
from telegram.ext import CallbackContext
from config.settings import Settings
from handlers.message import ConversationManager
import logging

logger = logging.getLogger(__name__)

async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text(
        "Hi! I am a Telegram bot integrated with AI."
        )
async def stat(update: Update, context: CallbackContext) -> None:
    try:
        # Cek apakah user adalah pemilik bot
        if update.message.from_user.id != Settings.BOT_OWNER_ID:
            await update.message.reply_text("Maaf, anda tidak dapat menggunakan perintah ini.")
            return
            
        conversation_manager = ConversationManager()
        stats = {
            "total_users": len(conversation_manager.conversation_context),
            "total_messages": sum(len(messages) for messages in conversation_manager.conversation_context.values())
        }
        
        response = (
            "📊 Statistik Bot:\n"
            f"• Total Pengguna: {stats['total_users']}\n"
            f"• Total Pesan: {stats['total_messages']}"
        )
        
        await update.message.reply_text(response)
        
    except Exception as e:
        logger.error(f"Error in stat command: {e}")
        await update.message.reply_text("Maaf, terjadi kesalahan saat mengambil statistik.")