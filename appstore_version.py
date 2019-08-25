# coding=utf-8
import requests
import re
import yagmail

new_version = "3.4.0"
from_email = 'xxx@qq.com'
psd = "xxx"
to_email = 'xxx@qq.com'

url = "https://apps.apple.com/cn/app/id1366525149"
def check_version(url):
    resp = requests.get(url)
    version = re.findall(r'版本 (.*?)<',resp.text)
    print(version[0])
    if version[0] == new_version:
        yag = yagmail.SMTP(user = from_email, password = psd, host = 'smtp.qq.com')
        content= "仓海帮"+new_version+"已经上传到App Store"
        yag.send(to = to_email, subject = 'App Store提醒', contents = content)
        return True

while True:
    if(check_version(url)):
        print("检测到新版本")
        break
