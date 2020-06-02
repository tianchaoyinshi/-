# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 20:14:02 2020

@author: Lenovo
"""
#每天睡觉前运行或者直接按照最后一个注释操作使得程序一直运行每天打卡，有条件可以放在服务器上一直跑每天打卡。
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys  
import time
import datetime
import os
curr_time = datetime.datetime.now()
time_str = curr_time.strftime("%m%d")
m=time_str[0:2]
d=time_str[2:4]
numm=int(m)
numd=int(d)
#numd=numd+1#前一天晚上打开程序
num=0
while 1:
    startTime = datetime.datetime(2020,numm,numd,1,0,0)#第二天1点打卡
    time.sleep(2)
    while datetime.datetime.now() > startTime:
       print('打卡开始')
       chrome_options = Options()
       chrome_options.add_argument('–headless')
       chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver"#google浏览器驱动的位置
       driver = webdriver.Chrome(chromedriver,chrome_options=chrome_options)
       driver.get("https://onewechat.bnu.edu.cn/uc/wap/login?redirect=https%3A%2F%2Fonewechat.bnu.edu.cn%2Fncov%2Fwap%2Fdefault%2Findex%3Ffrom%3Dsinglemessage")
       driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[1]/input').send_keys('xxxxxxxxxxx')#括号内填写账号
       driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/input').send_keys('xxxxxxxxxxx')#括号内填写密码
       driver.find_element_by_xpath('//*[@id="app"]/div[3]').click()
       time.sleep(2)
       driver.find_element_by_xpath('/html/body/div[1]/div/div/section/div[4]/ul/li[7]/div/input').click()
       time.sleep(2)
       driver.find_element_by_xpath('/html/body/div[1]/div/div/section/div[5]/div/a').click()
       time.sleep(2)
       driver.find_element_by_xpath('//*[@id="wapcf"]/div/div[2]/div[2]').click()
       time.sleep(2)
       driver.find_element_by_xpath('//*[@id="wapat"]/div/div[2]/div').click()
       time.sleep(1)
       driver.close()
       #numd=numd+1#去掉这个注释并且把后面的全删掉始终保持程序运行能一直打卡
       num=num+1
       if num == 1:
           os._exit(0)
           #os.system('shutdown /s /t 10')可以选择关机，但要把上一行注释掉
       else:
           print("erro")
      

