# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpRequest, HttpResponseRedirect
from .models import *
from .forms import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect, reverse
from django.views.decorators.csrf import csrf_protect
from bs4 import BeautifulSoup
from selenium import webdriver





@csrf_protect
def custreg(request):
    if request.method == 'POST' :
        form = cust_reg_form(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=password)
            usr = auth.authenticate(username=username, password=password)
            auth.login(request, usr)
            return redirect(reverse('welcome'))
    else:
        form = cust_reg_form()
    return render(request, 'reg.html', {'form': form})


def login(request):
    if request.method == "POST" :
        username = request.POST['user']
        password = request.POST['psk']
        try:
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect(reverse('welcome'))
            else:
                messages.error(request, 'Username or password didn\'t match.')

        except auth.ObjectDoesNotExist:
            print("invalid user")

    return render(request, 'login.html')

@login_required(login_url="/account/login")
def welcome(request):
    observation_all = Observation.objects.all()
    return render(request, 'welcome.html' ,  { 'observation_all': observation_all})


@login_required(login_url="/account/login")
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/login')

@login_required(login_url="/account/login")
def info(request):
    observation_all = Observation.objects.all()
    return render(request, 'info.html' ,  { 'observation_all': observation_all})

def crawl(request):
    browser = webdriver.PhantomJS(executable_path= 'account/phantomjs')
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

    obser_obj = Observation.objects.all()
    obser_obj.delete()
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
        i = Observation.objects.create(station=station_list[i], max_temp=max_temp_list[i], mini_temp=mini_temp_list[i],
                                       rainfall_mm=rainfall_mm_list[i])
        i.save()
    observation_all = Observation.objects.all()
    return render(request, 'welcome.html', {'observation_all': observation_all, 'msg': 'crawled'})

