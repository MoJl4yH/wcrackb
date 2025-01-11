import requests
from save_data import *

'''В этом файле приведены все методы из https://seller-analytics-api.wildberries.ru/'''

seller_analytics_url="https://seller-analytics-api.wildberries.ru/"
name_api="seller-analytics"

METHODS_FROM_ANALYTICS={"api/v2/nm-report/detail":"Получение статистики КТ за выбранный период, по nmID/предметам/брендам/ярлыкам",
              #"api/v2/nm-report/grouped":"Получение статистики КТ за период, сгруппированный по предметам, брендам и ярлыкам",
              "api/v2/nm-report/detail/history":"Получение статистики КТ по дням по выбранным nmID",
              "api/v2/nm-report/grouped/history":"Получение статистики КТ по дням за период, сгруппированный по предметам, брендам и ярлыкам",
              "api/v2/search-report/report":"Основная страница",
              "api/v2/search-report/table/groups":"Пагинация по группам",
              "api/v2/search-report/table/details":"Пагинация по товарам в группе",
              "api/v2/search-report/product/search-texts":"Поисковые запросы по товару",
              "api/v2/search-report/product/orders":"Заказы и позиции по поисковым запросам товара",
              "api/v1/analytics/excise-report":"Отчёт по товарам с обязательной маркировкой",
              "api/v1/analytics/acceptance-report":"Получить отчёт за платную приемку",
              "api/v1/analytics/antifraud-details":"Отчёты по удержаниям - Самовыкупы",
              "api/v1/analytics/incorrect-attachments":"Отчёты по удержаниям - Подмена товара",
              "api/v1/analytics/storage-coefficient":"Отчёты по удержаниям - Коэффициент логистики и хранения",
              "api/v1/analytics/goods-labeling":"Отчёты по удержаниям - Маркировка товара",
              "api/v1/analytics/characteristics-change":"Смена характеристик - Возвраты покупателями",
              "api/v1/analytics/region-sale":"Продажи по регионам",
              "api/v1/analytics/brand-share/brands":"Бренды продавца",
              "api/v1/analytics/brand-share/parent-subjects":"Родительские категории бренда",
              "api/v1/analytics/brand-share":"Получить отчёт по доле бренда в продажах",
              "api/v1/analytics/banned-products/blocked":"Заблокированные карточки",
              "api/v1/analytics/banned-products/shadowed":"Скрытые из каталога",
              "api/v1/analytics/goods-return":"Получить отчёт по возвратам товаров"}




'''Получение статистики КТ за выбранный период, 
по nmID/предметам/брендам/ярлыкам'''
def transformation_data_nm_report_detail(api_key):
    print("Работа с методом \"Получение статистики КТ за выбранный период, по nmID/предметам/брендам/ярлыкам\"")
    name_method="api/v2/nm-report/detail"
    begin_date = input("Укажите период начала для получения статистики в формате <YYYY-MM-DD 00:00:00>: ") # дата начала отчета
    end_date = input("Укажите период окончания получения статистики в формате <YYYY-MM-DD 00:00:00>: ") # дата окончания отчета
    headers={"Authorization":api_key,"Content-Type":"application/json"} # заголовок для запроса к методу 
    payload={"timezone":"Europe/Moscow","period":{"begin":begin_date,"end":end_date},"page":1} # данные для запроса к методу
    response=requests.post(url=seller_analytics_url+name_method, headers=headers, json=payload, timeout=3) # в response хранятся данные полученные от метода
    data = save_to_json(response, name_api, name_method.replace("/","-"))
    cards = data['data']['cards']  # data -> cards
    processed_data = [] # преобразование списка cards
    for card in cards:
        card_data = {
            "Артикул WB": card.get("nmID"),
            "Артикул продавца": card.get("vendorCode"),
            "Название бренда": card.get("brandName"),
            #"ID ярлыка": card["tags"].get("id"),
            #"Название ярлыка": card["tags"].get("name"),
            "ID предмета": card["object"].get("id"),
            "Название предмета": card["object"].get("name"),
            "Остатки МП, шт.": card["stocks"].get("stocksMp"),
            "Остатки на складах WB": card["stocks"].get("stocksWb"),
        }
        
        stats = card["statistics"]["selectedPeriod"] # добавляем данные из cards -> statistics -> selectedPeriod
        card_data.update({
            "Начало периода": stats.get("begin"),
            "Конец периода": stats.get("end"),
            "Количество переходов в карточку товара": stats.get("openCardCount"),
            "Положили в корзину, штук": stats.get("addToCartCount"),
            "Заказали товаров, шт": stats.get("ordersCount"),
            "Заказали на сумму, руб.": stats.get("ordersSumRub"),
            "Выкупили товаров, шт.": stats.get("buyoutsCount"),
            "Выкупили на сумму, руб.": stats.get("buyoutsSumRub"),
            "Отменили товаров, шт.": stats.get("cancelCount"),
            "Отменили на сумму, руб.": stats.get("cancelSumRub"),
            "Средняя цена, руб.": stats.get("avgPriceRub"),
            "Среднее количество заказов в день, ш": stats.get("avgOrdersCountPerDay"),
        })

        # Добавляем данные из cards -> statistics -> selectedPeriod -> conversions
        conversions = stats.get("conversions", {})
        card_data.update({
            "Конверсия в корзину, %": conversions.get("addToCartPercent"),
            "Конверсия в заказ, %": conversions.get("cartToOrderPercent"),
            "Процент выкупа, %": conversions.get("buyoutsPercent"),
        })
        
        processed_data.append(card_data)
    save_json_to_xlsl(processed_data, name_api, name_method.replace("/","-"))
    
    
