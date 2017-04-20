#
# Python script to test JSON input/output
#

import json

# create list
my_list = range(8)
my_list.append('whatever')
my_list.append('hello')
my_list.append({})
my_list[-1]
my_list[-1]['ip_addr'] = '10.1.2.3'
my_list[-1]['atrribs'] = range(7)

#my_list

#len(my_list)

# display contents of my_list
print json.dumps(my_list)

# write contents of my_list to file "testfile.json"
with open("testfile.json", "w") as f:
  json.dump(my_list, f)
	