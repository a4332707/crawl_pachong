import MySQLdb
import requests
from lxml import etree

class MyMysql(object):
    def __init__(self):
         self.conn=MySQLdb.connect(
            host='127.0.0.1',port=3306,
            user='root',password='000000',charset='utf8',db='dbzhilian'
        )
    #保存ip到数据库
    def save(self,ip_type,ip_port):
        sql='insert into t_ips(ip_type,ip_port)VALUES (%s,%s)'
        self.conn.cursor().execute(sql,[ip_type,ip_port])
        self.conn.commit()
    # 从数据库取ip地址
    def get_ip(self):
        sql = 'select ip_type,ip_port from t_ips limit 0,1'
        cursor=self.conn.cursor()
        cursor.execute(sql)
        result=cursor.fetchone()
        self.delete_ip(result[1])
        return result
    # 删除已经取出的ip地址
    def delete_ip(self,ip_prot):
        sql='delete from t_ips where ip_port=%s'
        self.conn.cursor().execute(sql,[ip_prot])
        self.conn.commit()
    # 获取数据库所有ip的数量
    def get_count(self):
        sql='select count(id) from t_ips'
        cursor = self.conn.cursor()
        cursor.execute(sql)
        return cursor.fetchall()[0][0]
    # 从数据库获取所有ip地址
    def get_all(self):
        sql='select ip_type,ip_port from t_ips'
        cursor = self.conn.cursor()
        cursor.execute(sql)
        ips = cursor.fetchall()
        return ips


class IP_chi(object):
    def __init__(self,index,yuzhi,host_ip):
        self.index=index
        self.db=MyMysql()
        self.yuzhi=yuzhi
        self.host_ip=host_ip
    # 采集ip,并将可用的ip存入数据库
    def get_ip_from_xici(self):
        url='http://www.xicidaili.com/nn/'+str(self.index)
        html=etree.HTML(requests.get(url,headers={
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'
        }).text)
        for tr in html.xpath('//tr[@class="odd"]'):
            tds=tr.getchildren()
            ip=tds[5].text.lower() + '://' + tds[1].text + ':' + tds[2].text
            if self.check_ip(ip):
                self.db.save(tds[5].text.lower(),tds[1].text + ':' + tds[2].text)

    # 检测ip可用性,并保存到数据库
    def check_ip(self,target_ip):
        check_url='http://httpbin.org/ip'
        ip=target_ip.split('://')
        proxies={ip[0]:target_ip}
        try:
            t_ip=requests.get(url=check_url,proxies=proxies,timeout=3).text
            if t_ip!=self.host_ip:
                return True
        except:
            pass
        return False
    # 取出ip，并检测池的ip数量是否小于阈值
    def get_ip(self):
        self.check_ip_for_yuzhi()
        return self.db.get_ip()
    def check_ip_for_yuzhi(self):
        count=self.db.get_count()
        while count< self.yuzhi:
            print(count)
            self.index += 1 #换下一页
            self.get_ip_from_xici()   #采集可用ip，并入库
            count = self.db.get_count()
    # 定时检测ip池里面的ip
    def check_ip_for_time(self):
        # 获取所有ip地址
        ips=self.db.get_all()
        # 依次检测ip地址可用性
        for ip in ips:
            if not self.check_ip(ip[0]+'://'+ip[1]):
                self.db.delete_ip(ip[1])
        # 判断数据库中ip的总量是否小于阈值
        self.check_ip_for_yuzhi()
if __name__ == '__main__':
    host_ip=requests.get('http://httpbin.org/ip').text
    ipc = IP_chi(index=0,yuzhi=2,host_ip=host_ip)
    ipc.check_ip_for_yuzhi()
    # db=MyMysql()
    # print(db.get_count())
    # for i in range(100):
    #     ipc.index=i
    #     ipc.get_ip_from_xici()