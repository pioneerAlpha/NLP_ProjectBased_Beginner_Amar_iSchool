import json, os

def get_data(directory):
    data = []

    #iterating through the directory in search for json files
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith("json"):

            #reading the data from each json and appending inside data list
            data.append(json_parser(os.path.join(directory, filename)))
    
    return data

def json_parser(filename):
    # Opening JSON file
    f = open(filename)
    
    # returns JSON object as a dictionary
    data = json.load(f)

    # Closing file
    f.close()
    
    #reading the values from the keys in json file
    classes = data['classes']
    annotations = data['annotations'][0]

    text = annotations[0]

    entities = annotations[-1]['entities']

    #creating tuples according to the desired format
    entities = [tuple(item) for item in entities]

    return (text, entities)


'''
to run this code.
keep this file in your notebook directory
import this file in your notebook by from json_parser import *

then in your notebook do:
train_data = get_data(<directory name where the json file is>)

for example if all the json files are stored in ./data folder just run:
train_data = get_data('./data)   
'''