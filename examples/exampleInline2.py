from telegram.ext import *
from telegram import *
import logging

from warnings import filterwarnings
from telegram.warnings import PTBUserWarning

filterwarnings(action="ignore", message=r".*CallbackQueryHandler", category=PTBUserWarning)
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


TOKEN = "5835529587:AAEnoYniWd8LjGJFsP47xq5_QnI9OIoSe3c"

START, END = 0,1

async def start_bot(update: Update, context= ContextTypes.DEFAULT_TYPE) -> None:
   await context.bot.send_message(chat_id=update.effective_chat.id, text="Hey, itz-a-me examples")

async def start_bot2(update: Update, context= ContextTypes.DEFAULT_TYPE) -> None:
   pass
 


async def start_conversation(update: Update, context= ContextTypes.DEFAULT_TYPE) -> int:
    text = "Please Choose"
    logger.info("User started the conversation.")
    #this is 1
    keyboard = [
        [InlineKeyboardButton("1.1", callback_data=str(1)),
         InlineKeyboardButton("1.2", callback_data=str(2))
         ],
        [ InlineKeyboardButton("END", callback_data=str("END"))]
        ]

    await update.message.reply_text(text= text, reply_markup=InlineKeyboardMarkup(keyboard))
    return START
    
    

async def answer(update: Update, context= ContextTypes.DEFAULT_TYPE) -> int:
    logger.info("answer")
    query = update.callback_query
    await query.answer()
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f"Query: {query.data}")
    await query.edit_message_text(text=f"You selected{query.data}")
    return ConversationHandler.END
    

async def end(update: Update, context= ContextTypes.DEFAULT_TYPE) -> int:
    logger.info("ended")
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(text=f"You selected{query.data}")

    return ConversationHandler.END


def main():
    application = Application.builder().token(TOKEN).build()
    conversation_handler = ConversationHandler(
        entry_points=[MessageHandler(filters.TEXT, start_conversation)],
        states={
            START : [
                CallbackQueryHandler(answer)
            ],
            END : [
                CallbackQueryHandler(end, pattern="^(END)$")
            ]
        },
        fallbacks=[CommandHandler("start", start_bot2)]
    )
    # application.add_handlers([MessageHandler(filters.TEXT, start_conversation),CallbackQueryHandler(answer), CallbackQueryHandler(end, pattern="^END$")])
    application.add_handler(conversation_handler)
    application.run_polling()
main()