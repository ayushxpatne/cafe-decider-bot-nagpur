from globals import *

def correction_type_of_place_discrepancy(query):
     #* CALLBACK DATA DESCRIPANCY HANDELING FOR "Khau Gallis", "Roadside", "Main Course"
    if str(query) == 'KhauGallis':
        ATTRIBUTES.append('Multiple Eateries Together / Khau Galli')
    elif str(query) == 'MainCourse':
        ATTRIBUTES.append('Main Course')
    else:
        ATTRIBUTES.append(query)

def correction_600_1000_discrepancy(query):
    #* CALLBACK DATA DESCRIPANCY HANDELING FOR 600-100
    if str(query) == '600-1000':
        ATTRIBUTES.append('600-1000+')
    else:
        ATTRIBUTES.append(query)

