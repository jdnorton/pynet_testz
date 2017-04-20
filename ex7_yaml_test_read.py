

import yaml

with open("testfile.yaml") as f:
  my_list = yaml.load(f)

print yaml.dump(my_list, default_flow_style=False)
	