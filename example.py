#!/usr/bin/python3
import sys
from dual_web_crawler import DualWebCrawler
	
if __name__ == "__main__":
	if len(sys.argv) < 2:
		print("input URL [CSS-selector]")
		sys.exit(-1)

	url = sys.argv[1]
	selector = None
	if len(sys.argv) > 2:
		selector = sys.argv[2]

	WEB_DRIVER_PATH = '/usr/local/bin/geckodriver'
	crawler = DualWebCrawler(WEB_DRIVER_PATH)
	data = crawler.scrap(url, selector=selector, use_selenium=True, remove_html=True)
	print(data)
