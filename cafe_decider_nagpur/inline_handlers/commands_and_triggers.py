from essential_imports import *

#* THE /START COMMAND
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = """ 
Greetings!
Welcome To DECIDER BOT. 
    
This message will include the basic walkthrough of this bot.
    """
    await update.message.reply_text(text=text)

async def troubleshoot_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    text = """ 
Hopefully the error corrected. Please send "Hey" or "Hi" to start again.
    """
    await update.message.reply_text(text=text)
    return ConversationHandler.END

async def end_conversation(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    # os.remove('decider/json_temp.json')
    logger.info(msg="end_conversation() is started")

    generating_list_recieved_query.append('stop')
    generating_list_recieved_query.append('stop')
    
    inlineButtons = [[InlineKeyboardButton('STOP', callback_data=str(END))]]
    reply_markup = InlineKeyboardMarkup(inlineButtons)

    if len(ATTRIBUTES) == 0:
        message_id = query_id_dict['start']
    else:
        message_id = query_id_dict['next']
    
    await bot.edit_message_text(
        text= "Click Below:",
        chat_id= update.effective_chat.id,
        message_id=message_id, 
        reply_markup= reply_markup
    )
    logger.info(msg=f"update.message.id : {message_id}, dictionary: {query_id_dict, ATTRIBUTES} ")
    return END


#* CONVERSATION STARTER
async def start_conversation(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:

    text =  """Which Option is most applicable to you?"""

    inlineButtons = [
       [InlineKeyboardButton("I KNOW THE BUDGET".title(), callback_data="budget"),] ,
       [InlineKeyboardButton("I KNOW THE TYPE OF PLACE".title(), callback_data="place")],
    ]
    reply_markup = InlineKeyboardMarkup(inlineButtons)
    

    await update.message.reply_text(text=text, reply_markup= reply_markup )
    
    query_id = update.message.message_id
    query_id_dict['start'] = query_id

    logger.info(msg="start_conversation() is started")
    logger.info(msg=f"update.message.id : {query_id}, dictionary: {query_id_dict, ATTRIBUTES} ")
    return START
