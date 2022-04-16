import requests as req

url='https://tw.appledaily.com/home/'
url2='https://tw.appledaily.com/https://tw.appledaily.com/forum/20220410/QOAEZBQLLJDAJC4JCV7HERUCUA/'
url3='https://httpbin.org/get'
r = req.get(url3)
print(r.text)
# print(r.headers)


# with open ('123.jpg', mode='wb') as file:
#     file.write(r.content)





