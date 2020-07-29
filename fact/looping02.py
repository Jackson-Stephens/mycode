#!/usr/bin/env python3

# 1st example
#dnsfile = open("dnsservers.txt", "r")
#dnslist = dnsfile.readlines()
#for svr in dnslist:
#print(svr, end="")
#dnsfile.close


# 2nd example
# with open("dnsservers.txt", "r") as dnsfile:
    #dnslist = dnsfile.readlines()
    #for svr in dnslist:
       # print(svr, end="")

# 3rd example

with open("dnsservers.txt", "r") as dnsfile:
    for svr in dnsfile:
        print(svr, end="")



