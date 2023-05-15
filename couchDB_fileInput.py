import json
import couchdb
import time

username = 'admin_yuki'
pwd = 'pwd12345'
link = f'http://{username}:{pwd}@172.26.133.179:5984/'
connect = couchdb.Server(link)

database = 'twitter_data'
if database not in connect:
    dbs = connect.create(database)
else:
    dbs = connect[database]

with open("twitter_output.json", "r", encoding='UTF-8') as line:
    while True:
        msg = line.readline().strip().rstrip(',')

        if msg == "":
            break

        msg_data = json.loads(msg)
        _id, _rev = dbs.save(msg_data)

view_name = "_design/info"
if view_name in dbs:
    design_view = dbs[view_name]
else:
    design_view = {"_id": view_name}

design_view['views'] = {
    "lang": {
        "map": "function(doc){emit(doc.lang,1)}"
    }
}

while True:
    try:
        dbs.save(design_view)
        break
    except couchdb.http.ResourceConflict:
        time.sleep(0.5)