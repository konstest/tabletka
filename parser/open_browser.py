#! /usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


'''
Открытие браузера и ввод поискового слова: МИРАМИСТИН
'''
capabilities=DesiredCapabilities.FIREFOX.copy()
capabilities['javascriptEnabled']=True
browser = webdriver.Remote(
   command_executor='http://127.0.0.1:4444/wd/hub',
   desired_capabilities=capabilities
)

url="http://tabletka.online/"
print('Go to website: {}'.format(url))
browser.get(url)
