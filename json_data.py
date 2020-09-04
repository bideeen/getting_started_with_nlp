# Import the necessary libraries
import json, requests
# json file from "https://quotes.rest/qod.json"
r = requests.get("https://quotes.rest/qod.json")
# response
res = r.json()
# print(json.dumps(res, indent=4))
# Extracting content
q = res['contents']['quotes'][0]
# Extract only quote
print(q['quote'], '\n--', q['author'])