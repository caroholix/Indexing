from oauth2client.service_account import ServiceAccountCredentials
import httplib2
import json

JSON_KEY_FILE = "amosix-indexing-api-key.json"   # <-- replace if different
URL_TO_SUBMIT = "https://amosix.in/"             # <-- replace with your URL

SCOPES = ["https://www.googleapis.com/auth/indexing"]

credentials = ServiceAccountCredentials.from_json_keyfile_name(JSON_KEY_FILE, scopes=SCOPES)
http = credentials.authorize(httplib2.Http())

endpoint = "https://indexing.googleapis.com/v3/urlNotifications:publish"

content = {
  "url": URL_TO_SUBMIT,
  "type": "URL_UPDATED"
}

response, body = http.request(
    endpoint,
    method="POST",
    headers={"Content-Type": "application/json"},
    body=json.dumps(content),
)

print("Status:", response)
print("Body:", body.decode())
