# Automatic-login-on-the-campus-network-of-UPC
中国石油大学华东校园网自动登录， python脚本
+ 使用了selenium，模拟浏览器行为，自动化操作，而非脚本
+ 提供可选的自动开启热点的操作
+ main.py中也有将本地IP通过邮箱自动发送的操作

本项目主要是用于在UPC搭建远程主机，设置脚本开机启动，就可以在开机后自动联网，自动开启热点

### auto.bat为主要脚本，其中主要是三部分
+ 隐藏CMD窗口
+ 启动运行main.py
+ 开启热点
