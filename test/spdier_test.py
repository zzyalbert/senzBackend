# -*- encoding:utf-8 -*- 

import sys
sys.path.append("../activity_spider")
from damai import DamaiSpider
from douban import DoubanSpider
from huodongxing import HuodongxingSpider
import runCrawlerTimer

def testDamai():
	spider=DamaiSpider()
	spider.crawl()

def testDouban():
	spider=DoubanSpider()
	spider.crawl()

def testHuodngxing():
	spider=HuodongxingSpider()
	spider.crawl()

def testMulti_thread_crawl():
        runCrawlerTimer.multi_thread_crawl()

def testRunTimer():
        runCrawlerTimer.runCrawler()

def main():
	testDamai()
	testDouban()
	testHuodngxing()
	#testRunTimer()
	testMulti_thread_crawl()

if __name__ == '__main__':
	main()
        


