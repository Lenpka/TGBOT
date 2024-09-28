
from testtables import *
from collections import defaultdict
# Весь этот модуль стоит вынести в отдельный каталог

table_link_raiting = 'https://docs.google.com/spreadsheets/d/1Xpfs6p6yzCxH4RUm-hFX4csd7AH5-4N8OwwXTc1Db4Q/edit?gid=0#gid=0'

def raiting_test_get_data() -> dict:
    """Принимает рейтинг"""
    # todo - read variables from env
    client = service_account(filename='./tgbot.json')
    tables = get_table_by_url(client, table_link_raiting)
    data = extract_data_from_sheet(tables, "Рейтинг")
    homeworks = defaultdict()

    return data

if __name__ == "__main__":
    print(raiting_test_get_data())
