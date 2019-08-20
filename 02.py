
import tushare

# tushare.set_token('你的token，在账号登录后的个人主页里找')
tushare.set_token('bfc8c4db935f95de5924f273abd26372bd4e5b15b2ee35118aa934f8')
pro = tushare.pro_api()
# data = pro.stock_basic()
data = pro.stock_basic(fields='ts_code,symbol,name,area,industry,list_date,market,is_hs,list_status,exchange,delist_date,curr_type')

print(data)
