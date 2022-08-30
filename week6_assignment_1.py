import urllib.request, urllib.parse, urllib.error
import json

# Sample: http://py4e-data.dr-chuck.net/comments_42.json
# Actual: http://py4e-data.dr-chuck.net/comments_1599506.json

url = input("Enter - ")
url_handle = urllib.request.urlopen(url)
data = url_handle.read()

info = json.loads(data)
info = info["comments"]
print('User count:', len(info))

num = 0
for item in info:
    # print("count: ", item["count"])
    num += item["count"]
print(f"Sum: {num}")
    