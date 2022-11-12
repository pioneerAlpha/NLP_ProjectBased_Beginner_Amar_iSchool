import re
import pandas as pd

def preprocess(data):
    pattern = '\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{2}\s(?:pm|am)\s-\s'
    messages = re.split(pattern,data)[1:]
    dates= re.findall(pattern, data)
    df = pd.DataFrame({'user_message':messages, 'message_date': dates})

    #convert message_date type
    df['message_date'] = pd.to_datetime(df['message_date'], format ='%d/%m/%Y, %I:%M %p - ')

    df.rename(columns={'message_date': 'date'}, inplace=True)

    users =[]
    messages = []
    for message in df['user_message']:
        entry=re.split('([\w\W]+?):\s', message)
        if entry[1:]:
            users.append(entry[1])
            messages.append(entry[2])
        else:
            users.append('group_notification')
            messages.append(entry[0])
    df['users'] = users
    df['messages'] = messages
    df.drop(columns=['user_message'], inplace=True)

    df['month'] = df['date'].dt.month_name()
    df['day'] = df['date'].dt.day
    df['hour'] = df['date'].dt.hour
    df['minute'] = df['date'].dt.minute

    df['messages'] = df['messages'].replace('\n','', regex=True)
    df['messages'] = df['messages'].replace('\t','', regex=True)

    df.drop('date', inplace=True, axis=1)

    return df