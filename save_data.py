import pandas
import json
import os


def save_to_json(response, name_api, name_method):
    if os.path.exists(f"temporary/{name_api}"):
        if os.path.isfile(f"temporary/{name_api}/{name_method}.json"):
            os.remove(f"temporary/{name_api}/{name_method}.json")
    else:
        os.makedirs(f"temporary/{name_api}")
    with open(f"temporary/{name_api}/{name_method}.json", "w") as file:
        json.dump(response.json(), file)
    data=pandas.read_json(f"temporary/{name_api}/{name_method}.json")
    return data

    

def save_json_to_xlsl(data, name_api, name_method, rename_columns=None):
    if os.path.exists(f"report/{name_api}"):
        if os.path.isfile(f"report/{name_api}/{name_method}.xlsx"):
            os.remove(f"report/{name_api}/{name_method}.xlsx")
    else:
        os.makedirs(f"report/{name_api}")
    excel_file=f"report/{name_api}/{name_method}.xlsx"
    data_to_excel = pandas.DataFrame(data)
    if rename_columns:
        data_to_excel=data_to_excel.rename(columns=rename_columns)
    data_to_excel.to_excel(excel_file, index=False)
    if os.path.exists(f"report/{name_api}/{name_method}.xlsx"):
        print(f"Отчет по выбранному методу создан по пути - report/{name_api}/{name_method}.xlsx"+"\n")