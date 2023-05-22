import requests, json

result = requests.get("http://admin_yuki:pwd12345@172.26.133.179:5984/twitter_data_geo/_design/info/_view/spot_sentiment")

result_json = result.json()

geojson_result = {
    "type": "FeatureCollection",
    "features": []
}

for row in result_json["rows"]:
    corrdinate = [row["key"][0], row["key"][1]]
    sentiment = row["value"]
    new_row = {
        "type": "Feature",
        "geometry": {
            "type": "Point",
            "coordinates": corrdinate
        },
        "properties": {
            "sentiment": sentiment
        } 
    }
    geojson_result["features"].append(new_row)
    
with open("twitter_data_geo.geojson", "w") as f:
    json.dump(geojson_result, f)
    print(json.dumps(geojson_result))