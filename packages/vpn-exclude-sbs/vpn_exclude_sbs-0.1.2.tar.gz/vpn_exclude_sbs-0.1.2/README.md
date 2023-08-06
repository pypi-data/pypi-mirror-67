# vpn_exclude_sbs

This is a package for excluding DNSs from the VPN connection the PC connected to.

You can either pass a domain name to exclude, or a specifiec ip address.

# How to use ?

# 1. For excluding a url -
python -m vpn_exclude_sbs -url < domain name >

# 2. For excluding a specifiec ip address -
python -m vpn_exclude_sbs -ip < ip address >

# Prerequisites:

The module uses 'netifaces' module.
For the module to work well, first, you need to install the 'netifaces' module.

You can do it by:
pip install netifaces

# Additional Information:

The modules supports only Windows operating system.

The module requires administrator privileges to work well; <br>
Since, by default - win os requires admin privilege to modify routing table.

