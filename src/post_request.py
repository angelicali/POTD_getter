import json
import requests

NETID = "netid"
PASSWORD = "password"

data = {"j_username":NETID,"j_password":PASSWORD,'_eventId_proceed':"Login"}
data = json.dumps(data)

url = "https://prairielearn.engr.illinois.edu/cs225/"

s = requests.session()
r = s.get(url)



rr = s.post(r.url, data = data, allow_redirects=True)
print(r.url)
print(r.status_code)
print(rr.url)
print(rr.status_code)
cs225 = s.get(url)
print(cs225.url)
print(rr.history)