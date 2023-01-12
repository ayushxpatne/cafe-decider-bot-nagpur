from essential_imports import *

#* GENERATE THE FINAL LIST : BUDGET OPTION >> PLACE >> GENERATE THIS
# QUERIES RECIEVING : Beverages|Clubs|Pubs|Lounge|Roadside|MainCourse|KhauGallis|Cafe|South Indian Exclusives
async def generate_list(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()

    generating_list_recieved_query.append(query.data)
    generating_list_recieved_query.append('budget')

    correction_type_of_place_discrepancy(query.data)
    

    generatingJSON_for_budget()
    
    inlineButtons = [[InlineKeyboardButton('Generate', callback_data=str(END)),]]
    reply_markup = InlineKeyboardMarkup(inlineButtons)
    
    await query.edit_message_text(text="Click Generate:", reply_markup= reply_markup)

    query_id = get_query_id(query)

    logger.info(msg=f"") #queries from budget function is stored here
    logger.info(msg=f"generate_list() is running")
    logger.info(msg=f"Query recieved: {query.data}") #queries from budget function is stored here
    logger.info(msg=f"ATTRIBUTES: {ATTRIBUTES}")
    logger.info(msg=f"QUERY ID : {query_id}")
    logger.info(msg=f"update.message.id : {query_id}, dictionary: {query_id_dict, ATTRIBUTES} ")
    return END

#* GENERATE THE FINAL LIST FOR FILTERS : PLACE >> FILTERS >> GENERATE THIS
#QUERIES RECIEVING : None|Pure Veg|Serves Alcohol|KhauGallis|South Indian Exclusives
async def generate_list_filters(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()

    generating_list_recieved_query.append(query.data)
    generating_list_recieved_query.append('place')

    correction_type_of_place_discrepancy(query.data)

    
    if query.data == 'Pure Veg' or query.data == 'Serves Alcohol':
        generatingJSON_for_filters()
    elif query.data in ['KhauGallis','South Indian Exclusives','Clubs','Pubs','Lounge','Beverages','None']:
        generatingJSON_for_filters_None()

        
    inlineButtons = [[InlineKeyboardButton('Generate', callback_data=str(END)),]]
    reply_markup = InlineKeyboardMarkup(inlineButtons)

    await query.edit_message_text(text= "Click Generate:", reply_markup= reply_markup)
    query_id = get_query_id(query)
    
    logger.info(msg=f"") #queries from budget function is stored here
    logger.info(msg=f"generate_list_filters() is running")
    logger.info(msg=f"Query recieved: {query.data}") #queries from budget function is stored here
    logger.info(msg=f"ATTRIBUTES: {ATTRIBUTES}")
    logger.info(msg=f"QUERY ID : {query_id}")
    logger.info(msg=f"update.message.id : {query_id}, dictionary: {query_id_dict, ATTRIBUTES} ")
    return END
