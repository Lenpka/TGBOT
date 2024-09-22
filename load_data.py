from testtables import get_table_by_url, client_init_json
from gspread import spreadsheet
homework = "https://docs.google.com/spreadsheets/d/1GDyS3jw3tPuYKNxmjaSxGjQoRG2MqOOVpZRttTE7nnA/edit?gid=153533360#gid=153533360"
def insert_one(table:spreadsheet, title:str, data:list, index:int = 1):
    """Вставка данных в лист"""
    worksheet = table.Worksheet(title)
    worksheet.insert_row(data, index=index)

def test_data_load():
    client = client_init_json()
    table= get_table_by_url(client, homework)
    worksheet_info = get_worksheet_info(table)
    print('Информация по домашкам: ', worksheet_info)
    insert_one (table=table,
               title = worksheet_info['Домашнее задание'],
               data = [])
    return insert_one


def add_data_to_worksheet_var_2(table: Spreadsheet, title: str, data: List[Dict], start_row: int = 2) -> None:
    """
    Добавляет данные на рабочий лист в Google Sheets.

    :param table: Объект таблицы (Spreadsheet).
    :param title: Название рабочего листа.
    :param data: Список словарей с данными.
    :param start_row: Номер строки, с которой начнется добавление данных.
    """
    try:
        worksheet = table.worksheet(title)
    except exceptions.WorksheetNotFound:
        worksheet = create_worksheet(table, title, rows=100, cols=20)

    headers = data[0].keys()
    end_row = start_row + len(data) - 1
    end_col = chr(ord('A') + len(headers) - 1)

    cell_range = f'A{start_row}:{end_col}{end_row}'
    cell_list = worksheet.range(cell_range)

    flat_data = []
    for row in data:
        for header in headers:
            flat_data.append(row[header])

    for i, cell in enumerate(cell_list):
        cell.value = flat_data[i]

    worksheet.update_cells(cell_list)