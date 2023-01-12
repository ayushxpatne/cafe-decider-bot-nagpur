import json
import pandas as pd
from globals import ATTRIBUTES

database_path = 'cafe_decider_nagpur/database/db.csv'
generated_json_path = 'cafe_decider_nagpur/json_temp.json'

def sorter_to_json_budget(budget, category,):
    df = pd.read_csv(database_path)

    df['Average Price Per Person'] = df['Average Price Per Person'].astype(str)
    df = df.drop(columns = ['Timestamp'])

    df['Categories'] = df['Categories'].str.split(', ')
    df2 = df.explode('Categories', ignore_index= False)

    df_budget =df2.loc[(df2['Average Price Per Person']==budget) & (df2['Categories']==category)]
    
    df_budget.to_json(generated_json_path, index=False, orient="table")

def sorter_to_json_filter(category, filter):
    df = pd.read_csv(database_path)

    df['Average Price Per Person'] = df['Average Price Per Person'].astype(str)
    df = df.drop(columns = ['Timestamp'])

    df['Categories'] = df['Categories'].str.split(', ')
    df2 = df.explode('Categories', ignore_index= False)

    df_budget =df2.loc[(df2['Categories']==category) & (df2['Filters']==filter)]
    
    df_budget.to_json(generated_json_path, index=False, orient="table")

def sorter_to_json_for_filter_None(category):
    df = pd.read_csv(database_path)

    df['Average Price Per Person'] = df['Average Price Per Person'].astype(str)
    df = df.drop(columns = ['Timestamp'])

    df['Categories'] = df['Categories'].str.split(', ')
    df2 = df.explode('Categories', ignore_index= False)

    df_budget =df2.loc[(df2['Categories']==category)]
    
    df_budget.to_json(generated_json_path, index=False, orient="table")

def returningJSONData():
    json_file_path = generated_json_path
    with open(json_file_path, 'r') as j:
        json_file = json.loads(j.read())

    length = len(json_file['data'])
    final_list = []
    

    if len(json_file['data']) == 0:
        temp_dict = {}
        temp_dict['name']="Sorry! No such place is available"
        temp_dict['address']='I will try and find such place soon.'
        final_list.append(temp_dict)
    else:
        for index in range(0,length):
            temp_dict = {}
            temp_dict['name'] = json_file['data'][index]['Name']
            temp_dict['address'] = json_file['data'][index]['Address']
            # tag_list = json_file['data'][index]['Additional Tags']
            final_list.append(temp_dict)
            

    return final_list

def generatingJSON_for_budget():
    sorter_to_json_budget(ATTRIBUTES[0], ATTRIBUTES[1])
    return 0

def generatingJSON_for_filters():
    sorter_to_json_filter(ATTRIBUTES[0], ATTRIBUTES[1],)
    return 0

def generatingJSON_for_filters_None():
    sorter_to_json_for_filter_None(ATTRIBUTES[0],)
    return 0


def write_json(data, file_name = 'response.json'):
    with open(file_name, 'w') as f:
        json.dump(data,f, indent=4, ensure_ascii= False)
        