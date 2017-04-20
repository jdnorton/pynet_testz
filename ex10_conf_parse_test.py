

from ciscoconfparse import CiscoConfParse

cisco_cfg = CiscoConfParse("cisco_ipsec.txt")

print cisco_cfg

# find objects that begin with "crypto map CRYPTO" and are not 
crypto = cisco_cfg.find_objects_wo_child(parentspec=r"^crypto map CRYPTO", childspec=r"transform-set AES")

print "\nObjects not using AES"
print "------------------------"

# print the found objects and thier children
for i in crypto:
  print i.text

  






