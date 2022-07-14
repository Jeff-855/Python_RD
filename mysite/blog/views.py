from django.shortcuts import render,redirect
from .models import Post
from .models import Test
from .forms import TestModelForm
from django.template import Context

import time
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.support.select import Select
import csv
import random

from datetime import datetime
from django.http import HttpResponse
from github import Github
import os
import pandas as pd
import io



def post_list(request):
    posts = Post.objects.filter(published_date__isnull=False).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
def test_list(request):
    tests = Test.objects.filter(published_date__isnull=False).order_by('published_date')
    return render(request, 'blog/test_list.html', {'tests': tests})

def crud(request):
    
    tests = Test.objects.all()
    form = TestModelForm()
    
    if request.method == "POST":
        form = TestModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/index1")
                            
    context = {
        'tests': tests,
        'form': form
    }
    return render(request, 'blog/crud.html', context)

def update(request, pk):
    test = Test.objects.get(test_id=pk)
    form = TestModelForm(instance=test)

    if request.method == 'POST':
        print('save ok0')
        form = TestModelForm(request.POST, instance=test)
        if form.is_valid():
            print('save ok1')
            form.save()
            print('save ok2')
        return redirect('/index1')
        #return redirect('https://jefftestapp.herokuapp.com/index1')
    context = {
        'form': form
    }

    print('save ok3')
    return render(request, 'blog/update.html', context)

def delete(request, pk):
    test = Test.objects.get(test_id=pk)

    if request.method == "POST":
        test.delete()
        return redirect('/index1')
    context = {
        'test': test
    }
    return render(request, 'blog/delete.html', context)    
def getStock(request):

    #tw_stock_share_distribution("20210226","d:\\test\\stock_index_list_8.csv", "d:\\test\\download_8.csv", 49)
    github = Github('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')
    repository = github.get_user().get_repo('Python_RD_Git')   
    download_8_filename = 'files/download_8.csv'
    download_8_file = repository.get_contents(download_8_filename)
    d8_file=download_8_file.decoded_content.decode()
    print("down8_file:",d8_file)
    stock_index_filename = 'files/stock_index_list_8.csv'
    stock_index_file = repository.get_contents(stock_index_filename)
    st_index_file=stock_index_file.decoded_content.decode()
    print("stock_index_file",st_index_file)
    tw_stock_share_distribution1("20210226",st_index_file, d8_file, 49)
    return render(request, 'hello_world.html', {
        'current_time': str(datetime.now()),
    }) 



def getStockOwnerDetails1(request):
     github = Github('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')
     repository = github.get_user().get_repo('Python_RD_Git') 
     #context          = {}
     filename = 'files/download_8.csv'
     file = repository.get_contents(filename)
     data=file.decoded_content.decode()
     nmlist = ['資料日期', '證券代號', '持股分級', '持股數量分級', '人數', '股數', '占集保庫存數比例%']
     df = pd.read_csv(io.StringIO(data),names=nmlist)
     
     st_own_lists=df.values.tolist()
     context={"st_own_lists" : []} 
     for st_own_list in st_own_lists :
         context["st_own_lists"].append(st_own_list)
     print("st_lists:",st_own_lists)
     return render(request, 'blog/st_ow_details1.html',context)

def getStockOwnerDetails(request):        
        context={"st_own_lists" : []} 
        with open("d:\\test\\download_8.csv", "r", newline="") as fr:
            st_own_lists = csv.reader(fr,delimiter=',')  
         
            for st_own_list in st_own_lists :
                context["st_own_lists"].append(st_own_list)
                #context["st_own_lists"].append(" ".join(st_own_list))
             
        return  render(request, 'blog/st_ow_details.html',context )
    
