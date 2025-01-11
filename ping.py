import requests
import time


def check_connection(api_key, methods):
    '''Функция для проверки доступности WB API 
    по полученному ключи из app.py -> API_KEY'''
    print("Проверка доступности API-ключа к WB API:\n")
    access_list=[]
    for method in methods:
        try:
            headers={"Authorization":api_key}
            response=requests.get(url=method+"ping", headers=headers, timeout=5)
            if (response.status_code == 200):
                print(f"Вам доступны методы из раздела <{methods[method]}>,", "ссылка на методы:",method)
                access_list.append(method)
        except requests.exceptions.ReadTimeout:
            print("Возникла ошибка! Есть несколько причин:\n\
                1. Вы неправильно ввели ключ доступа к API\n\
                2. Wildberries на данный момент недоступен, попробуйте перейти на https://www.wildberries.ru/ и убедиться в этом.\n\
                    Пробуем повторное подключение...\n")
    return access_list