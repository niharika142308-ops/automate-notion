'''
Automate Notion using Python
Author: Niharika
'''
#Put your credentials in config.py
import config
#import the necessary module!
from notion.client import NotionClient


#fetch the token_v2
token = config.token

client =  NotionClient(token_v2=token)

#fetch the tracker URL
list_url = config.list_url
collection_view = client.get_collection_view(list_url)

#add new role
new_row = collection_view.collection.add_row()

#populate the data
new_row.running = True
new_row.Journaling = True

new_row.screen_time_minutes = 30

print('New Row has been successfully created!')