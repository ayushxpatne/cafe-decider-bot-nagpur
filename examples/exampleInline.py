from telegram.ext import *
from telegram import *

TOKEN = "5835529587:AAEnoYniWd8LjGJFsP47xq5_QnI9OIoSe3c"

START, END = 0,1
ONE, TWO, THREE = range(3)

async def start_bot(update: Update, context= ContextTypes.DEFAULT_TYPE) -> int:
   await context.bot.send_message(chat_id=update.effective_chat.id, text="Hey, itz-a-me examples")


async def start_conversation(update: Update, context= ContextTypes.DEFAULT_TYPE) -> int:
    text = "Please Choose"
    #this is 1
    keyboard = [
        [InlineKeyboardButton("1.1", callback_data=str(ONE))],
        [InlineKeyboardButton("END", callback_data=str(END))]
        ]

    await update.message.reply_text(text= text, reply_markup=InlineKeyboardMarkup(keyboard))

    return START

async def stage_one(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    # this is 1.1
    text = "BASE 1.1"

    keyboard = [
        [InlineKeyboardButton("1.1.1 ", callback_data=str(TWO))],
        [InlineKeyboardButton("1.1.2", callback_data=str(THREE))],
        # [InlineKeyboardButton("END", callback_data=str(END))]
        ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(text= text, reply_markup=reply_markup)

    return START

async def stage_one_one(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    # this is 1.1
    text = "BASE 1.1.1"

    keyboard = [
        [InlineKeyboardButton("OPTION TEMP FOR 1.1.1 ", callback_data=str(TWO))],
        [InlineKeyboardButton("END", callback_data=str(END))]
        ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(text= text, reply_markup=reply_markup)

    return START

async def stage_one_two(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    # this is 1.1
    text = "BASE 1.1.2"

    keyboard = [
        [InlineKeyboardButton("START BUT THIS IS 1.1.2 ", callback_data=str(ONE))],
        [InlineKeyboardButton("END", callback_data=str(END))]
        ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(text= text, reply_markup=reply_markup)

    return END

async def end(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(text="See you next time!")
    return ConversationHandler.END

def main():
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start_bot))

    conversation_handler = ConversationHandler(
        entry_points=[MessageHandler(filters.TEXT, start_conversation)],
        states={
            START : [
                CallbackQueryHandler(stage_one, pattern="^"+str(ONE)+"$"),
                CallbackQueryHandler(stage_one_one, pattern="^"+str(TWO)+"$"),
                CallbackQueryHandler(stage_one_two, pattern="^"+str(THREE)+"$")
            ],
            END : [CallbackQueryHandler(end, pattern="^"+str(END)+"$")]
        },
        fallbacks=[CommandHandler("start", start_bot)]
    )
    application.add_handler(conversation_handler)
    application.run_polling()
main()