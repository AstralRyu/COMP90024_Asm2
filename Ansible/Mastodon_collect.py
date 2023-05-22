import couchdb 
from mastodon import Mastodon, StreamListener
import json
import re
from deep_translator import GoogleTranslator

admin = 'admin_yuki'
password = 'pwd12345'
url = f'http://{admin}:{password}@172.26.133.179:5984/'
couch = couchdb.Server(url)

db_name = 'mastodon_data'

if db_name not in couch:
    db = couch.create(db_name)
else:
    db = couch[db_name]


token = 'HEztjdf5UugH-u-_XutVwaOnDiZ4McZ1zM7UNBD4auk'

m = Mastodon(
     api_base_url = f'https://mastodon.social',
     access_token=token
)

class Listener(StreamListener):
    def on_update(self, status):
        json_str = json.dumps(status, indent=2, sort_keys=True, default=str)
        json_object = json.loads(json_str)
        pattern = re.compile(r'<[^>]+>',re.S)
        result = pattern.sub('', json_object['content'])
        try:
            after_trans = GoogleTranslator(source='auto', target='en').translate(result)
        except Exception:
            after_trans = result

        check = False
        keyword = ['journey', 'holiday','sightseeing','business trip','trip','tourism','tourist','travelling','sydney','melbourne','golden coast','perth','adelaide']
        
        if after_trans != None:
            for i in keyword:
                if i in after_trans:
                    check=True
                    break
        
        if check == True:
            json_object['after_trans'] = after_trans
            doc_id, doc_rev = db.save(json_object)
            print(f'Document saved with ID: {doc_id} and revision: {doc_rev}' )

m.stream_public(Listener())



