# -*- encoding:utf-8 -*- 

import sys
sys.path.append("../poi_generator")
from poiGenerator import *

def testAddPoiGroup():
        poi = PoiGenerator()
        poi.addPoiGroupByName('跑步','zhong2')

def testAddPoiGroupMember():
        poi = PoiGenerator()
        for i in range(1,6):
                poi.addPoiGroupMemberByName('跑步','zhong2',11+i,113)

def testDeleteGroupMember():
        poi = PoiGenerator()
        poi.deletePoiGroupMemberByName('跑步','zhong2',13,113)

def testDeleteGroup():
        poi = PoiGenerator()
        poi.deletePoiGroupByName('跑步','zhong1')
        
def testGetGroupMember():
        poi = PoiGenerator()
        print poi.getPoiGroupMembersByName('跑步','zhong1')

def main():
        testAddPoiGroup()
        testAddPoiGroupMember()
        testDeleteGroupMember()
        #testDeleteGroup()
        testGetGroupMember()

if __name__ == '__main__':
        main()
        


