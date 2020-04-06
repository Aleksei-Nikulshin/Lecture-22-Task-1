from pprint import pprint


# Домашнее задание к лекции 2.2 «Классы и их применение в Python»
# Вы приехали помогать на ферму Дядюшки Джо и видите вокруг себя множество разных животных:

# гусей "Серый" и "Белый"
# корову "Маньку"
# овец "Барашек" и "Кудрявый"
# кур "Ко-Ко" и "Кукареку"
# коз "Рога" и "Копыта"
# и утку "Кряква"
# Со всеми животными вам необходимо как-то взаимодействовать:

# кормить
# корову и коз доить
# овец стричь
# собирать яйца у кур, утки и гусей
# различать по голосам(коровы мычат, утки крякают и т.д.)
# Задача №1
# Нужно реализовать классы животных, не забывая использовать наследование, определить общие методы взаимодействия с животными и дополнить их в дочерних классах, если потребуется.

# Задача №2
# Для каждого животного из списка должен существовать экземпляр класса. Каждое животное требуется накормить и подоить/постричь/собрать яйца, если надо.

# Задача №3
# У каждого животного должно быть определено имя(self.name) и вес(self.weight).

# Необходимо посчитать общий вес всех животных(экземпляров класса);
# Вывести название самого тяжелого животного.


class Animals:
    state = 'hungry'
    name = ''
    animals_count = 0
    sum_weight = 0
    item_dict = {}
    item_list = []

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        Animals.animals_count += 1
        self.__class__.sum_weight += self.weight
        self.__class__.item_dict[self.name] = self.weight
        Animals.item_dict[self.name] = self.weight
        Animals.item_list.append(self.__class__.item_dict)
        Animals.sum_weight += self.weight

    def feed(self):  # покормить
        print(f'Вы только что покормили {self.name} !')
        self.state = 'full'

    def weight():
        print(f'Общий вес всех животных {Animals.sum_weight}')
        name_class = input(
            'Введите название класса, по которому Вы желаете получить общий вес экземпляров класса, или "q", если нужно остановить программу: ')
        if name_class == "q":
            print('Программа остановлена')
        elif name_class == 'Goose':
            print(f'Общий вес экземпляров класса {name_class} составляет {Goose.sum_weight}')
        elif name_class == 'Cow':
            print(f'Общий вес экземпляров класса {name_class} составляет {Cow.sum_weight}')
        elif name_class == 'Sheeps':
            print(f'Общий вес экземпляров класса {name_class} составляет {Sheeps.sum_weight}')
        elif name_class == 'Chicken':
            print(f'Общий вес экземпляров класса {name_class} составляет {Chicken.sum_weight}')
        elif name_class == 'Goats':
            print(f'Общий вес экземпляров класса {name_class} составляет {Goats.sum_weight}')
        elif name_class == 'Ducks':
            print(f'Общий вес экземпляров класса {name_class} составляет {Ducks.sum_weight}')
        else:
            print("Класса с таким названием нет")


def weight_max():  # Вывести название самого тяжелого животного с результатом
    d = Animals.item_dict.items()
    c = list(d)
    f = sorted(Animals.item_dict, key=Animals.item_dict.get, reverse=True)
    start_value = 0
    result_dict = {}
    for k, v in c:
        if f[0] in k:
            print(f'Наибольший вес у экземпляра {k} с результатом {v}')


class Goose(Animals):
    voice = 'honk'
    add_state = 'with eggs'
    sum_weight = 0
    item_dict = {}

    def collect_eggs(self):
        print(f'Вы только что собрали яйца у {self.name} !')
        self.add_state = 'without eggs'


class Cow(Animals):
    voice = 'moo'
    add_state = 'with milk'
    sum_weight = 0
    item_dict = {}

    def milk(self):
        print(f'Вы только что подоили {self.name} !')
        self.add_state = 'without milk'


class Sheeps(Animals):
    voice = 'baa'
    add_state = 'with wool'
    sum_weight = 0
    item_dict = {}

    def cut(self):
        print(f'Вы только что подстригли {self.name} !')
        self.add_state = 'without wool'


class Chicken(Goose):
    voice = 'cluck'
    sum_weight = 0
    item_dict = {}


class Goats(Cow):
    horns = 'horns'
    voice = 'baa'
    sum_weight = 0
    item_dict = {}


class Ducks(Goose):
    voice = 'quack'
    sum_weight = 0
    item_dict = {}


goose_gray = Goose('Серый', 8)
goose_white = Goose('Белый', 7)

cow_manka = Cow('Манька', 30)

sheep_barashek = Sheeps('Барашек', 12)
sheep_kudryavii = Sheeps('Кудрявый', 13)

chicken_ko_ko = Chicken('Ко-Ко', 2)
chicken_kukareku = Chicken('Кукареку', 2)

goat_roga = Goats('Рога', 11)
goat_kopita = Goats('Копыта', 11)

duck_kryakwa = Ducks('Кряква', 4)

weight_max()
Animals.weight()



