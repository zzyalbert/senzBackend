#!/usr/bin/python
# -*- coding: utf-8 -*-
from math import *
import sys
import json
import sys
sys.path.append("../utils")
from avos_manager import *

#calulate distence from GPS
def distence(lon1, lat1, lon2, lat2):
        lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
        c = 2 * atan2(sqrt(a), sqrt(1-a))
        return 6371300 * c

def iso2timestamp(iso_time):
        t = time.strptime(iso_time, "%Y-%m-%dT%H:%M:%S.000Z")
        return long(time.mktime(t)*1000)

class UserActivityMapping(object):
        def __init__(self):
                self.avosManager = AvosManager()
                self.mappingList = {}
                self.users = {}
                self.activities = []
                
        #Consider whether user in this activity         
        def isInActivity(self,user,activity):
                aLon=activity['location']['longitude']
                aLat=activity['location']['latitude']
                activeTimes = []
                for oneTime in user:
                        uLon=oneTime['longitude']
                        uLat=oneTime['latitude']
                        if(distence(aLon, aLat, uLon, uLat)<100):
                                activeTimes.append(oneTime['timestamp'])

                if len(activeTimes) == 0:
                        return 0
                
                startTime = iso2timestamp(activity['start_time']['iso'])               
                endTime = iso2timestamp(activity['end_time']['iso']) if 'end_time' in activity else long(sys.maxint)*1000

                actives = len([timestamp for timestamp in activeTimes if timestamp>=startTime and timestamp<=endTime])
                if actives >= len(activeTimes)*0.5:
                        return 1
                else:
                        return 0
                        
        
        def getUserList(self):
                print 'Getting user list ...'
                L = 200
                start = 0
                res_len = L
                while res_len == L:                       
                        res = json.loads(self.avosManager.getData('location_record',limit=L, skip=start))['results']
                        res_len = len(res)
                        for user in res:
                                if user['userId'] not in self.users:
                                        self.users[user['userId']]=[user]
                                else:
                                        self.users[user['userId']].append(user);
                        start = start+L
                print 'Done'
                
        def getActivities(self):
                print 'Getting activities ...'
                L = 200
                start = 0
                res_len = L
                while res_len == L:                       
                        res = json.loads(self.avosManager.getData('activities' ,limit=L, skip=start))['results']
                        res_len = len(res)
                        self.activities = self.activities+res
                        start = start+L
                print 'Done'
                
        def mapping(self):
                self.getUserList()
                self.getActivities()

                for userId,user in self.users.items():
                        print 'Mapping user: id=  '+userId+' ...'
                        self.mappingList[userId] = []
                        for activity in self.activities:
                                if self.isInActivity(user,activity):
                                        self.mappingList[userId].append(activity['objectId'])
                        print 'Done'
                print 'Mapping finished!'
                             
        def dump2file(self,filename):
                print 'Dumping result to file: '+filename+' ...'
                f = open(filename,'w')
                f.write('No UserId       \tActivities\n');
                n=1
                for user,activities in self.mappingList.items():
                        line = unicode.encode(user,'utf8')+'\t'
                        for activity in activities:
                                line = line+unicode.encode(activity,'utf8')+'/'
                        line = line[:-1]+'\n\n\n\n'
                        f.write(str(n)+'  '+line);
                        n=n+1
                f.close()
                print 'Dumping finished!'

if __name__=="__main__":
        mapping = UserActivityMapping()
        mapping.mapping()
        mapping.dump2file('./mapping_result.txt')
