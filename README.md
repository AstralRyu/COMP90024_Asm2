# COMP90024_Asm2 Team 81
# Contributors
Yuan Feng: 1395290
Sihan Ma: 1379420
Jiaxin Liu: 1401237
Zijian Cai: 1371728
Jiahao Wu: 1306754   

# Structure
├── [Ansible/](https://github.com/AstralRyu/COMP90024_Asm2/tree/main/Ansible)                      
├── [mapbox/](https://github.com/AstralRyu/COMP90024_Asm2/tree/main/mapbox)                   
├── [grafana/](https://github.com/AstralRyu/COMP90024_Asm2/tree/main/grafana)  
├── [CouchDB/](https://github.com/AstralRyu/COMP90024_Asm2/tree/main/CouchDB)    

## Ansible
* Use private key to connect `172.26.128.84`
* Run `ansible-playbook harvester.yaml`

## CouchDB
* To upload Twitter in CouchDB http://172.26.133.179:5984/
   * run `mpiexec -np 8 python twitter_filter.py` to filter the tweets about travel
   * run over_night_fileInput.py and couchDB_fileInput.py
* To view CouchDB databases and corresponding views, visit http://172.26.133.179:5984/_utils/#login with username `admin_yuki` and password `pwd12345`

## Grafana
* To run a Grafana service, simply run `grafana_start.sh` in grafana folder
* To view the front end page, user can access http://172.26.135.46:3000/ and login as:
    * Viewer: with username of `guest` and password of `123456`, or
    * Administrator: with both username and password of `admin`.

## Mapbox
* To transfer the twitter data with spatial features into a GeoJson file, run `json_to_geojson.py` in mapbox folder.


