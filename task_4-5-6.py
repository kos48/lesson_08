'''
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
уникальные для каждого типа оргтехники.
5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и
передачу в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
а также других данных, можно использовать любую подходящую структуру, например словарь.
6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например,
для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных
на уроках по ООП.
'''

import json

class ErrorData(Exception):
    def __init__(self):
        self.message = 'Не числовой тип данных'
        super().__init__(self.message)

class Warehouse:  # склад
    _total_products = 0
    product_list = []

    def __init__(self, name, price, quantity, unit):
        self.name = name
        self.price = price
        try:
            if type(quantity) == int: # проверка на тип данных
                self.quantity = quantity
            else:
                raise ErrorData
        except ErrorData as e:
            print('количество должно быть число!!!', e)
        self.unit = unit
        Warehouse._total_products += 1

    def __str__(self):
        return f'название: {self.name}, цена:{self.price}, кол-во: {self.quantity}({self.unit}) '

class OfficeMaschines(Warehouse):  # оргтехника
    _ids = []
    _default_id = 0
    product_list = []

    def __init__(self, name, price, quantity, unit, id=None):
        super().__init__(name, price, quantity, unit)
        if id != None and id not in OfficeMaschines._ids:
            self.id = id
        else:
            while OfficeMaschines._default_id in OfficeMaschines._ids:
                OfficeMaschines._default_id += 1
            self.id = OfficeMaschines._default_id
        OfficeMaschines._ids.append(self.id)

    @property
    def change_name(self):
        return self.name

    @change_name.setter
    def change_name(self, value):
        self.name = value

    @property
    def change_price(self):
        return self.price

    @change_price.setter
    def change_price(self, value):
        self.price = value

    @property
    def change_quantity(self):
        return self.quantity

    @change_quantity.setter
    def change_quantity(self, value):
        self.quantity = value

    @property
    def change_unit(self):
        return self.unit

    @change_unit.setter
    def change_unit(self, value):
        self.unit = value

    def reception(self, subdivision):
        '''прием на склад, передача в подразделение компании, запись в файл'''
        self.subdivision = subdivision  # название подразделения
        spec_product_list = []
        spec_product_list.append([self.subdivision, self.product, self.name, self.price, self.quantity,
                                       self.unit, self.id])
        Warehouse.product_list.append(spec_product_list)
        print(f'{self.product} {self.name} принят на склад. Подразделение {self.subdivision}')
        file_name = 'product_list.json'
        x = input('сохранить в файл? (Y/N)')
        if x.upper() == 'Y':
            with open(file_name, 'a', encoding='utf-8') as f:  # запись в файл
                f.write('\n')
                json.dump(spec_product_list, f)
            print(f'данные сохранены в {file_name}')

class Printer(OfficeMaschines):
    product = 'Printer'

    def __init__(self, name, price, quantity, unit, id, color):
        super().__init__(name, price, quantity, unit, id)
        self.color = color
        self.product = 'Printer'

    @property
    def change_color(self):
        return self.color

    @change_color.setter
    def change_color(self, value):
        self.color = value

    def __str__(self):
        return f'название: {self.name}, цена:{self.price}, кол-во: {self.quantity}({self.unit}), id={self.id},' \
               f' color = {self.color} '

class Scanner(OfficeMaschines):
    product = 'Scanner'

class Xerox(OfficeMaschines):
    product = 'Xerox'

a = Printer('sony', 5000, 100, 'PCS', '0002', True)
a.color = False
a.reception('logistics')
print(a)

b = Scanner('sony', 5000, 100, 'PCS')
b.reception('express')
print(b)

c = Xerox('Panasonic', 2000, 50, 'PCS')
c.reception('logistics')
print(c)

print(OfficeMaschines._ids)

# print(Warehouse.product_list)

