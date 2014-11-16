# -*- encoding:utf-8 -*-
#__author__ = 'Zhong.zy'

from __future__ import absolute_import
import json
import sys
sys.path.append("../utils")
from avos_manager import *
from util_opt import *

class PoiGenerator(object):
        def __init__(self):
                self.avos = AvosManager()
                
        def addPoiGroupByName(self,name,username):
                userId = self.avos.getUserIdByName(username)
                self.addPoiGroup(name,userId)

        def addPoiGroup(self,name,userId):
                user = dict(__type='Pointer',className='_User',objectId=userId)
                dataDict = dict(name=name,owner=user)
                self.avos.saveData('PoiGroup',dataDict)

        def getPoiGroupIdByName(self,poiGroupName,username):
                user = dict(__type='Pointer',className='_User',
                            objectId=self.avos.getUserIdByName(username))
                return self.avos.getIdByCondition('PoiGroup',name=poiGroupName,owner=user)               

        def addPoiGroupMemberByName(self,poiGroupName,username,lat,lng):
                poiGroupId = self.getPoiGroupIdByName(poiGroupName,username)
                if poiGroupId!=None:
                        self.addPoiGroupMember(poiGroupId,lat,lng)
                else:
                        print username + " has no PoiGroup called '"+ poiGroupName +"'"

        def addPoiGroupMember(self,poiGroupId,lat,lng):
                group = dict(__type='Pointer',className='PoiGroup',objectId=poiGroupId)
                dataDict = dict(poiGroup = group,location=gps2GeoPoint(lat,lng))
                self.avos.saveData('PoiGroupMember',dataDict)

        def getPoiGroupMembersByName(self,poiGroupName,username):
                poiGroupId = self.getPoiGroupIdByName(poiGroupName,username)
                if poiGroupId==None:
                        print username + " has no PoiGroup called '"+ poiGroupName +"'"
                else:
                        cond = dict(poiGroup=dict(__type='Pointer',className='PoiGroup',objectId=poiGroupId))
                        res = self.avos.getData('PoiGroupMember',where=json.dumps(cond))
                        memberList = json.loads(res)['results']
                        return [(member['location']['latitude'],member['location']['longitude']) for member in memberList]

        def deletePoiGroupMemberByName(self,poiGroupName,username,lat,lng):
                poiGroupId = self.getPoiGroupIdByName(poiGroupName,username)
                group = dict(__type='Pointer',className='PoiGroup',objectId=poiGroupId)
                objId = self.avos.getIdByCondition('PoiGroupMember',poiGroup=group,location=gps2GeoPoint(lat,lng))
                self.avos.deleteData('PoiGroupMember',str(objId))

        def deletePoiGroupByName(self,poiGroupName,username):
                poiGroupId = self.getPoiGroupIdByName(poiGroupName,username)
                if poiGroupId==None:
                        print username + " has no PoiGroup called '"+ poiGroupName +"'"
                else:
                        cond = dict(poiGroup=dict(__type='Pointer',className='PoiGroup',objectId=poiGroupId))
                        res = self.avos.getData('PoiGroupMember',keys='objectId',where=json.dumps(cond))
                        memberList = json.loads(res)['results']
                        for member in memberList:
                                self.avos.deleteData('PoiGroupMember',str(member['objectId']))
                        self.avos.deleteData('PoiGroup',str(poiGroupId))
                        

if __name__ == '__main__':
        poi = PoiGenerator()
        #poi.addPoiGroupByName('跑步','zhong1')
        #for i in range(1,6):
        #        poi.addPoiGroupMemberByName('跑步','zhong1',11+i,113)
        #poi.deletePoiGroupMemberByName('跑步','zhong2',13,113)
        #poi.deletePoiGroupByName('跑步','zhong1')
        print poi.getPoiGroupMembersByName('跑步','zhong1')
