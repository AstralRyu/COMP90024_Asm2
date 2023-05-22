import couchdb
import json
import re
import time

admin = 'admin_yuki'
password = 'pwd12345'
url = f'http://{admin}:{password}@172.26.133.179:5984/'
couch_db = couchdb.Server(url)
db_name = 'over_night_data'

if db_name not in couch_db:
    database = couch_db.create(db_name)
else:
    database = couch_db[db_name]


with open("overnight.json", 'r') as f:
    objects = json.load(f)
    # print(objects['features'][5])
    for i in range(len(objects['features'])):
        data = objects['features'][i]['properties']
        sum = 0
        for obj in data:
            match = re.search("overnight_tourism_visitors" + ".*", obj)
            if match:
                sum += data[obj]
        record = {
            "tourism_region": data["tourism_region"],
            "state": data["state"],
            "rank": data["rank"],
            "tourist_num": sum
        }

        doc_id, doc_rev = database.save(record)

view_name = "_design/info"
if view_name in database:
    design_view = database[view_name]
else:
    design_view = {"_id": view_name}

design_view['views'] = {
    "top": {
        "map": "function (doc) {emit(doc.rank, {region:doc.tourism_region,num:doc.tourist_num});}"
    },
    "topRegion": {
        "map": "function (doc) {emit(doc.rank, doc.tourism_region);}"
     }
}

while True:
    try:
        database.save(design_view)
        break
    except couchdb.http.ResourceConflict:
        time.sleep(0.5)