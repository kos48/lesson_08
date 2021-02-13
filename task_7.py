'''7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры
класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного
результата.'''

class Complex_number:

    def __init__(self, num_1, num_2):
        self.num_1 = num_1
        self.num_2 = num_2

    def __add__(self, other):
        return f'{self.num_1 + other.num_1} + {self.num_2 + other.num_2} * i'

    def __mul__(self, other):
        return f'{self.num_1 * other.num_1 - (self.num_2 * other.num_2)} + {self.num_2 * other.num_1} * i'

a = Complex_number(1, 2)
b= Complex_number(3, 4)
print(a + b)
print(a * b)
