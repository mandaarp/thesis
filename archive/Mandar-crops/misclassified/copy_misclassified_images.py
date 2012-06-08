#!/usr/bin/python
import sys
import os

if len(sys.argv) != 2:
 print "usage: %s <.tab_file>"% (sys.argv[0])
 quit()

tab_file = sys.argv[1]
file_read = open(tab_file,'r')
lines = file_read.readlines()

thisline = lines[0].replace('\r\n','').split('\t')
command = 'mkdir %s_as_%s' % (thisline[0],thisline[2])
os.system(command)
command = 'mkdir %s_as_%s' % (thisline[2],thisline[0])
os.system(command)

for i in lines:
 thisline = i.replace('\r\n','').split('\t')
 print thisline   
 expected = thisline[0]
 imagepath = thisline[1]
 actual = thisline[2]
 command = 'cp .%s ./%s_as_%s/' % (imagepath,expected,actual) 
 print command
 os.system(command)
