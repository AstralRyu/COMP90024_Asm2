import json
import couchdb

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