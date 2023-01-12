import telegram
from token import TOKEN

START, BUDGET, TYPE, END = range(4)

ATTRIBUTES = []

bot = telegram.Bot(TOKEN)
generating_list_recieved_query = []
query_id_dict = {
    'start': 0,
    'next' : 0,
}

def get_query_id(query):
    query_id = query.message.message_id

    if len(ATTRIBUTES) == 0:
        query_id_dict['start'] = query_id
    else:
        query_id_dict['next'] = query_id
    
    return query_id