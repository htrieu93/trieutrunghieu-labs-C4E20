from pymongo import MongoClient

mongo_uri = 'mongodb://admin:admin@ds021182.mlab.com:21182/c4e'

client = MongoClient(mongo_uri)

db = client.get_default_database()

posts = db['posts']

content = "Yesterday is history, tomorrow is a mystery, today is a gift of God, which is why we call it the present."

new_post = {
    'title' : 'A little note',
    'author' : 'Hieu',
    'content' : content
}

posts.insert_one(new_post)
