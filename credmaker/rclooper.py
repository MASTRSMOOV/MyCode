#!/usr/bin/env python3

#import the csv library
import csv

#file object
f = open("csv_users.txt", "r")

#set i equal to 0
i = 0

#use csv.reader()
for row in csv.reader(f):
    i = i + 1
#set filename equal to admin.rc%d
    filename = "admin.rc%d"%(i)
#write OS_AUTH_URL to rcfile
    rcfile = open(filename, "w")
    print("export OS_AUTH_URL=" + row[0], file=rcfile)
    print("export OS_IDENTITY_API_VERSION=3", file=rcfile)
    print("export OS_PROJECT_NAME=" + row[1], file=rcfile)
    print("export OS_PROJECT_DOMAIN_NAME=" + row[2], file=rcfile)
    print("export OS_USERNAME=" + row[3], file=rcfile)
    print("export OS_USER_DOMAIN_NAME=" + row[4], file=rcfile)
    print("export OS_PASSWORD=" + row[5], file=rcfile)
    rcfile.close()



