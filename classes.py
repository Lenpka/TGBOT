from main import bot, dp
class Lesson(object):
    def __init__(self, name:str, time:str, teacher:str, place:str):
        self.name = name
        self.time = time
        self.teacher = teacher
        self.place = place
English = Lesson("English", "10:45-12:20", "Хотянова Ольга Борисовна или Пояркова Александра Викторовна", "209 или 229")
Seminar_Chemistry = Lesson("Seminar_Chemistry", "12:30 - 14:05","Берекчиян М.В., Брылѐв О.А., Харченко А.В.", "ауд. 210, 215, 229" )
Lunch = Lesson("Lunch", "14:05 - 15:10")
Practice = Lesson("Practice","15:10 - 18:25", "Берекчиян М.В., Брылѐв О.А., Лунѐв А.М., Харченко А.В.", "Химический факультет")