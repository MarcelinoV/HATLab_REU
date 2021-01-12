# imported libraries
import requests
import json
import csv
import pandas as pd
import numpy as np
from itertools import cycle

# Demo code ---------------------------------
'''
api_id = 'XXXXXX'
api_key = 'XXXXXXXXXXXXXXXXXXXXXX'
'''
# --------------------------------------------

# Nutrient API URL
url = 'https://trackapi.nutritionix.com/v2/natural/nutrients'

# dataset where we are getting text data from
data = pd.read_csv(input('Enter file name: ') + '.csv')

# API ids and keys to be called
ids_keys = {'XXXXXX': 'XXXXXXXXXXXXXXXXXXXXXX',
            'XXXXXX': 'XXXXXXXXXXXXXXXXXXXXXX',
            'XXXXXX': 'XXXXXXXXXXXXXXXXXXXXXX',
            'XXXXXX': 'XXXXXXXXXXXXXXXXXXXXXX',
            'XXXXXX': 'XXXXXXXXXXXXXXXXXXXXXX',
            'XXXXXX': 'XXXXXXXXXXXXXXXXXXXXXX',
            'XXXXXX': 'XXXXXXXXXXXXXXXXXXXXXX'}

# Manual Food Bank in a set to check if words are food.
food = {'waffle', 'apple', 'cheese', 'muffin', 'soup', 'coffee', 'butter', 'ham', 'syrup', 'tortilla',
        'salt', 'pepper', 'butternut', 'walnut', 'cinnamon', 'kale', 'spinach', 'banana', 'bean', 'turkey', 'jam',
        'carrot', 'cracker', 'rice', 'soy', 'tempura', 'sushi', 'orange', 'pasta', 'chicken', 'beef', 'fish', 'lamb',
        'pork', 'broccoli', 'lettuce', 'tomato', 'garlic', 'bacon', 'salad', 'vanilla', 'raspberry', 'cake', 'beer',
        'onion', 'vegetable', 'chocolate', 'sugar', 'chip', 'cookie', 'milk', 'cashew', 'vinegar', 'artichoke',
        'cheddar', 'cauliflower', 'pinto', 'egg', 'peanut', 'cocoa', 'avocado', 'pomegranate', 'clementine', 'grape',
        'sausage', 'coconut', 'chorizo', 'taco', 'strawberry', 'spinach', 'blueberry', 'goulash', 'fig', 'potato'}

# Demo Code---------------
'''
headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'x-app-id': api_id,
            'x-app-key': api_key,
            'x-remote-user-id': '0'
}
'''
# Demo Code: test query
'''
query = {'query': 'apple'}
'''
# ----------------------------------------

print('Variables declared... ')
print('Beginning Process...')

# List that will become new column in dataset or by itself
col = []

for post, api_id, api_key in zip(
        data['post'], cycle(list(ids_keys.keys())), cycle(list(ids_keys.values()))
                                ): # cycles through text data & api keys

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'x-app-id': api_id,
        'x-app-key': api_key,
        'x-remote-user-id': '0'
    }

    calories = [] # every post in the data will have its own list for calorie storage

    print('Current data:', len(data['post']), '\n New column: ', len(col)) # prints length of post vs new cal column

    for word in np.unique(eval(post)):
        if word not in food:
            continue
        else:
            print('Detected Word: ', word)
            query = {'query': '{}'.format(word)}
            try:
                response = requests.request("POST", url, headers=headers, data=query)
            except KeyError as ke:
                print(ke, 'Out of calls, dropping spent key...')
                ids_keys.pop(api_id, None) # drop current api id & key from dict if out of calls
                print('API keys left:', len(ids_keys))
            finally:
                stats = response.json()
                print('Food Stats: \n', stats)
                try:
                    print('Calories in food: ', stats['foods'][0]['nf_calories'])
                except KeyError as ke:
                    print(ke, 'Out of calls, next key...')
                    ids_keys.pop(api_id, None)  # drop current api id & key from dict if out of calls
                    print('API keys left:', len(ids_keys))

                    # Demo Code --------------------
                    '''
                    print(stats['message'])
                    print('Take word out of set:', word)
                    exit()
                    '''
                    # ------------------------------------
                else:
                    calories.append(stats['foods'][0]['nf_calories'])
                    print('Current Key', api_id, ':', api_key)
    col.append(calories)

print(col[0:5])
print('Current data:', len(data), '\n New column: ', len(col))

prompt = input('Proceed? ')

if prompt == 'no'.casefold():
    exit()
else:
    # If new column is longer than data set, save independently
    try:
        data['Calories'] = col
    except ValueError:
        prompt2 = input('Column cannot be appended to data. Save independently? ')
        if prompt2 != 'no'.casefold():
            new_col = pd.Series(list(np.array(col, dtype='object')))
            print(new_col[0:7])
            prompt
            if prompt != 'no'.casefold():
                print('Saving to csv...')
                new_col.to_csv(input(r'Enter new column file name:') + '.csv', index=False, header=['Calories'], encoding='utf-8')

            # Demo code --------------------------------------
            '''
            with open('independent col.csv', 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file, quoting=csv.QUOTE_MINIMAL)
                writer.writerow(['calories'])
                for row in col:
                    writer.writerow(row)
            '''
            # ----------------------------------------------------
        else:
            exit()
    else:
        print(data.head())
        if prompt == 'no'.casefold():
            exit()
        else:
            # Saving to csv
            print('Saving to csv...')
            data.to_csv(input('Enter new dataset name: ') + '.csv', index=False, header=True, encoding='utf-8')

print('done')
