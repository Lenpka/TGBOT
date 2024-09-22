from testtables import get_table_by_url, service_account,  extract_data_from_sheet, test_get_data

table_link_schedule = 'https://docs.google.com/spreadsheets/d/1UZKFIVril9zME7EOiHIsjHyeVB0P94OAUlLPINjne3A/edit?gid=153533360#gid=153533360'
def schedule_test_get_data() -> None:
    """Принимает расписание"""
    client = service_account(filename='/home/darowa/Documents/TGBOT/tbgot-436304-9178e9d66479.json')
    tables = get_table_by_url(client, table_link_schedule)
    data = extract_data_from_sheet(tables, "1 бак.")
    for dat in data:
        print(dat)
if __name__ == "__main__":
    schedule_test_get_data()