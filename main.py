import logging
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from config import settings
from handlers.message_handlers import MessageHandlers
from handlers.command_handlers import start

# Setup logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

def main() -> None:
    try:
        application = Application.builder().token(settings.Settings.TELEGRAM_BOT_TOKEN).build()
        
        message_handlers = MessageHandlers()
        
        application.add_handler(CommandHandler("start", start))
        application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, message_handlers.chat))
            
        logger.info("Starting bot...")
        application.run_polling()
    except Exception as e:
        logger.error(f"Error in main: {e}")

if __name__ == "__main__":
    main()