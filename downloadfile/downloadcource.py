import logging; logging.basicConfig(level=logging.INFO)
import requests 

logging.info ("downloading with requests")
for i in range(16):
    url = "https://github.com/michaelliao/awesome-python3-webapp/archive/day-{0:02d}.zip".format(i+1)
    # url = "https://github.com/michaelliao/awesome-python3-webapp/archive/day-%2d.zip" % (i+1) 
    bookname = "day-{0:02d}.zip".format(i+1)
    print('get book:{}'.format(bookname))
    r = requests.get(url) 
    # bookname = "day-{:2}.zip".format(i+1)  
    with open(bookname, "wb") as code:
        code.write(r.content)
 