from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import asyncio

TOKEN = "7515123882:AAFtuZVZqDc_W9xxGWgJkmj1P9kxjN4u-Oc"
NUM_MESSAGGI = 100
MESSAGGIO = "caccapupu"

async def invia100(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    for i in range(NUM_MESSAGGI):
        await context.bot.send_message(chat_id=chat_id, text=f"{MESSAGGIO} ({i + 1})")
        await asyncio.sleep(1)
    await update.message.reply_text("✅ 100 messaggi inviati!")

if __name__ == "__main__":
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("invia100msg", invia100))
    app.run_polling()