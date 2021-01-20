# author: leisurexi
# date: 2021-01-20 22:21
# Python metaclass

import yaml


class Monster(yaml.YAMLObject):
    yaml_tag = u'!Monster'

    def __init__(self, name, hp, ac, attacks):
        self.name = name
        self.hp = hp
        self.ac = ac
        self.attacks = attacks

    def __repr__(self):
        return f'{self.__class__.__name__}(name={self.name}, hp={self.hp}, ac={self.ac}, attacks={self.attacks})'


if __name__ == '__main__':
    # yaml.load("""
    # --- !Monster
    # name: Cave spider
    # hp: [2,6]    # 2d6
    # ac: 16
    # attacks: [BITE, HURT]
    # """)

    monster = Monster('Cave spider', [2, 6], 16, ['BITE', 'HURT'])
    print(yaml.dump(monster))

    class MyClass:
        data = 1

    instance = MyClass()
    print(MyClass)
    print(instance)
    print(instance.data)

    MyClass = type('MyClass', (), {'data': 1})
    instance = MyClass()
    print(MyClass)
    print(instance)
    print(instance.data)
