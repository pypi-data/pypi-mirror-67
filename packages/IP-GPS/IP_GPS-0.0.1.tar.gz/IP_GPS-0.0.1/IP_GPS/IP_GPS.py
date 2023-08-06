'''
This python3 script made by Bash
You can use 'from IP_GPS import get_gps, get_gps_dict'
get_gps will() return a string
get_gps_dict() will return a dict
https://freet-tk.gitee.io/
'''
import requests
from fake_useragent import UserAgent
import json
from GetProxyIp import get_proxy_ip
def get_gps(ipaddr):
    ua = UserAgent()
    headers = {'User-Agent': ua.random}
    url = "https://mall.ipplus360.com/center/ip/api?ip={}&type=district&coordsys=BD09".format(ipaddr)
    requests.packages.urllib3.disable_warnings()
    html = requests.get(url, verify=False, headers=headers, proxies=get_proxy_ip()).text
    html = html.replace('[', '')
    html = html.replace(']', '')
    Html = json.loads(html)
    ipstr = "IP地址：" + ipaddr + '\n' + "状态：" + Html["msg"] + '\n' + "亚洲：" + Html["data"]["continent"] + '\n' + "国家：" + \
            Html["data"]["country"] + '\n' + "省，市：" + Html["data"]["multiAreas"]["prov"] + '\n' + "区，县：" + \
            Html["data"]["multiAreas"]["district"] + '\n' + "经纬度：" + Html["data"]["multiAreas"]["lng"] + ',' + \
            Html["data"]["multiAreas"]["lat"] + '\n' + "邮政编码：" + Html["data"]["zipcode"] + '\n' + "覆盖半径：" + \
            Html["data"]["multiAreas"]["radius"] + "KM\n"
    return ipstr
def get_gps_dict(ipaddr):
    ip_dict = {}
    iip_list = []
    gps_text = get_gps(ipaddr)
    texh = gps_text.split('\n')
    for i in texh:
        acxs = i.split('：')
        iip_list.append(acxs)
    for y in range(0,9):
        ip_dict[iip_list[y][0]] = iip_list[y][1]
    return ip_dict
