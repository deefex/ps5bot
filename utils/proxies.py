# import requests
# from itertools import cycle
# import random
# import traceback
# from lxml.html import fromstring


# def get_proxies():
#     my_url = 'https://free-proxy-list.net/'
#     my_response = requests.get(my_url)
#     parser = fromstring(my_response.text)
#     my_proxies = set()
#     for x in parser.xpath('//tbody/tr')[:10]:
#         if x.xpath('.//td[7][contains(text(),"yes")]'):
#             my_proxy = ":".join([x.xpath('.//td[1]/text()')[0], x.xpath('.//td[2]/text()')[0]])
#             my_proxies.add(my_proxy)
#     return my_proxies
#
#
# proxies = get_proxies()
# proxy = random.choice(tuple(proxies))
# print(proxies)
# print(proxy)
# proxy_pool = cycle(proxies)
#
# url = 'https://httpbin.org/ip'
# for i in range(1, 11):
#     # Get a proxy from the pool
#     proxy = next(proxy_pool)
#     print("Request #%d %s......" % (i, proxy), end="")
#     try:
#         response = requests.get(url, proxies={"http://": proxy, "https://": proxy})
#         print(response.status_code)
#     except Exception as e:
#         # Most free proxies will often get connection errors. You will have retry the entire request using another
#         # proxy to work. We will just skip retries as its beyond the scope of this tutorial and we are only downloading
#         # a single url
#         print("Skipping......", e)
