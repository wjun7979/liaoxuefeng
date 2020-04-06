# -*- conding: utf-8 -*-
# 利用urllib读取JSON，然后将JSON解析为Python对象：

from urllib import request
import json

def fetch_data(url):
    with request.urlopen(url) as f:
        data = f.read().decode('utf-8')
        return json.loads(data)



# 测试
URL = 'https://yesno.wtf/api'
data = fetch_data(URL)
print(data)
assert data['answer'] == 'yes' and data['forced'] == False
print('ok')
