from telegram import Update
from telegram.ext import CallbackContext

async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text(
        "Halo! Saya adalah bot Telegram yang terintegrasi dengan OpenRouter. Kirimkan pesan apa pun, dan saya akan meresponsnya."
        )
