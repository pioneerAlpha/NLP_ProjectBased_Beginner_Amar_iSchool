from urlextract import URLExtract
import pandas as pd

extract = URLExtract()

def fetch_stats(selected_user, df):
    if selected_user == 'Overall':
        # fetch number of total messages
        num_messages = df.shape[0]
        # fetch number of total words written
        words =[]
        for message in df['messages']:
            words.extend(message.split())        
        # fetch number of media messages
        num_media_messages = df[df['messages'] == '<Media omitted>\n'].shape[0]

        # fetch number of links shared
        links = []
        for message in df['messages']:
            links.extend(extract.find_urls(message))
        return num_messages, len(words), num_media_messages, len(links)
    else:
        new_df = df[df['users']== selected_user]
        # fetch number of total messages
        num_messages = new_df.shape[0]
        # fetch number of total words written
        words =[]
        for message in new_df['messages']:
            words.extend(message.split())
        # # fetch number of media messages
        num_media_messages = new_df[new_df['messages'] == '<Media omitted>\n'].shape[0]

        # # fetch number of links shared
        links = []
        for message in new_df['messages']:
            links.extend(extract.find_urls(message))

        return num_messages, len(words), num_media_messages, len(links)

def most_busy_users(df):
    x = df['users'].value_counts().head()
    df = round((df['users'].value_counts() / df.shape[0]) * 100, 2).reset_index().rename(columns={'index': 'name', 'users': 'percent'})
    return x, df
