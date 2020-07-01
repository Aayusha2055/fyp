# -*- coding: utf-8 -*-
# from __future__ import unicode_literals
#
# from django.test import TestCase
from account.models import *

# Create your tests here.


from bs4 import BeautifulSoup
from selenium import webdriver


browser = webdriver.PhantomJS()
browser.delete_all_cookies()
browser.get('http://mfd.gov.np/')
c = browser.page_source
soup = BeautifulSoup(c, "html.parser")

station_list = []
max_temp_list = []
mini_temp_list = []
rainfall_mm_list = []

station = soup.select('td:nth-child(1)')
max_temp = soup.select('td:nth-child(2)')
mini_temp = soup.select('td:nth-child(3)')
rainfall_mm = soup.select('.center~ .center+ td')

for i in station:
    station = (i.text)
    station_list.append(station)

for i in max_temp:
    max_temp = (i.text)
    max_temp_list.append(max_temp)

for i in mini_temp:
    mini_temp = (i.text)
    mini_temp_list.append(mini_temp)

for i in rainfall_mm:
    rainfall_mm = (i.text)
    rainfall_mm_list.append(rainfall_mm)

data_length = (len(max_temp_list))

for i in range(0, data_length):
    i = Observation.objects.create(station=station_list[i], max_temp = max_temp_list[i], mini_temp = mini_temp_list[i], rainfall_mm= rainfall_mm_list[i])
    i.save()











