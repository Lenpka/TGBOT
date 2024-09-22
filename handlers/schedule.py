
class Lesson(object):
    def __init__(self, name:str, time = '', teacher="", comment='', place="", task=""):
        self.name = name
        self.time = time
        self.teacher = teacher
        self.place = place
        self.comment = comment
        self.task = task
    def __str__(self) -> str:
        result = f"{self.name}  ({self.time})"
        if self.teacher:
            result += f"\nИмя преподавателя - {self.teacher}"
            result += "\n "
        if self.place:
            result += f"\nНомер аудитории - {self.place}"
            result += "\n "
        if self.comment:
            result += f"\nКомментарий - {self.comment}"
            result += "\n "
        if self.task:
            result += f"\nЗадание - {self.task}"
            result += "\n "
        return result

# TODO - Удалить
# Seminar_Chemistry = Lesson("Seminar_Chemistry", "12:30 - 14:05","Берекчиян М.В., Брылѐв О.А., Харченко А.В.", "ауд. 210, 215, 229" )
# Lunch = Lesson("Lunch", "14:05 - 15:10", "отдыхай", "но скоро пара")
# Practice_Chemistry = Lesson("Practice","15:10 - 18:25", "Берекчиян М.В., Брылѐв О.А., Лунѐв А.М., Харченко А.В.", "Химический факультет")
# # Понедельник

# English_Monday_1 = Lesson("Английский язык (I подгруппа)", "10:45 - 12:20", "Пояркова Александра Викторовна", "ауд. 229")
# English_Monday_2 = Lesson("Английский язык (II подгруппа)", "10:45 - 12:20", "Хотянова Ольга Борисовна", "ауд. 209")
# Chemistry_Seminar = Lesson("Общая химия и химия элементов (семинар)", "12:30 - 14:05", "Берекчиян М.В., Брылѐв О.А., Лунѐв А.М., Харченко А.В.", "ауд. 210, 215, 229")
# Lunch_Monday = Lesson("Обед", "14:15 - 15:10")
# Practice_Chemistry_1 = Lesson("Практикум по общей химии", "15:10 - 16:45", "Берекчиян М.В., Лунѐв А.М., Харченко А.В.", "Химический факультет")
# Practice_Chemistry_2 = Lesson("Практикум по общей химии", "15:30 - 17:05", "Берекчиян М.В., Лунѐв А.М.", "ауд. 209, 210, 229")

# # Вторник
# Math_Seminar_Tuesday = Lesson("Математический анализ (семинар)", "9:00 - 10:35", "Долгалева Ольга Евгеньевна", "ауд. 229")
# Chemistry_Lecture = Lesson("Общая химия и химия элементов (лекция)", "10:45 - 12:20", "Гудилин Е.А., Шевельков А.В.", "БХА")
# Practice_Chemistry_Tuesday = Lesson("Общая химия и химия элементов (практикум)", "12:30 - 14:25", "Берекчиян М.В., Брылѐв О.А., Лунѐв А.М., Харченко А.В.", "ауд. 210, 215, 229")
# Lunch_Tuesday = Lesson("Обед", "14:25 - 15:35")
# Chemistry_Seminar_Tuesday = Lesson("Практикум по общей химии", "15:35 - 17:05", "Берекчиян М.В., Лунѐв А.М.", "Химический факультет")

# # Среда
# Programming_1 = Lesson("Программирование и ЭВМ", "9:00 - 10:35", "Поярков Андрей Александрович", "ауд. 219")
# Programming_2 = Lesson("Программирование и ЭВМ", "10:45 - 12:20", "Поярков Андрей Александрович", "ауд. 219")
# Physical_Culture_Wednesday = Lesson("Физическая культура", "12:50 - 14:25", "Еремина Любовь Павловна")
# Lunch_Wednesday = Lesson("Обед", "14:05 - 15:00")

# # Четверг
# Math_Seminar_Thursday_1 = Lesson("Математический анализ (семинар)", "9:00 - 10:35", "Долгалева Ольга Евгеньевна", "ауд. 229")
# Math_Lecture_Thursday_2 = Lesson("Математический анализ (лекция)", "10:45 - 14:00", "Зайцева Наталья Владимировна", "ауд. 229")
# English_Thursday_1 = Lesson("Английский язык (I подгруппа)", "15:00 - 16:35", "Пояркова Александра Викторовна", "ауд. 229")
# English_Thursday_2 = Lesson("Английский язык (II подгруппа)", "15:00 - 16:35", "Хотянова Ольга Борисовна", "ауд. 209")
# Lunch_Wednesday = Lesson("Обед", "14:05 - 15:00")

# # Пятница
# Chemistry_Lecture_Friday = Lesson("Общая химия и химия элементов (лекция)", "10:45 - 12:20", "Гудилин Е.А., Шевельков А.В.", "БХА")
# Lunch_Friday = Lesson("Обед", "12:20 - 13:10")
# Introduction_Friday = Lesson("Введение в специальность", "13:10 - 14:55", "Тарасов Алексей Борисович", "ауд. 229")
# Chemistry_Seminar_Friday = Lesson("Общая химия и химия элементов (семинар)", "15:00 - 16:35", "Берекчиян М.В., Брылѐв О.А., Харченко А.В.", "ауд. 209, 219, 229")

# # Суббота
# Linear_Algebra_1 = Lesson("Высшая алгебра и аналитическая геометрия", "10:00 - 13:00", "Толпыго Денис Сергеевич", "ауд. 229")
# Lunch = Lesson("Обед", "13:00-14:00")
# Physical_Culture_Saturday = Lesson("Физическая культура", "14:00 - 15:35", "Еремина Любовь Павловна")


# FNM_first_course = {
#     "Monday": [
#         English_Monday_1,
#         English_Monday_2,
#         Chemistry_Seminar,
#         Lunch_Monday,
#         Practice_Chemistry_1,
#         Practice_Chemistry_2
#     ],
#     "Tuesday": [
#         Math_Seminar_Tuesday,
#         Chemistry_Lecture,
#         Practice_Chemistry_Tuesday,
#         Lunch_Tuesday,
#         Chemistry_Seminar_Tuesday
#     ],
#     "Wednesday": [
#         Programming_1,
#         Programming_2,
#         Lunch_Wednesday,
#         Physical_Culture_Wednesday
#     ],
#     "Thursday": [
#         Math_Seminar_Thursday_1,
#         Math_Lecture_Thursday_2,
#         English_Thursday_1,
#         English_Thursday_2
#     ],
#     "Friday": [
#         Chemistry_Lecture_Friday,
#         Lunch_Friday,
#         Introduction_Friday,
#         Chemistry_Seminar_Friday
#     ],
#     "Saturday": [
#         Linear_Algebra_1,
#         Lunch,
#         Physical_Culture_Saturday
#     ],
#     "Sunday": []  # Выходной день
# }