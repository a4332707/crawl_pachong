import queue
import random
import string
import threading

import time
from lxml import etree

import requests

# from day3.get_data import get_data
from IPdailichi import MyMysql

url='http://192.168.0.3/first/all/?num='

# headers='''Cookie: sessionid=4yhwm291y2ubyh0wz39gvmm4q7apeno5
# Referer: http://192.168.0.3/first/reg/?username=USdddsdf&password=PASdsafsdddd'''

#
# headers='''Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
# Accept-Encoding: gzip, deflate
# Accept-Language: zh-CN,zh;q=0.9
# Connection: keep-alive
# Cookie: sessionid=4yhwm291y2ubyh0wz39gvmm4q7apeno5
# Host: 192.168.0.3
# Referer: http://192.168.0.3/first/reg/?username=USdddsdf&password=PASdsafsdddd
# Upgrade-Insecure-Requests: 1
# User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'''
# headers=get_data(headers)
cookies={
    'Cookie':'sessionid=4yhwm291y2ubyh0wz39gvmm4q7apeno5'
              #sessionid=48kcr1x95cwj8t2a5hkjyuic4saj1hq6
}
def get_name():
    st=random.sample(string.ascii_letters.upper(),8)   #ascii_letters 随机选取
    username=(st[0]+st[1]+st[2]+st[3]+st[4]+st[5]+st[6]+st[7])
    st=random.sample(string.ascii_letters.upper(),8)
    password=(st[0]+st[1]+st[2]+st[3]+st[4]+st[5]+st[6]+st[7])

    header={
    'Cookie':'sessionid=4yhwm291y2ubyh0wz39gvmm4q7apeno5',
    'Referer':'http://192.168.0.3/first/reg/?username='+str(username)+"&password="+str(password)}
    return header

class Renmysql(MyMysql):
    def add_name(self,userid,name,anhao,idcard):
        sql="insert into t_pctest(userid,name,anhao,idcard) values (%s,%s,%s,%s)"
        self.cursor.execute(sql,(userid,name,anhao,idcard))
        self.conn.commit()
proxies={'http':'http//61.138.33.20:808'}
q=queue.Queue()
renmysql=Renmysql()

def put_name():
    while 1:
        q.put(get_name())

def get_teacher():
    num=3
    while num:

        header=q.get()
        print(header)
        html=etree.HTML(requests.get(url+str(num),cookies=cookies,headers=header).text)
        for i in html.xpath('//tr')[1:]:
            userid=i.getchildren()[0].text
            name=i.getchildren()[1].text
            anhao=i.getchildren()[2].text
            idcard=i.getchildren()[3].text
            renmysql.add_name(str(userid),str(name),str(anhao),str(idcard))

        num+=1
if __name__=="__main__":
    producer1=threading.Thread(target=put_name)
    producer2=threading.Thread(target=get_teacher)


    producer1.start()
    producer2.start()




