import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
import socket
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from datetime import datetime
import os


def check_internet_connection():
    # 使用ping命令检测能否访问外部网站，这里以百度为例
    response = os.system(f"ping -n 1 baidu.com")
    if response == 0:
        print("Internet connection established")
        return True
    else:
        print("Internet connection unestablished, login again after 10 minutes")
        return False


# 连接校园网
options = Options()
options.add_argument('--headless')  # 启用无头模式
options.add_argument('--disable-gpu')  # 禁用GPU加速，提高性能

username_upc = "S2407001" # 学号
password_upc = "password" # 数字石大密码

while True:
    if check_internet_connection():
        break
    driver = webdriver.Edge(options=options)
    driver.get('https://lan.upc.edu.cn/') # 有线网络，无线网是wlan
    username_input = driver.find_element(By.ID, 'username')
    username_input.send_keys(username_upc)
    password_input = driver.find_element(By.ID, 'pwd')
    driver.execute_script("arguments[0].style.display = 'block';", password_input)
    password_input.send_keys(password_upc)
    dropdown_trigger = driver.find_element(By.ID, 'selectDisname')
    dropdown_trigger.click()
    time.sleep(0.5)
    dropdown_trigger = driver.find_element(By.ID, '_service_3')
    # _service_3是中国联通，0是校园网，1是移动，4是电信
    dropdown_trigger.click()
    login_button = driver.find_element(By.ID, 'loginLink_div')
    login_button.click()
    time.sleep(2)
    print("click login")
    if check_internet_connection():
        break
    else:
        time.sleep(600)


# 之后是可选功能：通过邮箱发送本地IP地址
# 适用于远程主机
# """
print("send message to mail")

# 将本地ip地址通过邮箱发送出去
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
try:
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
finally:
    s.close()

# 邮件服务器地址
smtp_server = 'smtp.qq.com'
# 发送者邮箱
sender = 'qqhaoma@qq.com'
# 接收者邮箱
receivers = ['qqhaoma@qq.com']
# 邮件服务器登录密码,smtp服务的密码
password = 'youxiang_password'

# 获取当前日期
current_date = datetime.now().date()

# 邮件正文
message = MIMEText(ip, 'plain', 'utf-8')
message['From'] = Header("qqhaoma@qq.com")
message['To'] = Header("qqhaoma@qq.com", 'utf-8')
message['Subject'] = Header(str(current_date), 'utf-8')

# 创建SMTP对象
smtp_obj = smtplib.SMTP(smtp_server, 587)  # 587是SMTP端口
smtp_obj.starttls()  # 启用TLS加密
smtp_obj.login(sender, password)
smtp_obj.sendmail(sender, receivers, message.as_string())

print("DONE")
smtp_obj.quit()
# """