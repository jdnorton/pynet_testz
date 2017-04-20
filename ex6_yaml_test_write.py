#
# Python script to test YAML input/output
#

import yaml

# create list
my_list = range(8)
my_list.append('whatever')
my_list.append('hello')
my_list.append({})
my_list[-1]
my_list[-1]['ip_addr'] = '10.1.2.3'
my_list[-1]['atrribs'] = range(7)
my_list[-1]['whatever'] = 'test'


#my_list

#len(my_list)

# display contents of my_list
print yaml.dump(my_list, default_flow_style=False)

# write contents of my_list to file "testfile.yaml"
with open("testfile.yaml","w") as f:
  f.write(yaml.dump(my_list, default_flow_style=False))
	