import pymysql
import tushare

conn = pymysql.connect(host='localhost', user='root', password='root', database='stock', use_unicode=True, charset='utf8')
cursor=conn.cursor()
res=cursor.execute('truncate table stock_basic')
conn.commit()

tushare.set_token('028b2fde23ea28e87e2884d178b6d4c86776f691c4363c14d2d061f7')
pro = tushare.pro_api()
data =  pro.stock_basic(fields='ts_code,symbol,name,area,industry,list_date,market,is_hs,list_status,exchange,delist_date,curr_type')
data.head()
