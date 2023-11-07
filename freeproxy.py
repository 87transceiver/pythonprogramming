import requests
from bs4 import BeautifulSoup

# 定义代理网站的 URL
proxy_site_url = "http://spys.one/en/socks-proxy-list/" # 替换为实际的代理网站URL

# 发送 GET 请求并解析页面内容
response = requests.get(proxy_site_url)
soup = BeautifulSoup(response.content, "html.parser")

# 提取代理列表
proxy_list = []
for row in soup.find_all("tr"):
    columns = row.find_all("td")
    if len(columns) >= 2:
        ip = columns[0].text
        port = columns[1].text
        proxy_list.append(f"{ip}:{port}")

# 将代理列表保存到本地文本文件
with open("proxy_list.txt", "w") as file:
    for proxy in proxy_list:
        file.write(proxy + "\n")

print("代理列表已保存到 proxy_list.txt 文件")
