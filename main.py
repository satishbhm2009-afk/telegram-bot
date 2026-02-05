import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, MessageHandler, ContextTypes, filters

ADMIN_ID = int(os.environ.get("1812820539"))

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📊 Stats", callback_data="stats")],
        [InlineKeyboardButton("ℹ️ About", callback_data="about")]
    ]
    await update.message.reply_text(
        "👋 Welcome!\nMenu choose karein 👇",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def admin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != 1812820539:
        await update.message.reply_text("⛔ Admin only.")
        return
    await update.message.reply_text("✅ Admin panel ready")

async def stats(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != 1812820539:
        await update.message.reply_text("⛔ Permission denied.")
        return
    await update.message.reply_text("📊 Bot running 24×7 on Railway 🚆")

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    q = update.callback_query
    await q.answer()
    if q.data == "stats":
        if q.from_user.id != 1812820539:
            await q.edit_message_text("⛔ Admin only.")
        else:
            await q.edit_message_text("📊 Stats OK")
    elif q.data == "about":
        await q.edit_message_text("🤖 Telegram Bot\nPowered by Railway")

async def auto_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🙏 /start likh kar menu open karein")

app = ApplicationBuilder().token(os.environ.get("BOT_TOKEN")).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("admin", admin))
app.add_handler(CommandHandler("stats", stats))
app.add_handler(CallbackQueryHandler(button))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, auto_reply))

app.run_polling()
