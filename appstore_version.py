# coding=utf-8
import requests
import re

url = "https://apps.apple.com/cn/app/id1366525149"
resp = requests.get(url)
# print(resp.text)
version = re.findall(r'版本 (.*?)<',resp.text)
print(version[0])