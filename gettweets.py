#!/usr/bin/python
"""
@author: vishal patel
@email: vkpatel@cmu.edu
"""
import pickle
import tweepy
import datetime
from getpass import getpass
username = raw_input('Twitter username: ')
password = getpass('Twitter password: ')
api = tweepy.API.new('basic',username,password)
pcount=1
loop=True
lastuptime=datetime.datetime.now()
lastuptime= datetime.datetime(2009,1,1)

fh = open("mytweets.txt","wb")
while loop:
    ftl = api.friends_timeline(count=200,page=pcount)
    if len(ftl)==0:
        loop=False
    for s in ftl:
        if s.created_at>lastuptime:
            try:
                storestr = "Id:%s\nUser:%s \n%s\n\nTime:%s\n==End==\n" %(unicode(str(s.id)), unicode(str(s.user.name)) ,unicode(str(s.text)), unicode(str(s.created_at)) )
                print storestr
                fh.write(storestr)
            except:
                print "couldnot decode id",s.id
    pcount+=1
    
fh.close()
