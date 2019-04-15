import requests
import time
for i in range(1,89):
    url = 'https://book.yunzhan365.com/nvdn/pwml/files/mobile/%s.jpg'%i
    img=requests.get(url)
    with open("G:/2/%s.jpg"%time.time(),"wb") as code:
        code.write(img.content)
        print("下载第%s个完成"%i)