'''1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
«день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать
число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить
валидацию числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных
данных.'''


class Date:

    def __init__(self, str_date):
        self.str_date = str(str_date)

    @classmethod
    def transform_date(cls, str_date):
        num_date = []
        for el in str_date.split('-'):
            num_date.append(el)
        return int(num_date[0]), int(num_date[1]), int(num_date[2])

    @staticmethod
    def validation_date(day, month, year):
        if (day <=0 or day >31) or (month <=0 or month > 12):
            return f'Неверная дата!!!'
        return str(day) + '-' +str(month) + '-' + str(year)


print(Date.transform_date('1-02-1999'))

print(Date.validation_date(223, 30, 1980))
print(Date.transform_date(Date.validation_date(21, 3, 1980)))
print(Date.validation_date(21, 3, 1980))