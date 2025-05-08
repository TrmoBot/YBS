from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
from ybs_bot.route_finder import find_routes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Welcome to YBS Route Finder Bot! Send me a message like 'From Thamine to Myaynigone'.")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_input = update.message.text
    response = find_routes(user_input)
    await update.message.reply_text(response)

def main():
    app = ApplicationBuilder().token("7646184792:AAFcb7wWC4pElnOt0XOIebrKeEvBGVUwZVo").build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()

if __name__ == "__main__":
    main()
