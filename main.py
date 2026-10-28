
import os
from telegram import (
    Update,
    ReplyKeyboardMarkup,
)
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

TOKEN = os.getenv("BOT_TOKEN")

PRODUCTS = [
    ["💎 MLBB Diamonds", "🎯 PUBG UC"],
    ["🔥 Free Fire Diamonds", "🎁 Roblox Robux"],
    ["⭐ Telegram Stars", "💎 Telegram Premium"],
]

async def start(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    keyboard = PRODUCTS + [["📦 Buyurtmalar haqida"]]

    await update.message.reply_text(
        "🛍 UZGAME SHOP\n\n"
        "Assalomu alaykum!\n"
        "O'yin mahsulotini tanlang:",
        reply_markup=ReplyKeyboardMarkup(
            keyboard,
            resize_keyboard=True,
        ),
    )

async def handle_message(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    choice = update.message.text

    if choice == "📦 Buyurtmalar haqida":
        text = (
            "Buyurtma holatini bilish uchun "
            "admin bilan bog'laning."
        )
    else:
        text = (
            f"Tanlangan mahsulot: {choice}\n\n"
            "Buyurtma berish tizimi sozlanmoqda."
        )

    await update.message.reply_text(text)

def main():
    if not TOKEN:
        raise RuntimeError("BOT_TOKEN sozlanmagan!")

    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message)
    )
    app.run_polling()

if __name__ == "__main__":
    main()
