import os
from oauth2client.service_account import ServiceAccountCredentials
import httplib2
import json

# Read JSON key from environment variable
json_key = os.environ["GOOGLE_API_JSON"]
json_key_file = "service_key.json"

# Write JSON key to file
with open(json_key_file, "w") as f:
    f.write(json_key)

# URL to index
URL = os.environ.get("URL_TO_INDEX", "https://amosix.in/")

SCOPES = ["https://www.googleapis.com/auth/indexing"]

credentials = ServiceAccountCredentials.from_json_keyfile_name(json_key_file, scopes=SCOPES)
http = credentials.authorize(httplib2.Http())

endpoint = "https://indexing.googleapis.com/v3/urlNotifications:publish"

content = {
  "url": URL,
  "type": "URL_UPDATED"
}

response, body = http.request(
    endpoint,
    method="POST",
    headers={"Content-Type": "application/json"},
    body=json.dumps(content),
)

print("Indexed:", URL)
print("Status:", response)
print("Body:", body.decode())
