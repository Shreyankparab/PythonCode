import pymongo
client=pymongo.MongoClient('mongodb://localhost:27017')
db=client.Student
studcollection=db.Student_info
details=[{"name":"Rahul Deshpande","roll_no":24201,"class":"MCA","Marks":99},
            {"name":"Swayam Shinde","roll_no":24202,"class":"MCA","Marks":95},
            {"name":"Shyam Dheol","roll_no":24203,"class":"MCA","Marks":89},
            {"name":"Sahil P","roll_no":24204,"class":"MCA","Marks":91},
            {"name":"Prathamesh S","roll_no":24205,"class":"MCA","Marks":90},
            {"name":"Raj P","roll_no":24206,"class":"MCA","Marks":96},
            {"name":"Aditya G","roll_no":24207,"class":"MCA","Marks":97},
         ]
# ========================Insert=======================================
#Insert New Students details

# x=studcollection.insert_many(details)
# ===============================================================

# ==========================ReadAll=====================================

#to fetch all students record from database
#
# for data in studcollection.find():
#     print(data)
# ===============================================================


# ==========================Read GT 90=====================================

#To print the data of marks greater than 90 and limit them for only printing first 2 data

# for data in studcollection.find({"Marks": {"$gt": 90}}).limit(2):
#     print(data)
# ===============================================================


# =============================Update==================================

#Update Students Marks with specified roll no
# studcollection.update_one({"roll_no":24206},{"$set":{"Marks":99}})
#
# for data in studcollection.find({"Marks": {"$gt": 90}}):
#     print(data)
# ===============================================================



# ==========================Sorting in descending Order==========

# for data in studcollection.find({"Marks": {"$gt": 90}}).sort("Marks", -1):
#     print(data)

# ===============================================================


# =========================Delete class MBA Students======================================

# studcollection.delete_many({"class":"MBA"})
# for data in studcollection.find():
#     print(data)
# ===============================================================


# ==========================Fetch top 3 students=====================================
for data in studcollection.find({"Marks": {"$gt": 90}}).sort("Marks", -1).limit(3):
    print(data)
# ===================================================================================


