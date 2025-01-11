import json
import requests
import pandas
from ping import check_connection
from seller_analytics import *
from statistics_wb import *
import sys

'''----------------------------------------------------------------------------------------------------------------'''

# Методы в соответствии со спецификацией приведенной на 
# https://openapi.wildberries.ru/ на 08.12.2024
METHODS_FROM_API={"https://common-api.wildberries.ru/":"Тарифы, Новости", # 1
              "https://content-api.wildberries.ru/":"Контент № 1", # 2
              "https://content-api-sandbox.wildberries.ru/":"Контент № 2", # 3
              "https://seller-analytics-api.wildberries.ru/":"Аналитика", # 4
              "https://discounts-prices-api.wildberries.ru/":"Цены и скидки № 1", # 5
              "https://discounts-prices-api-sandbox.wildberries.ru/":"Цены и скидки № 2", # 6
              "https://marketplace-api.wildberries.ru/":"Маркетплейс", # 7
              "https://statistics-api.wildberries.ru/":"Статистика № 1", # 8
              "https://statistics-api-sandbox.wildberries.ru/":"Статистика № 2", # 9
              "https://advert-api.wildberries.ru/":"Продвижение № 1", # 10
              "https://advert-api-sandbox.wildberries.ru/":"Продвижение № 2", # 11
              "https://feedbacks-api.wildberries.ru/":"Вопросы и отзывы № 1", # 12
              "https://feedbacks-api-sandbox.wildberries.ru/":"Вопросы и отзывы № 2", # 13
              "https://buyer-chat-api.wildberries.ru/":"Чат с покупателями", # 14
              "https://supplies-api.wildberries.ru/":"Поставки", # 15
              "https://returns-api.wildberries.ru/":"Возвраты покупателями", # 16
              "https://documents-api.wildberries.ru/":"Документы"} # 17

# Описание, которое выдается на старте работы скрипта.
ascii_art="""

██╗    ██╗ ██████╗██████╗  █████╗  ██████╗██╗  ██╗██████╗ 
██║    ██║██╔════╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██╔══██╗
██║ █╗ ██║██║     ██████╔╝███████║██║     █████╔╝ ██████╔╝
██║███╗██║██║     ██╔══██╗██╔══██║██║     ██╔═██╗ ██╔══██╗
╚███╔███╔╝╚██████╗██║  ██║██║  ██║╚██████╗██║  ██╗██████╔╝
 ╚══╝╚══╝  ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═════╝ 
                                                          
"""
                                                                                                    
print(ascii_art)
print("Приложение для формирования таблицы xlsl из данных wildberries магазина...\n")

# Переменная для ввода API-ключа для доступа к WB API 
# и проверка доступа ко всем методам
API_KEY=input("Введите API-ключ для подключения к магазину:\n\
>>> ")
access_list_api=check_connection(API_KEY,METHODS_FROM_API)
if not bool(access_list_api):
    print("Похоже у вас нет доступа к необходимому API, проверьте правильность ввода или же уточните, выдали ли вам необходимый доступ.")
    sys.exit(1)
'''----------------------------------------------------------------------------------------------------------------'''

print("\nВыберите какой вид отчета вы хотите получить, для выхода из программы нажмите 0\n")
for access_api in access_list_api:
    key_list=list(METHODS_FROM_API.keys())
    index = key_list.index(access_api)
    print("Для получения отчета по", access_api,f"(раздел {METHODS_FROM_API[access_api]})", "выберете -", index+1)

while(enumerate!=0):
    enumerate=int(input(">>> "))
    if (enumerate==1):
        print("На данный момент не реализовано")
    elif(enumerate==2):
        print("На данный момент не реализовано")
    elif(enumerate==3):
        print("На данный момент не реализовано")
    elif(enumerate==4):
        transformation_data_nm_report_detail(API_KEY)
        transformation_data_nm_report_detail_history(API_KEY)
    elif(enumerate==5):
        print("На данный момент не реализовано")
    elif(enumerate==6):
        print("На данный момент не реализовано")
    elif(enumerate==7):
        print("На данный момент не реализовано")
    elif(enumerate==8):
        transformation_data_supplier_incomes(API_KEY)
        transformation_data_supplier_sales(API_KEY)
        transformation_data_supplier_reportDetailByPeriod(API_KEY)
    elif(enumerate==9):
        print("На данный момент не реализовано")
    elif(enumerate==10):
        print("На данный момент не реализовано")
    elif(enumerate==11):
        print("На данный момент не реализовано")
    elif(enumerate==12):
        print("На данный момент не реализовано")
    elif(enumerate==13):
        print("На данный момент не реализовано")
    elif(enumerate==14):
        print("На данный момент не реализовано")
    elif(enumerate==15):
        print("На данный момент не реализовано")
    elif(enumerate==16):
        print("На данный момент не реализовано")
    elif(enumerate==17):
        print("На данный момент не реализовано")
    elif(enumerate==0):
        print("Работа завершена, если все успешно, ваши данные находятся в директории report.")
        break
    for access_api in access_list_api:
        key_list=list(METHODS_FROM_API.keys())
        index = key_list.index(access_api)
        print("Вы вернулись в основное меню, для получения отчета по", access_api,f"(раздел {METHODS_FROM_API[access_api]})", "выберете -", index+1, "\n")
    print("Для выхода из программы введите 0")
