import requests
from save_data import *

'''В этом файле приведены все методы из https://statistics-api.wildberries.ru/'''

seller_analytics_url="https://statistics-api.wildberries.ru/"
name_api="statistics"


METHODS_FROM_STATISTICS={"api/v1/supplier/incomes":"Статистика - Поставки",
              "api/v1/supplier/stocks":"Статистика - Склад",
              "api/v1/supplier/orders":"Статистика - Заказы",
              "api/v1/supplier/sales":"Статистика - Продажи",
              "api/v5/supplier/reportDetailByPeriod":"Статистика - Отчет о продажах по реализации"}


'''Статистика - Поставки'''
def transformation_data_supplier_incomes(api_key):
    print("Работа с методом \"Статистика по поставкам\"")
    name_method="api/v1/supplier/incomes"
    dateFrom=input("Укажите дату и время последнего изменения по поставке <YYYY-MM-DD 00:00:00>: ") # дата последнего изменения
    headers={"Authorization":api_key,"Content-Type":"application/json"} # заголовок для запроса к методу 
    response=requests.get(url=seller_analytics_url+name_method+f"?dateFrom={dateFrom}", headers=headers, timeout=60) # в response хранятся данные полученные от метода
    data = save_to_json(response, name_api, name_method.replace("/","-"))
    rename_columns={
        "incomeId":"Номер поставки",
        "number":"Номер УПД",
        "date":"Дата поступления.",
        "lastChangeDate":"Дата и время обновления информации в сервисе",
        "supplierArticle":"Артикул продавца",
        "techSize":"Размер товара (пример S, M, L, XL, 42, 42-43)",
        "barcode":"Бар-код",
        "quantity":"Количество",
        "totalPrice":"Цена из УПД",
        "dateClose":"Дата принятия (закрытия) в WB",
        "warehouseName":"Название склада",
        "nmId":"Артикул WB",
        "status":"Текущий статус поставки"
    }
    save_json_to_xlsl(data, name_api, name_method.replace("/","-"), rename_columns)
    
'''Статистика - Склад'''
def transformation_data_supplier_stocks(api_key):
    print('wait')
    
'''Статистика - Заказы'''
def transformation_data_supplier_orders(api_key):
    print('wait')


'''Статистика - Продажи'''
def transformation_data_supplier_sales(api_key):
    print("Работа с методом \"Статистика по продажам\"")
    name_method="api/v1/supplier/sales"
    dateFrom=input("Укажите дату и время последнего изменения по продаже <YYYY-MM-DD 00:00:00>: ") # дата последнего изменения
    headers={"Authorization":api_key,"Content-Type":"application/json"} # заголовок для запроса к методу 
    response=requests.get(url=seller_analytics_url+name_method+f"?dateFrom={dateFrom}", headers=headers, timeout=60) # в response хранятся данные полученные от метода
    data = save_to_json(response, name_api, name_method.replace("/","-"))
    rename_columns={
        "date":"Дата и время продажи",
        "lastChangeDate":"Дата и время обновления информации в сервисе",
        "warehouseType":"Склад отгрузки",
        "countryName":"Страна",
        "oblastOkrugName":"Округ",
        "regionName":"Регион",
        "supplierArticle":"Артикул продавца",
        "nmId":"Артикул WB",
        "barcode":"Баркод",
        "category":"Категория",
        "subject":"Предмет",
        "brand":"Бренд",
        "techSize":"Размер товара",
        "incomeID":"Номер поставки",
        "isSupply":"Договор поставки",
        "isRealization":"Договор реализации",
        "totalPrice":"Цена без скидок",
        "discountPercent":"Скидка продавца",
        "spp":"Скидка WB",
        "paymentSaleAmount":"Оплачено с WB Кошелька",
        "forPay":"К перечислению продавцу",
        "finishedPrice":"Фактическая цена с учетом всех скидок",
        "priceWithDisc":"Цена со скидкой продавца",
        "saleID":"Уникальный идентификатор продажи/возврата",
        "orderType":"Тип заказа",
        "sticker":"Идентификатор стикера",
        "gNumber":"Номер заказа",
        "srid":"Уникальный идентификатор заказа."
    }
    save_json_to_xlsl(data, name_api, name_method.replace("/","-"), rename_columns)
    
