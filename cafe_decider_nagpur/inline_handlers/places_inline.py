from essential_imports import *

# * BUDGET >> TYPE OF PLACE
async def display_types(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:

    query = update.callback_query
    await query.answer()

    inlineButtons = filtering_inline_button_wrt_budget(query.data)
    text = type_of_place_callback_data_handeling(query.data)

    correction_600_1000_discrepancy(query.data)

    reply_markup = InlineKeyboardMarkup(inlineButtons)

    await query.edit_message_text(text=text, reply_markup=reply_markup)

    logger.info(msg=f"")  # queries from budget function is stored here
    logger.info(msg=f"display_type() is running")
    # queries from budget function is stored here
    logger.info(msg=f"Query recieved: {query.data}")
    logger.info(msg=f"ATTRIBUTES: {ATTRIBUTES}")
    query_id = get_query_id(query)
    logger.info(msg=f"QUERY ID : {query_id}")
    logger.info(msg=f"update.message.id : {query_id}, dictionary: {query_id_dict, ATTRIBUTES} ")
    return BUDGET

# * IF TYPE OF PLACE IS CHOSEN IN FIRST PLACE
async def display_types_for_types(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:

    query = update.callback_query
    await query.answer()

    inlineButtons = filtering_inline_button_wrt_budget(query.data)
    text = type_of_place_callback_data_handeling(query.data)

    reply_markup = InlineKeyboardMarkup(inlineButtons)

    await query.edit_message_text(text=text, reply_markup=reply_markup)

    logger.info(msg=f"")  # queries from budget function is stored here
    logger.info(msg=f"display_types_for_types() is running")
    # queries from budget function is stored here
    logger.info(msg=f"Query recieved: {query.data}")
    logger.info(msg=f"ATTRIBUTES: {ATTRIBUTES}")
    query_id = get_query_id(query)
    logger.info(msg=f"QUERY ID : {query_id}")
    logger.info(msg=f"update.message.id : {query_id}, dictionary: {query_id_dict, ATTRIBUTES} ")
    return TYPE

# * FILTERING INLINE BUTTON FOR 600-100
def filtering_inline_button_wrt_budget(query):

    if str(query) == '600-1000':
        inlineButtons = [
            [
                InlineKeyboardButton("CLUBS".title(), callback_data="Clubs"),
                InlineKeyboardButton("PUBS".title(), callback_data="Pubs"),
            ],
            [
                InlineKeyboardButton("LOUNGE".title(), callback_data="Lounge"),
                InlineKeyboardButton("MAIN COURSE".title(), callback_data="MainCourse"),
            ],
            [
                InlineKeyboardButton("CAFES".title(), callback_data="Cafe"),
            ],
        ]
    elif str(query) == '100-150' or str(query)== '150-300':
        inlineButtons = [
            [
                InlineKeyboardButton("ROADSIDE".title(), callback_data="Roadside"),
                InlineKeyboardButton("SOUTH INDIAN ".title(), callback_data="South Indian Exclusives"),
            ],
            [
                InlineKeyboardButton("MAIN COURSE".title(),
                                     callback_data="MainCourse"),
                InlineKeyboardButton( "\"KHAU GALLIS\"".title(), callback_data="KhauGallis"),
            ],
            [
                InlineKeyboardButton("CAFES".title(), callback_data="Cafe"),
                InlineKeyboardButton("BEVERAGE EXCLUSIVES".title(), callback_data="Beverages"),
            ],
        ]
    else:
        inlineButtons = [
            [
                InlineKeyboardButton("CLUBS".title(), callback_data="Clubs"),
                InlineKeyboardButton("PUBS".title(), callback_data="Pubs"),
            ],
            [
                InlineKeyboardButton("LOUNGE".title(), callback_data="Lounge"),
                InlineKeyboardButton("ROADSIDE".title(), callback_data="Roadside"),
            ],
            [
                InlineKeyboardButton("MAIN COURSE".title(), callback_data="MainCourse"),
                InlineKeyboardButton(
                    "\"KHAU GALLIS\"".title(), callback_data="KhauGallis"),
            ],
            [
                InlineKeyboardButton("CAFES".title(), callback_data="Cafe"),
                InlineKeyboardButton(
                    "BEVERAGE EXCLUSIVES".title(), callback_data="Beverages"),
            ],
            [InlineKeyboardButton("SOUTH INDIAN".title(), callback_data="South Indian Exclusives"),
             ]
        ]

    return inlineButtons

# * CALLBACK DATA HANDELING FOR "Place"
def type_of_place_callback_data_handeling(query):

    if str(query) == 'place':
        text = "What are you looking for?"

    else:
        text = f"Okay. \nSo your Budget is {query}. \n\nWhat are you looking for? "

    return text
