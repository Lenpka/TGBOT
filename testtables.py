


from gspread import Client, Spreadsheet, Worksheet, service_account, exceptions
from typing import List, Dict

#from get_fake_users import get_fake_users
table_link = 'https://docs.google.com/spreadsheets/d/1Xpfs6p6yzCxH4RUm-hFX4csd7AH5-4N8OwwXTc1Db4Q/edit?gid=0#gid=0'
table_id = '1Xpfs6p6yzCxH4RUm-hFX4csd7AH5-4N8OwwXTc1Db4Q/edit?gid=0#gid=0'


def client_init_json() -> Client:
    """Создание клиента для работы с Google Sheets."""
    return service_account(filename='/home/darowa/Documents/TGBOT/tbgot-436304-9178e9d66479.json')
def get_table_by_url(client: Client, table_url):
    """Получение таблицы из Google Sheets по ссылке."""
    return client.open_by_url(table_url)

def get_worksheet_info(table:Spreadsheet) -> dict:
    """ Возращает размеры таблицы"""
    worksheets = table.worksheets()
    worksheet_info = {
        "count": len(worksheets),
        "Названия_листов": [worksheet.title for worksheet in worksheets]
    }
    return worksheet_info

def test_get_table(table_url: str):
    """Тестирование получения таблицы из Google Sheets."""
    client = client_init_json()
    table = get_table_by_url(client, table_url)
    print('Инфо по таблице по ссылке: ', table)


def main():
    client = client_init_json()
    table = get_table_by_url(client, table_link)

    info = get_worksheet_info(table)
    print(f"Листов {info['count']}")
    print("Их названия")
    for name in info['Названия_листов']:
        print(name)

def extract_data_from_sheet(table: Spreadsheet, sheet_name: str) -> List[Dict]:
    """
    Извлекает данные из указанного листа таблицы Google Sheets и возвращает список словарей.

    :param table: Объект таблицы Google Sheets (Spreadsheet).
    :param sheet_name: Название листа в таблице.
    :return: Список словарей, представляющих данные из таблицы.
    """
    worksheet = table.worksheet(sheet_name)
    rows = worksheet.get_all_records()
    return rows
def test_get_data():
    """Тестирование извлечения данных из таблицы Google Sheets."""
    client = client_init_json()
    table = get_table_by_url(client, table_link)
    data = extract_data_from_sheet(table, 'Рейтинг')
    for i in data:
        print(i)




if __name__ == '__main__':
    test_get_data()