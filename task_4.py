# 4. Начните работу над проектом «Склад оргтехники».
# Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные
# для каждого типа оргтехники.

class StoreHouse:
    def __init__(self):
        self.store = {}

    def create_item(self):
        item_list = {}
        i = 0
        while True:
            user_input = input('Choose item ("printer", "scaner", "herox") or "q" to stop: ')
            if user_input == 'q':
                break
            if user_input in ['printer', 'scaner', 'herox', 'Printer', 'Scaner', 'Herox']:
                try:
                    name = input(f'Enter {user_input} name: ')
                    cost = int(input(f'Enter {user_input} cost: '))
                    quantity = int(input(f'Enter {user_input} quantity: '))
                    unicnum = input(f'Enter unic {user_input} number: ')
                    if user_input == 'printer':
                        a = Printer(name, cost, quantity, unicnum)
                        i += 1
                        item_list[f'№{i}'] = a.tech
                    elif user_input == 'scaner':
                        a = Scaner(name, cost, quantity, unicnum)
                        i += 1
                        item_list[f'№{i}'] = a.tech
                    elif user_input == 'herox':
                        a = Herox(name, cost, quantity, unicnum)
                        i += 1
                        item_list[f'№{i}'] = a.tech
                except:
                    print('Wrong input!')
                    continue
            else:
                print('Wrong input')
                continue
        return item_list

    def moving_item(self, item):
        office = input('Choose office (Moscow, St.Peterburg): ')
        self.store[office] = item
        return self.store


class Orgtech:
    def __init__(self, model, cost, quantity):
        self.tech = {'Model': model, 'Cost': cost, 'Quantity': quantity}


class Printer(Orgtech):
    def __init__(self, model, cost, quantity, pr_num):
        super().__init__(model, cost, quantity)
        self.tech['Unic_Num'] = pr_num


class Scaner(Orgtech):
    def __init__(self, model, cost, quantity, sc_num):
        super().__init__(model, cost, quantity)
        self.tech['Unic_Num'] = sc_num


class Herox(Orgtech):
    def __init__(self, model, cost, quantity, hr_num):
        super().__init__(model, cost, quantity)
        self.tech['Unic_Num'] = hr_num


sh = StoreHouse()
sh.moving_item(sh.create_item())
for key, value in sh.store.items():
    print(key, value)
