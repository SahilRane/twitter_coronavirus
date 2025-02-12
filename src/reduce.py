import code
from collections import defaultdict, Counter
import os
import json
import glob

directory = "/home/srane/twitter_coronavirus/src"
pattern = os.path.join(directory, "geoTwitter*")
files_lang = [f for f in os.listdir(directory) if f.startswith("geoTwitter") and f.endswith(".lang")]

files_country = [f for f in os.listdir(directory) if f.startswith("geoTwitter") and f.endswith(".country")]

counter_lang = defaultdict(Counter)
counter_country = defaultdict(Counter)

for file in files_lang:
    with open (file, 'r') as f:
        data = json.load(f)
        for k, v in data.items():
            counter_lang[k] += Counter(v)
for file in files_country:
    with open (file, 'r') as f:
        data = json.load(f)
        for k, v in data.items():
            counter_country[k] += Counter(v)

with open('reduce_lang', 'w') as f:
    f.write(json.dumps(counter_lang))

with open('reduce_country', 'w') as f:
    f.write(json.dumps(counter_country))

