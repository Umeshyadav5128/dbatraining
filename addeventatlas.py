# from pymongo import MongoClient
# client =  MongoClient("mongodb+srv://umeshyadav:Butki@93@cluster0.xf21whn.mongodb.net/?appName=Cluster0")

# eventdv = client["eventdv"]

# addevent = eventdv["addevent"]

# addevent.insert_one({
#     "eventname": "tedx",
#     "venue": "auditorium",
#     "date": "2026-02-06"
# })


# addevent.insert_many([{
#     "eventname": "tedx",
#     "venue": "auditorium",
#     "date": "2026-02-06"
# },
# {
#     "eventname": "tech conference",
#     "venue": "main hall",
#     "date": "2026-03-15"
# },
# {
#     "eventname": "art exhibition",
#     "venue": "gallery",
#     "date": "2026-04-20"
#     }])


# to delete the single document

# addevent.delete_one({"eventname": "tedx"}) 

# update the single event

# addevent.update_one({"eventname": "tech conference"}, {"$set": {"venue": "conference room"}})
for event in addevent.find():
    print(event)
