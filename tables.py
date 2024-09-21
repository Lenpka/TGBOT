import gspread
from random import shuffle
from datetime import datetime
from configys import CREDENTIALS_FILENAME

# создадим класс, который будет отображением нашей таблицы в Python:
class Quizzer:
    #создаём необходимые поля класса:
    def __init__(self,student_url = "https://docs.google.com/spreadsheets/d/1Xpfs6p6yzCxH4RUm-hFX4csd7AH5-4N8OwwXTc1Db4Q/edit?gid=0#gid=0") -> None:
        self.account = gspread.service_account(filename=CREDENTIALS_FILENAME)
        self.spreadheet - self.account.open_by_url(student_url)
        self.students = {
            elem.title: elem.id for elem in self.spreadsheet.worksheets()
        }
        self.raiting = self.spreadheet.get_worksheet_by_id(self.topics.get("Raiting"))
    def get_list_of_students(self) -> dict:
        return {key: value for key, value in self.topics.items() if key != "Raiting"}
    def get_raiting_by_student(self, student_name) -> list:
        if student_name in self.students:
            worksheet = self.spreadsheet.get_worksheet_by_id(self.students.get(student_name))
            return worksheet.get_all_records()
        return []
    def students_and_raitings(self, student_name):
        students = self.get_list_of_students(student_name)
        result = []
        for elem in students:
            raitings = [elem["%ИТОГ"],elem["%КР"], elem["%ТЕК"], elem["СУМ"]]
            shuffle(raitings)
            new_format = {
            "СТУДЕНТ" :  elem["СТУДЕНТ"],
            "МАКС" : elem["МАКС"],
            "СУМ" : elem["СУМ"]
            }
            result.append(new_format)
        return result
    def write_raiting_to_result_cell(self, user_id, students, raiting, max_value):
        index = len(list(filter(None, self.raitings.col_values(1)))) + 1
        self.raitings.update(f"C{index}:H{index}", [[
            user_id, students,raiting,max_value,f"{datetime.now()}"
        ]])