# dual-web-crawler
hybrid web crawler using selenium and request library selectively.

## Intro
웹페이지의 정보를 크롤링하기 위해서 `request`라이브러리르 많이 사용한다.
하지만 `request`를 단순히 사용해서는 SPA(Single pag application) 같은 Dyanmic web page의 정보를 읽어오기 어렵다.
이 경우, `selenium`을 사용하면 자바스크립트에 의해 로딩되는 부분도 쉽게 읽어올 수 있다.
하지만 `selenium`는 웹페이지 소스코드를 파싱하고 수행하기 때문에 `HttpRequest`를 단독으로 사용할 때보다 시간이 느린 문제가 있다.

빠르게 데이터를 읽어오기 위해서, `dual-web-cralwer`는 먼저 `request`를 통해 웹페이지를 크롤링한다.
만약 원하는 데이터가 없을 경우, selenium을 통해서 2차적으로 웹페이지를 크롤링한다.

`dual-web-crawler`는 웹페이지에서 원하는 데이터를 읽어오기 위해서 URI과 CSS selector를 입력받는다.

## Usage
1. selenium을 사용할 수 있도록, web driver의 경로를 입력하여 초기화한다.
	(입력하지 않을경우, `request`만 단독으로 사용된다)
	```python
	WEB_DRIVER_PATH = '/usr/local/bin/geckodriver'
	crawler = DualWebCrawler(WEB_DRIVER_PATH)
	```
1. 원하는 데이터의 URI와 CSS selector를 입력하면 데이터를 읽어올수 있다.
	```python
	data = crawler.scrap("https://www.google.com/search?q=python", selector="#result-stats", use_selenium=False, remove_html=True)
	print(data)
	```
	
	- `scrap (uri, selector=None, use_selenium=True, remove_html=True)`
		- `uri`: 필수
			웹페이지의 URI.
		- `selector`: 선택, None
			읽어올 데이터의 CSS selector.
			없을 경우, 웹페이지 전체 소스코드를 리턴
		- `use_selenium`: 선택, True
			selenium의 사용여부.
			False일 경우, `request`만 단독으로 사용
		- `remove_html`: 선택, True
			HTML 태그 제거 유무.
			False일 경우, HTML 태그를 포함한 데이터를 리턴하고, True일 경우 텍스트만 리턴
			
