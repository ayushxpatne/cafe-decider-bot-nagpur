from essential_imports import *

#* TYPE OF PLACE >> FILTERS
async def display_more_filters(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    
    correction_type_of_place_discrepancy(query=query.data)

    text =  f"Great! Does Any Of These Options Apply?"
    
    inlineButtons = [
       [InlineKeyboardButton("Pure Veg", callback_data="Pure Veg"),],
       [InlineKeyboardButton("Serves Alcohol", callback_data="Serves Alcohol"),],
       [InlineKeyboardButton("None", callback_data="None"),],
    ]

    reply_markup = InlineKeyboardMarkup(inlineButtons)
    
    await query.edit_message_text(text=text, reply_markup= reply_markup )
    logger.info(msg=f"") #queries from budget function is stored here
    logger.info(msg=f"display_more_filters() is running")
    logger.info(msg=f"Query recieved: {query.data}") #queries from budget function is stored here
    logger.info(msg=f"ATTRIBUTES: {ATTRIBUTES}")
    query_id = get_query_id(query)
    logger.info(msg=f"QUERY ID : {query_id}")
    logger.info(msg=f"update.message.id : {query_id}, dictionary: {query_id_dict, ATTRIBUTES} ")
    return TYPE