'''Получение статистики КТ по дням по выбранным nmID'''
def transformation_data_nm_report_detail_history(api_key):
    print("Работа с методом \"Получение статистики КТ по дням по выбранным nmID\"")
    name_method="api/v2/nm-report/detail/history"
    begin_date = input("Укажите период начала для получения статистики в формате <YYYY-MM-DD> (но не более 7 дней): ") # дата начала отчета
    end_date = input("Укажите период окончания получения статистики в формате <YYYY-MM-DD> (но не более 7 дней): ") # дата окончания отчета
    nmIDs_input=input("Укажите артикул(ы) WB по которому нужно получить статистику. Если хотите указать несколько, то указывайте в следующем формате 12345678,12345678,...,... (не более 20): ")
    nmIDs = [int(nm.strip()) for nm in nmIDs_input.split(',') if nm.strip().isdigit()] # преобразование введеных данных в список чисел
    headers={"Authorization":api_key,"Content-Type":"application/json"} # заголовок для запроса к методу 
    payload={"period":{"begin":begin_date,"end":end_date},"nmIDs":nmIDs} # данные для запроса к методу
    response=requests.post(url=seller_analytics_url+name_method, headers=headers, json=payload, timeout=3) # в response хранятся данные полученные от метода
    data = save_to_json(response, name_api, name_method.replace("/","-"))
    # Проверяем, есть ли данные
    items = data.get("data", [])

    # Преобразование данных в плоскую структуру
    processed_data = []
    for item in items:
        nmID = item.get("nmID")
        imtName = item.get("imtName")
        vendorCode = item.get("vendorCode")
        
        for history_entry in item.get("history", []):
            # Объединяем основные данные с историей
            entry_data = {
                "Артикул WB": nmID,
                "Наименование КТ": imtName,
                "Артикул продавца": vendorCode,
                "Дата": history_entry.get("dt"),
                "Количество переходов в карточку товара": history_entry.get("openCardCount"),
                "Положили в корзину, штук": history_entry.get("addToCartCount"),
                "Конверсия в корзину, %": history_entry.get("addToCartConversion"),
                "Заказали товаров, шт": history_entry.get("ordersCount"),
                "Заказали на сумму, руб.": history_entry.get("ordersSumRub"),
                "Конверсия в заказ, %": history_entry.get("cartToOrderConversion"),
                "Выкупили товаров, шт.": history_entry.get("buyoutsCount"),
                "Выкупили на сумму, руб.": history_entry.get("buyoutsSumRub"),
                "Процент выкупа, %": history_entry.get("buyoutPercent"),
            }
            processed_data.append(entry_data)
        save_json_to_xlsl(processed_data, name_api, name_method.replace("/","-"))