#!/usr/bin/python
# -*- coding: utf-8 -*-
from util_opt import *
import re
import json
from avos_manager import *

class GeoCoder(object):
	def __init__(self):
		pass
	def geoCoding(self,region):
		url = "http://api.map.baidu.com/geocoder/v2/?address=%s&output=json&ak=fPnXQ2dVgLevy7GwIomnhEMg&callback=showLocation" % region
		result_info = get_source(url)
		try:
			lng_1 = float(re.findall(r'(?<=lng\":)[^,]+(?=,)', result_info)[0])
			lat_1 = float(re.findall(r'(?<=lat\":)[^}]+(?=})', result_info)[0])
		except:
			return 0.0,0.0
		#type
		poiType = json.loads(result_info[27:-1])['result']['level']

		#convert
		lng,lat = self.convert(lng_1,lat_1)
                #save to avos
		dataDict = {'name':region,'type':poiType,'lattitude':lat,'longitude':lng}
		avosManager = AvosManager()
		avosManager.updateDataByName('poiClass',region,dataDict)
		return lng,lat

	def convert(self,lng_1,lat_1):
		#convert
		convert_url = 'http://api.map.baidu.com/geoconv/v1/?coords=%s,%s&ak=fPnXQ2dVgLevy7GwIomnhEMg&from=1&to=5&output=json&callback=BMap.Convertor.cbk_7594' % (lng_1,lat_1)
		convert_info = get_source(convert_url)
		try:
			lng_2 = float(re.findall(r'(?<=x\":)[^,]+(?=,)', convert_info)[0])
			lat_2 = float(re.findall(r'(?<=y\":)[^}]+(?=})', convert_info)[0])
		except:
			return lng_1,lat_1		
		lng = 2*lng_1 - lng_2
		lat = 2*lat_1 - lat_2
		return lng,lat		

if __name__ == "__main__":
	geo = GeoCoder()
	region = "​中国票务在线上海站"
	lng,lat=geo.geoCoding(region)
	print lng,lat
