from essential_imports import *

#* DEPLOYING THE FINAL LIST
async def deploy_results(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    
    generating_list_recieved_query_query = generating_list_recieved_query[0]
    generating_list_recieved_query_budget_or_place = generating_list_recieved_query[1]
    # if generating_list_recieved_query == 'stop':
    #     text="Process was aborted."
    # else:
    text_from_json = final_list_to_string(returningJSONData())
    # QUERY RECIEVED BY generating_list()/generating_list_filters() IS "3" HENCE WE CANT USE QUERY.DATA
    # SINCE THE FINAL TEXT DEPENDS ON WHICH QUERY IS RECIEVED BY generating_list() OR generating_list_filters()
    # WE NEED TO KEEP TRACK OF THE QUERY RECIEVED BY EITHER FUNCTION.
    
    if generating_list_recieved_query_query in ['Beverages','Roadside','MainCourse','Cafe','Clubs','Pubs','Lounge', 'KhauGallis', "South Indian Exclusives"]:
        if generating_list_recieved_query_budget_or_place == 'budget':
            text=f"""
            So just to confirm: 
            \nYour Budget is {ATTRIBUTES[0]} per person & Selected Type is {ATTRIBUTES[1]}.
            \nHere is the list\n{text_from_json}"""
        elif generating_list_recieved_query_budget_or_place == 'place':
            text=f"So you are looking for {generating_list_recieved_query_query}\nHere is the list\n{text_from_json}"
    
    elif generating_list_recieved_query_query in ['None','Pure Veg','Serves Alcohol']:
        text=f"""
        Okay, You are looking for {ATTRIBUTES[0]}. 
        \nHere is the list\n{text_from_json}"""
    elif generating_list_recieved_query_query == 'stop':
        text="Process Aborted"
    
  
    await query.edit_message_text(text=text)

    generating_list_recieved_query.clear()
    ATTRIBUTES.clear()

    # os.remove('decider/json_temp.json')
    logger.info(msg=f"")
    
    logger.info(msg=f"deploy_results() is running")
    logger.info(msg=f"generating_list_recieved_query: {generating_list_recieved_query}")
    logger.info(msg=f"Query recieved: {query.data}") 
    logger.info(msg=f"ATTRIBUTES: {ATTRIBUTES}")
    query_id = get_query_id(query)
    logger.info(msg=f"QUERY ID : {query_id}")
    
    return ConversationHandler.END

def final_list_to_string(returning_list):
    string = ""
    
    for index in range(len(returning_list)):

        string = f"{string}"+f"\n{returning_list[index]['name']}\nLocated at {returning_list[index]['address']}\n"

    return string