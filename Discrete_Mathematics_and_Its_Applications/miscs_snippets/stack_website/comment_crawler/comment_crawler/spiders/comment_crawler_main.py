import scrapy
import re
from os.path import expanduser
import os

"""
1. First use log enabled to see whether problems exist.
2. CSS reference https://www.freecodecamp.org/news/css-selectors-cheat-sheet-for-beginners/
"""


class CommentCrawlerMainSpider(scrapy.Spider):
  name = "comment_crawler_main"
  allowed_domains = ["*.stack*.com"]
  # start_urls = ["https://math.stackexchange.com/questions/285134/can-a-recurrence-relation-have-more-than-one-exact-solution"]
  url_pattern = '\(https://[^ ]*\.stack[^ ]*comment(\d+)_\d+'
  # get cookies in browser https://www.scraperapi.com/blog/headers-and-cookies-for-web-scraping/
  # cookies={
  #     'prov':'4a829a97-2696-4dac-b96c-7694db6e6bc1',
  #     'OptanonAlertBoxClosed':'2024-04-23T23:48:59.359Z',
  #     '__cflb':'0H28vFHtoAR1ohjxFgDZBwZ5H5NWURYHdEoQgGWWp7N',
  #     '__cf_bm':'IGbLWQUhhJWbmaV7Vx1K0h5nz.7LA01MZ6kDJ4vrLLk-1714050023-1.0.1.1-GG7tOPNe1O2hh_IPTodIN7BxwGlUFftzyzsuA7CUsLnrr8jIH.TvG5StinRZsfveeJjY0UPuou3gKr9vXdRcTw',
  #     'acct':'t=iSssKwMt5Kze0xR4sILhhsMz2Pg%2fdzQa&s=q5viw4VJIYIi3sViJb8ZVEQO6BHCnzBJ',
  #     'OptanonConsent':'isGpcEnabled=0&datestamp=Thu+Apr+25+2024+21%3A02%3A43+GMT%2B0800+(China+Standard+Time)&version=202312.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A0%2CC0003%3A0%2CC0004%3A0&geolocation=US%3BCA&AwaitingReconsent=false'
  # }
  # get headers https://stackoverflow.com/a/72909854/21294350 or response.headers
  headers = {
      b'Date': b'Thu, 25 Apr 2024 13:52:14 GMT',
      b'Content-Type': b'text/html; charset=utf-8',
      b'Cache-Control': b'private',
      b'Last-Modified': b'Fri, 29 Mar 2024 02:23:49 GMT',
      b'Vary': b'Accept-Encoding',
      b'Strict-Transport-Security': b'max-age=15552000',
      b'X-Frame-Options': b'SAMEORIGIN',
      b'X-Request-Guid': b'd94ba145-9a1c-446c-85bf-1fe47edba76f',
      b'Set-Cookie': b'prov=39997d58-ef6b-459c-833c-01f76bdb6534; expires=Fri, 25 Apr 2025 13:52:14 GMT; domain=.stackexchange.com; path=/; secure; samesite=none; httponly',
      b'Content-Security-Policy': b"upgrade-insecure-requests; frame-ancestors 'self' https://stackexchange.com",
      b'Cf-Cache-Status': b'DYNAMIC',
      b'X-Dns-Prefetch-Control': b'off',
      b'Server': b'cloudflare',
      b'Cf-Ray': b'879ecffc3b8b7cf5-LAX'
  }

  def start_requests(self):
    home = expanduser("~")
    target_files = []
    rootdirs = [f'{home}/Discrete_Mathematics_and_Algorithm/',
                '/mnt/ubuntu/home/hervey/csapp3e']
    regex = re.compile('(.*md$)')
    for rootdir in rootdirs:
      print(rootdir)
      # https://stackoverflow.com/a/39294155/21294350
      for root, _, files in os.walk(rootdir):
        for file in files:
          if regex.match(file):
            target_files.append(os.path.join(root, file))
    urls = []
    for target_file in target_files:
      print(f"check {target_file}")
      # https://stackoverflow.com/a/6186991/21294350
      urls = urls + [re.search(self.url_pattern, line)
                     for line in open(target_file)]
    urls = [x.group(0)[1:] for x in urls if x != None]
    # print(urls)
    for url in urls:
        # https://doc.scrapy.org/en/latest/topics/request-response.html?highlight=Request#errback-cb-kwargs
      yield scrapy.Request(url=url, callback=self.parse, cb_kwargs=dict(origin_url=url), headers=self.headers)

  def parse(self, response, origin_url):
    # print(f"begin parse {origin_url}")
    # https://stackoverflow.com/questions/59780089/one-liner-to-assign-if-not-none#comment118372090_59780160
    id = id_group.group(1) if (id_group := re.search(
        self.url_pattern[2:], origin_url)) is not None else 0
    if id == 0:
      print(f"error {origin_url} with {self.url_pattern[2:]}")
      return
    else:
      # print(f"\n{origin_url} -> {id}")
      pass
    parent_pattern = f'li[id*=comment-{id}] span[class="comment-copy"]'
    # https://doc.scrapy.org/en/latest/intro/tutorial.html#following-links
    if (sub_link := response.css(parent_pattern+' a::attr(href)')):
      if 'stack' not in sub_link:
          # if response.css(parent_pattern+' a[href]'):
        print(f"\n{origin_url}\n"+response.css(parent_pattern).get())
        yield ({'link': sub_link.get()})
