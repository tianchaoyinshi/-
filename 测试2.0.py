# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 19:29:45 2020

@author: Lenovo
"""
#改进，随系统更新（当天打卡之后一直打卡）
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys  
import time
import datetime
curr_time = datetime.datetime.now()
time_str = curr_time.strftime("%m%d")
m=time_str[0:2]
d=time_str[2:4]
numm=int(m)
numd=int(d)
while 1:    

    startTime = datetime.datetime(2020,numm,numd,1,0,0)#第二天1点打卡

    if datetime.datetime.now() > startTime:
       print('打卡开始')
       chrome_options = Options()
       chrome_options.add_argument('–headless')
       chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver"#google浏览器驱动的位置
       driver = webdriver.Chrome(chromedriver,chrome_options=chrome_options)
       driver.get("https://onewechat.bnu.edu.cn/uc/wap/login?redirect=https%3A%2F%2Fonewechat.bnu.edu.cn%2Fncov%2Fwap%2Fdefault%2Findex%3Ffrom%3Dsinglemessage")
       driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[1]/input').send_keys('***********')#括号内填写账号
       driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/input').send_keys('***********')#括号内填写密码
       driver.find_element_by_xpath('//*[@id="app"]/div[3]').click()#确定
       time.sleep(2)
       driver.find_element_by_xpath('/html/body/div[1]/div/div/section/div[4]/ul/li[6]/div/input').click()#地理位置
       time.sleep(2)
       driver.find_element_by_xpath('/html/body/div[1]/div/div/section/div[4]/ul/li[11]/div/div/div[1]/span[1]').click()#温度
       time.sleep(2)
       driver.find_element_by_xpath('/html/body/div[1]/div/div/section/div[4]/ul/li[9]/div/div/div[1]/span[1]/i').click()#居住地
       time.sleep(2)
       driver.find_element_by_xpath('/html/body/div[1]/div/div/section/div[5]/div/a').click()#提交
       time.sleep(2)
       driver.find_element_by_xpath('//*[@id="wapcf"]/div/div[2]/div[2]').click()#最终确认
       time.sleep(2)
       driver.find_element_by_xpath('//*[@id="wapat"]/div/div[2]/div').click()#确认提交
       time.sleep(2)
       driver.close()
       numd=numd+1#去掉这个注释并且把后面的全删掉始终保持程序运行能一直打卡
    time.sleep(1800)