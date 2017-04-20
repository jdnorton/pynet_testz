

from ciscoconfparse import CiscoConfParse

cisco_cfg = CiscoConfParse("cisco_ipsec.txt")

print cisco_cfg

# find objects that begin with "crypto map CRYPTO"
crypto = cisco_cfg.find_objects(r"^crypto map CRYPTO")

# print the found objects and thier children
for i in crypto:
  print i.text

  for c in i.children:
    print c.text


print "----------------------"

for i in crypto:
  print i.text

  for c in i.children:
    print c.text

    if (c.text == "set pfs group2"):
      print c.text





