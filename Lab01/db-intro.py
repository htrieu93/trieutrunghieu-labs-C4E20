from pymongo import MongoClient

mongo_uri = 'mongodb://ht:prototype101@ds113122.mlab.com:13122/fun_zone'

#1. Connect to database
client = MongoClient(mongo_uri)

#2. Get database
db = client.get_default_database()

#3. Create a collection
games = db['games']

# #4. Create a document
# new_game = {
#     'title': 'Hứng bia',
#     'description': 'Best game ever'
# }

# #5. Insert doc into collection
# games.insert_one(new_game)

# 6. Read all documents
all_game = games.find()
first_game = all_game[0]
print(first_game['description'])