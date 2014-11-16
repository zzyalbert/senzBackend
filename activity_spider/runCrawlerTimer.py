# -*- encoding:utf-8 -*-

from damai import DamaiSpider
from douban import DoubanSpider
from huodongxing import HuodongxingSpider
from threading import Thread
import sys
sys.path.append("../utils")
from timer import SchedTimer

def runCrawlers():
    print '爬虫将在24点运行...'
    damai = Thread(target=DamaiSpider().crawl)
    douban = Thread(target=DoubanSpider().crawl)
    huodongxing = Thread(target=HuodongxingSpider().crawl)
    #crawling with multi-threads
    damai.start()
    douban.start()
    huodongxing.start()

    damai.join()
    douban.join()
    huodongxing.join()
    print '本次爬取结束'

if __name__=="__main__":
    runCrawlers()
    t = SchedTimer(24,00,00)
    t.start(runCrawlers)
