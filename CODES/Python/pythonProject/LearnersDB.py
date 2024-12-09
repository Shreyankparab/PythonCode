import pymongo
from pymongo import *

client=pymongo.MongoClient('mongodb://localhost:27017')

db=client.LearnersDatabse
collection=db.learners_data

post=[{"_id":1,"name":"shreyank","course":"MCA","mob_no":9876543210},
        {"_id":2,"name":"asda","course":"MBA","mob_no":9876543210},
        {"_id":3,"name":"sasfds","course":"MCA","mob_no":9876543210},
        {"_id":4,"name":"sdfs","course":"MBA","mob_no":9876543210},
        {"_id":5,"name":"dfgd","course":"MCA","mob_no":9876543210},
        {"_id":6,"name":"asda","course":"MBA","mob_no":9876543210},
        {"_id":7,"name":"sdfsdf","course":"MBA","mob_no":9876543210},
        {"_id":8,"name":"dgdfg","course":"MCA","mob_no":9876543210},
      ]

# posts=collection.insert_many(post)
# querry=
collection.update_one({"_id":2},{"$set":{"course":"MPA"}})

collection.delete_one({"_id":1})

for i in collection.find():
    print(i)