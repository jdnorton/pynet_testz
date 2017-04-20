

import json

with open("testfile.json") as f:
  my_list = json.load(f)

print json.dumps(my_list)
	