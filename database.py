from pymongo import MongoClient

db_url = "mongodb+srv://Rohit:6zJeQrfOPSTNQZvX@cluster0.nlgby.mongodb.net/MyFirstDatabase?retryWrites=true&w=majority"
client = MongoClient(db_url)
db = client.test
movie_list = db['movie_list']
user_list = db['users_list']



