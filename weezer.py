

import requests
import sys
import json

if len(sys.argv) != 2:
    sys.exit()
response = requests.get ("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])
o = response.json()# o = object
for result in o['results']:
    print(result["trackName"])

#بكل اختصار نحن نتكلم عن المكتبه 
#json
#و في اخر ثلالث كودات قمنا بالاطلاع عليها
