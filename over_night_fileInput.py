import couchdb
import ijson
import json
import re

# authentication
admin = 'admin_yuki'
password = 'pwd12345'
url = f'http://{admin}:{password}@172.26.133.179:5984/'

# get couchdb instance
couch = couchdb.Server(url)

# indicate the db name
db_name = 'over_nightdata'

# if not exist, create one
if db_name not in couch:
    db = couch.create(db_name)
else:
    db = couch[db_name]


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
            "tourist_num":sum
        }

        doc_id, doc_rev = db.save(record)
