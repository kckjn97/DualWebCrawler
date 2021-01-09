#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium import webdriver
import re

class DualWebCrawler:
	def __init__(self, web_driver_path = None):
		options = FirefoxOptions()
		options.add_argument("--headless")

		if web_driver_path:
			self.driver = webdriver.Firefox(executable_path=web_driver_path, options=options, service_log_path='/dev/null')
			#print("webdriver init")
		else:
			self.driver = None

	def __del__(self):
		if self.driver:
			self.driver.quit()
		#print("webdriver quit")

	def request_html(self, url, use_selenium = False):
		if use_selenium :
			assert self.driver
			self.driver.get(url)
			self.driver.implicitly_wait(5)
			html = self.driver.page_source
			print('use selenium')

		else:
			headers = {'Content-Type': 'charset=utf-8', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}
			response = requests.get(url, headers=headers)
			assert response.status_code == 200
			html = response.content
		
		return html

	def _get_soup(self, url, selector, use_selenium):
		html = self.request_html(url, use_selenium)
		soup = BeautifulSoup(html, 'html.parser')

		if selector:
			selected = soup.select(selector)
			assert len(selected) > 0
			soup  = selected[0]
		return soup

	def _get_dual_scrap(self, url, selector, use_selenium, dual_scrap):
		if dual_scrap == True:
			try:
				soup = self._get_soup(url, selector, False)
			except:
				soup = self._get_soup(url, selector, True)
		else:
			soup = self._get_soup(url, selector, use_selenium)
		return soup

	def scrap(self, url, selector = None, dual_scrap = True, use_selenium = True, remove_html = True):
		soup = self._get_dual_scrap(url, selector, use_selenium, dual_scrap)

		if remove_html:
			_result = soup.get_text().strip()
			result = re.sub('\s\s+', ' ', _result)
		else:
			result = str(soup)
		return result

	def scrap_all(self, url, selector, dual_scrap = True, use_selenium = True, remove_html = True,):
		soup = self._get_dual_scrap(url, selector, use_selenium, dual_scrap)
		result = []
		for soup in selected:
			if remove_html:
				_result = soup.get_text().strip()
				result.append(re.sub('\s\s+', ' ', _result))
			else:
				result.append(str(soup))
		return result
