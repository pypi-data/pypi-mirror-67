'''
This python3 script made by Bash
You can 'from GetProxyIp *' to use this moudle
get_proxy_iplist() will return a list
get_proxy_ip() will return a dic
https://freet-tk.gitee.io/
'''
import requests
from fake_useragent import UserAgent
import re
import random
def get_proxy_iplist():
    ua = UserAgent()
    headers = {'User-Agent':ua.random}
    url ="https://www.kuaidaili.com/free"
    requests.packages.urllib3.disable_warnings()
    html = requests.get(url,verify=False,headers=headers)
    strs = html.text
    proxy_ip = re.findall('<td data-title="IP">(.*?)</td>',strs)
    proxy_port = re.findall('<td data-title="PORT">(.*?)</td>',strs)
    proxy_type = re.findall('<td data-title="类型">(.*?)</td>',strs)
    dip = []
    len_ip = len(proxy_ip)
    for i in range(0,len_ip):
        list_valeu = proxy_type[i].lower()  + ': '  + proxy_ip[i] + ':' + proxy_port[i]
        dip.append(list_valeu)
    return dip
def get_proxy_ip():
    np = random.randint(1,14)
    ipdic = {}
    ip_dic = get_proxy_iplist()[np]
    ip_ddd = ip_dic.split(': ')
    ipdic[ip_ddd[0]] = ip_ddd[1]
    return ipdic