def transformation_data_supplier_reportDetailByPeriod(api_key):
    print("Работа с методом \"Отчет о продажах по реализации\"")
    name_method="api/v5/supplier/reportDetailByPeriod"
    dateFrom=input("Укажите дату и время последнего изменения по продажам по реализации <YYYY-MM-DD 00:00:00>: ") # дата последнего изменения
    dateTo=input("Укажите конечную дату отсчета по продажам по реализации") # дата отсчета
    headers={"Authorization":api_key,"Content-Type":"application/json"} # заголовок для запроса к методу 
    response=requests.get(url=seller_analytics_url+name_method+f"?dateFrom={dateFrom}&dateTo={dateTo}", headers=headers, timeout=60) # в response хранятся данные полученные от метода
    data = save_to_json(response, name_api, name_method.replace("/","-"))
    rename_columns = {
        "realizationreport_id": "Номер отчёта",
        "date_from": "Дата начала отчётного периода",
        "date_to": "Дата конца отчётного периода",
        "create_dt": "Дата формирования отчёта",
        "currency_name": "Валюта отчёта",
        "suppliercontract_code": "Договор",
        "rrd_id": "Номер строки",
        "gi_id": "Номер поставки",
        "subject_name": "Предмет",
        "nm_id": "Артикул WB",
        "brand_name": "Бренд",
        "sa_name": "Артикул продавца",
        "ts_name": "Размер",
        "barcode": "Баркод",
        "doc_type_name": "Тип документа",
        "quantity": "Количество",
        "retail_price": "Цена розничная",
        "retail_amount": "Сумма продаж (возвратов)",
        "sale_percent": "Согласованная скидка",
        "commission_percent": "Процент комиссии",
        "office_name": "Склад",
        "supplier_oper_name": "Обоснование для оплаты",
        "order_dt": "Дата заказа",
        "sale_dt": "Дата продажи",
        "rr_dt": "Дата операции",
        "shk_id": "Штрих-код",
        "retail_price_withdisc_rub": "Цена розничная с учетом согласованной скидки",
        "delivery_amount": "Количество доставок",
        "return_amount": "Количество возвратов",
        "delivery_rub": "Стоимость логистики",
        "gi_box_type_name": "Тип коробов",
        "product_discount_for_report": "Согласованный продуктовый дисконт",
        "supplier_promo": "Промокод",
        "rid": "Уникальный идентификатор заказа",
        "ppvz_spp_prc": "Скидка постоянного покупателя",
        "ppvz_kvw_prc_base": "Размер кВВ без НДС, % базовый",
        "ppvz_kvw_prc": "Итоговый кВВ без НДС, %",
        "sup_rating_prc_up": "Размер снижения кВВ из-за рейтинга",
        "is_kgvp_v2": "Размер снижения кВВ из-за акции",
        "ppvz_sales_commission": "Вознаграждение с продаж до вычета услуг поверенного, без НДС",
        "ppvz_for_pay": "К перечислению продавцу за реализованный товар",
        "ppvz_reward": "Возмещение за выдачу и возврат товаров на ПВЗ",
        "acquiring_fee": "Возмещение издержек по эквайрингу",
        "acquiring_percent": "Размер комиссии за эквайринг без НДС, %",
        "acquiring_bank": "Наименование банка-эквайера",
        "ppvz_vw": "Вознаграждение WB без НДС",
        "ppvz_vw_nds": "НДС с вознаграждения WB",
        "ppvz_office_id": "Номер офиса",
        "ppvz_office_name": "Наименование офиса доставки",
        "ppvz_supplier_id": "Номер партнера",
        "ppvz_supplier_name": "Партнер",
        "ppvz_inn": "ИНН партнера",
        "declaration_number": "Номер таможенной декларации",
        "bonus_type_name": "Обоснование штрафов и доплат",
        "sticker_id": "Цифровое значение стикера",
        "site_country": "Страна продажи",
        "penalty": "Штрафы",
        "additional_payment": "Доплаты",
        "rebill_logistic_cost": "Возмещение издержек по перевозке",
        "rebill_logistic_org": "Организатор перевозки",
        "kiz": "Код маркировки",
        "storage_fee": "Стоимость хранения",
        "deduction": "Прочие удержания/выплаты",
        "acceptance": "Стоимость платной приёмки",
        "srid": "Уникальный идентификатор заказа",
        "report_type": "Тип отчёта"
    }
    save_json_to_xlsl(data, name_api, name_method.replace("/","-"), rename_columns)