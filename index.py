import os
import json
from oauth2client.service_account import ServiceAccountCredentials
import httplib2

# Read JSON from GitHub Secret
json_key = os.environ["GOOGLE_API_JSON"]

# Save JSON to file
with open("service_key.json", "w") as f:
    f.write(json_key)

SCOPES = ["https://www.googleapis.com/auth/indexing"]
credentials = ServiceAccountCredentials.from_json_keyfile_name("service_key.json", SCOPES)
http = credentials.authorize(httplib2.Http())

URL = os.environ.get("URL_TO_INDEX", "https://amosix.in/")
endpoint = "https://indexing.googleapis.com/v3/urlNotifications:publish"

content = {
    "url": URL,
    "type": "URL_UPDATED"
}

response, body = http.request(
    endpoint,
    method="POST",
    headers={"Content-Type": "application/json"},
    body=json.dumps(content)
)

print("Indexed:", URL)
print("Status:", response)
print("Body:", body.decode())
