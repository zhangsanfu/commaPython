# @Author  :  comma 
# @Date    :  2020-11-19 22:14


import requests
import urllib3


def getCookies():
    urllib3.disable_warnings()
    host = 'www.shop2cn.com'
    url = 'https://www.shop2cn.com/service/shop/api/accountlogin'  # 公版登录地址
    requestData = {"username": "18862396927",
                   "password": "q41ZxiimH+QTNSkdwYc1ybbNMo7c/vbuU+L2iRhEtTe1C+MyWk6XfDkCuPgj5JgoTIB4Cxmn/G2ECfbRyuxFN9mLllnUr0P7Lj2m4otCxyJ6ElGQx4vtQl+Uqb44zwP5wz6Ng7PUFFBEtDVyGvo6t3N4lTuWH/NN4C6xYKWsoNE="
                   }

    headers = {'Accept': 'application/json, text/plain, */*',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
               'Host': host}
    session = requests.session()
    responsedata = session.post(url, json=requestData, headers=headers, verify=False)
    responsedata.encoding='utf-8'
    print(responsedata.text)

if __name__ == '__main__':
    getCookies()