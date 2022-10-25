# ok this is not exactly like I asked you to to in the labs
import requests
import json
from config import config as cfg

filename = "repos-private.json"

#url = 'https://api.github.com/repos/andrewbeattycourseware/datarepresentation/contents/code'
url = 'https://api.github.com/repos/CiaranMoran27/aprivateone'
apikey = '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'

response = requests.get(url, auth = ('token', apikey))
with  open(filename, 'w') as fp:
    repoJSON = response.json()
    json.dump(repoJSON, fp, indent=4)