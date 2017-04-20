

from ciscoconfparse import CiscoConfParse

cisco_cfg = CiscoConfParse("cisco_ipsec.txt")

print cisco_cfg

# find objects that begin with "crypto map CRYPTO" and include "set pfs group2"
crypto = cisco_cfg.find_objects_w_child(parentspec=r"^crypto map CRYPTO", childspec=r"set pfs group2")

print "\nObjects using PFS Group2"
print "------------------------"


# print the found objects and thier children
for i in crypto:
  print i.text

  






