# author: leisurexi
# date: 2021-01-16 16:05
# 抽象类和抽象方法示例

from abc import ABCMeta, abstractmethod


class Entity(metaclass=ABCMeta):
    @abstractmethod
    def get_title(self):
        pass

    @abstractmethod
    def set_title(self):
        pass


class Document(Entity):
    def get_title(self):
        return self.title

    def set_title(self, title):
        self.title = title


if __name__ == '__main__':
    document = Document()
    document.set_title("Harry Potter")
    print(document.get_title())

    entity = Entity()
