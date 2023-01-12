from essential_imports import *

#* BUDGET OPTION IS SELECTED
async def budget(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    
    text =  "Alright!\nSo what is your budget per person?"

    inlineButtons = [
       [InlineKeyboardButton("100-150", callback_data="100-150"),],
       [InlineKeyboardButton("150-300", callback_data="150-300"),],
       [InlineKeyboardButton("300-600", callback_data="300-600"),],
       [InlineKeyboardButton("600-1000+", callback_data="600-1000"),],
    ]
    reply_markup = InlineKeyboardMarkup(inlineButtons)
    
    await query.edit_message_text(text=text, reply_markup= reply_markup )
    
    query_id = get_query_id(query)

    logger.info(msg=f"") #queries from budget function is stored here
    logger.info(msg=f"budget() is running")
    logger.info(msg=f"Query recieved: {query.data}") #queries from budget function is stored here
    logger.info(msg=f"ATTRIBUTES: {ATTRIBUTES}")
    logger.info(msg=f"QUERY ID : {query_id}")
    logger.info(msg=f"update.message.id : {query_id}, dictionary: {query_id_dict, ATTRIBUTES} ")
    
    return BUDGET
