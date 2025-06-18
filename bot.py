from telegram import Update, Bot
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import time
import threading
from fastapi import FastAPI
import uvicorn

TOKEN = "7515123882:AAFtuZVZqDc_W9xxGWgJkmj1P9kxjN4u-Oc"
NUM_MESSAGGI = 100
MESSAGGIO = "caccapupu"

app = FastAPI()
bot = Bot(token=TOKEN)
telegram_app = ApplicationBuilder().token(TOKEN).build()

async def invia_messaggi(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    for i in range(NUM_MESSAGGI):
        await bot.send_message(chat_id=chat_id, text=f"{MESSAGGIO} ({i + 1})")
        time.sleep(1)
    await update.message.reply_text("✅ Messaggi inviati!")

telegram_app.add_handler(CommandHandler("invia100msg", invia_messaggi))

@app.get("/")
def read_root():
    return {"message": "Bot Telegram attivo"}

if __name__ == "__main__":
    def run_telegram_bot():
        telegram_app.run_polling()

    thread = threading.Thread(target=run_telegram_bot)
    thread.start()

    uvicorn.run(app, host="0.0.0.0", port=10000)
