import requests
from bs4 import BeautifulSoup

def fetch_socks5_proxies(url):
    proxies = []
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        proxy_elements = soup.find_all('tr')  # 假设代理信息在表格的每一行<tr>中
        
        for proxy_element in proxy_elements:
            columns = proxy_element.find_all('td')  # 假设每一行中的代理信息在<td>标签中
            if len(columns) >= 2:
                ip = columns[0].text.strip()
                port = columns[1].text.strip()
                proxy = f"{ip}:{port}"
                proxies.append(proxy)
        
    return proxies

if __name__ == "__main__":
    target_url = "https://example.com/socks5-proxies"  # 替换为实际的网站链接
    socks5_proxies = fetch_socks5_proxies(target_url)
    
    if socks5_proxies:
        print("Fetched SOCKS5 Proxies:")
        for proxy in socks5_proxies:
            print(proxy)
    else:
        print("No SOCKS5 proxies found.")
