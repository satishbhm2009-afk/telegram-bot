import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, CallbackQueryHandler, MessageHandler, ContextTypes, filters

TOKEN = os.getenv("BOT_TOKEN")
if update.effective_user.id != ADMIN_ID:


if not TOKEN or not ADMIN_ID:
    raise RuntimeError("BOT_TOKEN or ADMIN_ID missing")

if update.effective_user.id != ADMIN_ID:


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📊 Stats", callback_data="stats")],
        [InlineKeyboardButton("ℹ️ About", callback_data="about")]
    ]
    await update.message.reply_text(
        "👋 Welcome!\nMenu choose karein 👇",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def stats(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID:
        await update.message.reply_text("⛔ Admin only.")
        return
    await update.message.reply_text("📊 Bot is running on Railway 🚆")

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    q = update.callback_query
    await q.answer()
    if q.data == "stats":
        if q.from_user.id != ADMIN_ID:
            await q.edit_message_text("⛔ Admin only.")
        else:
            await q.edit_message_text("📊 Stats OK")
    elif q.data == "about":
        await q.edit_message_text("🤖 Telegram Bot\nPowered by Railway")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("stats", stats))
app.add_handler(CallbackQueryHandler(button))

app.run_polling()