def tw_stock_share_distribution(query_date,stock_index_list,download_summary,select_date_index):
    """query_date:爬取的日期
        stock_index_list:股票清單
        download_summary:下載存入的檔案
        select_date_index:選擇日期index,每週會不同."""

    # 將股票代碼讀成list
    stock_lists = []
    with open(stock_index_list, "r", newline="") as fr:
        stock_indexs = csv.reader(fr)
        for stock_index in stock_indexs:
            stock_lists.extend(stock_index)

    # 寫入集保分散表資料 stock_index_list_0.csv-->download_0.csv，stock_index_list_1.csv-->download_1
    # stock_index_list_2.csv-->download_2.csv.....
    with open(download_summary, "w", newline="") as fw:
        fwt = csv.writer(fw)

        # 寫入標提列
        fwt.writerow(["資料日期", "證券代號", "持股分級", "持股數量分級", "人數", "股數", "占集保庫存數比例%"])
        
       # chrome網站設定成隱藏模式.
        # 設定selenime driver chrome所需的driver 路徑
        chrome_driver_path = r"D:\test\chromedriver_win32\chromedriver.exe"
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')  # 啟動隱藏模式
        chrome_options.add_argument('--disable-gpu')  # windowsd必須加入此行 原文網址：https://itw01.com/FYB2UED.html
        
        browser = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)
        url = r"https://www.tdcc.com.tw/portal/zh/smWeb/qryStock"

        # 到指定網頁,選擇下載選項
        browser.get(url)
        time.sleep(2)


        for stock_list in stock_lists:  # 下載stock_index_list的股票
             # %%股權分散表位置
            stock_index = stock_list

            # 設定開啟網頁之日期
            select_1 = Select(browser.find_element_by_name("scaDate"))
            select_1.select_by_index(select_date_index)  # 選定輸入的日期index
            time.sleep(1)

            # 輸入股票代碼
            browser.find_element_by_id("StockNo").clear()
            browser.find_element_by_id("StockNo").send_keys(stock_index)
            time.sleep(1)

            # 送出查詢
            browser.find_element_by_xpath("//tr[4]//td[1]//input[1]").click()
            time.sleep(1)

            # 取得網頁原始碼
            html_file = browser.page_source

            # 傳入html filＥ
            # 建立beautifulSoup 解析文件
            bsobj_1 = bs(html_file, "lxml")

           # 找出回傳之分散表
            tbody_trs = bsobj_1.find("table", class_="table").find("tbody").find_all("tr")

           # 每個股票的股權分散表的處理
            for tr in tbody_trs:
                tds = tr.find_all("td")

                temp_list = []
                for td in tds:
                    temp_list.append(td.text)
                temp_list.insert(0, query_date)
                temp_list.insert(1, stock_index)
                fwt.writerow(temp_list)

            # random sleep3~15秒
            random_sleep = random.randint(3, 15)
            print(stock_index)
            time.sleep(random_sleep)

def tw_stock_share_distribution1(query_date,stock_index_list,download_summary,select_date_index):
    """query_date:爬取的日期
        stock_index_list:股票清單
        download_summary:下載存入的檔案
        select_date_index:選擇日期index,每週會不同."""

    # 將股票代碼讀成list
    stock_lists = []
    with open(stock_index_list, "r", newline="") as fr:
        stock_indexs = csv.reader(fr)
        for stock_index in stock_indexs:
            stock_lists.extend(stock_index)

    # 寫入集保分散表資料 stock_index_list_0.csv-->download_0.csv，stock_index_list_1.csv-->download_1
    # stock_index_list_2.csv-->download_2.csv.....
    with open(download_summary, "w", newline="") as fw:
        fwt = csv.writer(fw)

        # 寫入標提列
        fwt.writerow(["資料日期", "證券代號", "持股分級", "持股數量分級", "人數", "股數", "占集保庫存數比例%"])
        
       # chrome網站設定成隱藏模式.
        # 設定selenime driver chrome所需的driver 路徑
        #heroku cloud path
        GOOGLE_CHROME_PATH = '/app/.apt/usr/bin/google_chrome'
        CHROMEDRIVER_PATH = '/app/.chromedriver/bin/chromedriver'
        ##########3
        #chrome_driver_path = r"D:\test\chromedriver_win32\chromedriver.exe"
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')  # 啟動隱藏模式
        chrome_options.add_argument('--disable-gpu')  # windowsd必須加入此行 原文網址：https://itw01.com/FYB2UED.html
        browser = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)

        browser.get("https://www.tdcc.com.tw/portal/zh/smWeb/qryStock")
        
        
        #browser = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, options=chrome_options)
        #url = r"https://www.tdcc.com.tw/portal/zh/smWeb/qryStock"

        # 到指定網頁,選擇下載選項
        #browser.get(url)
        time.sleep(2)


        for stock_list in stock_lists:  # 下載stock_index_list的股票
             # %%股權分散表位置
            stock_index = stock_list

            # 設定開啟網頁之日期
            select_1 = Select(browser.find_element_by_name("scaDate"))
            select_1.select_by_index(select_date_index)  # 選定輸入的日期index
            time.sleep(1)

            # 輸入股票代碼
            browser.find_element_by_id("StockNo").clear()
            browser.find_element_by_id("StockNo").send_keys(stock_index)
            time.sleep(1)

            # 送出查詢
            browser.find_element_by_xpath("//tr[4]//td[1]//input[1]").click()
            time.sleep(1)

            # 取得網頁原始碼
            html_file = browser.page_source

            # 傳入html filＥ
            # 建立beautifulSoup 解析文件
            bsobj_1 = bs(html_file, "lxml")

           # 找出回傳之分散表
            tbody_trs = bsobj_1.find("table", class_="table").find("tbody").find_all("tr")

           # 每個股票的股權分散表的處理
            for tr in tbody_trs:
                tds = tr.find_all("td")

                temp_list = []
                for td in tds:
                    temp_list.append(td.text)
                temp_list.insert(0, query_date)
                temp_list.insert(1, stock_index)
                fwt.writerow(temp_list)

            # random sleep3~15秒
            random_sleep = random.randint(3, 15)
            print(stock_index)
            time.sleep(random_sleep)

def hello_world1(request):
    return render(request, 'hello_world1.html', {
        'current_time': str(datetime.now()),
    })           