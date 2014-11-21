# -*- encoding:utf-8 -*- 

import json
import datetime
import requests
import sys
sys.path.append("../utils")
from avos_manager import *
from util_opt import *
import settings


def getDataSample():
        start = "2013-05-05 20:30:45"
        date_utc = getUtcDate(start)
        start_utc = timeConvet2utc(start)       
        start_iso = start_utc.replace(" ","T")+".000Z"
        date_iso = date_utc.replace(" ","T")+".000Z"
        date_time = dict(__type='Date',iso=date_iso)    
        start_time = dict(__type='Date',iso=start_iso)
        end_time = dict(__type='Date',iso=start_iso)
        dataDict = {"name":"《文成公主》大型实景剧","date":date_time,
        "start_time":start_time,"end_time":end_time,"ticket":"220","region":"北京市海淀区北京邮电大学","location":gps2GeoPoint(39.970513,116.361834),"category":""}
        return dataDict

def testSave():
        avosManager = AvosManager()
        className = "testDate"
        dataDict = getDataSample()
        avosManager.saveData(className,dataDict)


def testSaveActivity():
        avosManager = AvosManager()
        dataDict = getDataSample()
        avosManager.saveActivity(dataDict)


def testUpdate():
        avosManager = AvosManager()
        avosManager.updateDataByName('activities','《文成公主》大型实景剧',dict(ticket='200'))


def testUser():
        avosManager = AvosManager()
        avosManager.createUser(dict(username='zhong7',password='123'))
        id = avosManager.getUserIdByName('zhong7')
        print id

def testGetId():
        avosManager = AvosManager()
        id = avosManager.getIdByCondition('TestClass',name='b',test_num=111)
        print id

def testGeoPoint():
        avosManager = AvosManager()
        avosManager.saveData('geopointDemo',dict(geopoint=gps2GeoPoint(11,23)))
        
def main():
        testSave()
        testSaveActivity()
        testUpdate()
        testUser()
        testGetId()
        testGeoPoint()

if __name__ == '__main__':
        main()
        


