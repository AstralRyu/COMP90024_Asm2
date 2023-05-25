* To run a Grafana service, simply run grafana_start.sh in grafana folder
* To view the front end page, user can access http://172.26.135.46:3000/ and login as:
    * Viewer: with username of "guest" and password of "123456", or
    * Administrator: with both username and password of "admin".

* To upload Twitter in CouchDB
   * run `mpiexec -np 8 python twitter_filter.py` to filter the tweets about travel
   * run over_night_fileInput.py and couchDB_fileInput.py
