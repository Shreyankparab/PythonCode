import pymongo

client=pymongo.MongoClient('mongodb://localhost:27017')
db=client.faculty_database
collection=db.faculty_data

post=[{"_id":1,"name":"Prashant","Designation":"Assistant Professor","PhoneNo":6798678767,"Dept":"MCA"},
{"_id":2,"name":"Prashant","Designation":"Assistant Professor","PhoneNo":2354456345,"Dept":"MCA"},
{"_id":3,"name":"Kiran","Designation":"Assistant Professor","PhoneNo":24545634522,"Dept":"MCA"},
{"_id":4,"name":"Samiksha","Designation":"Assistant Professor","PhoneNo":45623543545,"Dept":"MCA"},
{"_id":5,"name":"Ashwini","Designation":"HOD","PhoneNo":34523235345,"Dept":"MCA"},
{"_id":6,"name":"Priyanka Singh ","Designation":"Director","PhoneNo":23435645332,"Dept":"MBA/MCA"},
{"_id":7,"name":"Suresh Mali","Designation":"Principle","PhoneNo":647342452434,"Dept":"DYPMID"},
{"_id":8,"name":"Rahul","Designation":"Assistant Professor","PhoneNo":8567345345,"Dept":"MBA"},
{"_id":9,"name":"Akash","Designation":"Professor","PhoneNo":84634523332,"Dept":"MBA"}
]
# posts=collection.insert_many(post)

# print("Data inserted Successfully")

#Update Done
# collection.update_one({"_id": 1}, {"$set": {"Dept": "MBA"}})

# query = {"Dept": "MCA", "Designation": "Assistant Professor"}
#
# results = collection.find(query)
#
# for data in results:
#     print(data)

collection.delete_one({"_id":9})
# {"_id": {"$gt": 5}}
for data in collection.find():
    print(data)

