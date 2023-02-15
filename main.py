"""
My little Queue
"""
from typing import Any


class Queue:
    def __init__(self):
        """
        Очередь с помощью python list
        Начало очередм - жлемент списка с индексом 0, конец очереди - элемент с индексом len(my_queue)-1
        """
        self.my_queue = []  # TODO инициализировать список

    def enqueue(self, elem: Any) -> None:
        """
        Добавление элемент в конец очереди

        :param elem: Элемент, который должен быть добавлен
        """
        self.my_queue.append(elem)

    def dequeue(self) -> Any:
        """
        Извлечение элемента из начала очереди.

        :raise: IndexError - Ошибка, если очередь пуста

        :return: Извлеченный с начала очереди элемент.
        """
        if not len(self.my_queue) > 0:
            raise IndexError('Очередь пуста')
        elem_to_remove = self.my_queue.pop(0)
        return elem_to_remove

    def peek(self, ind: int = 0) -> Any:
        """
        Просмотр произвольного элемента, находящегося в очереди, без его извлечения.

        :param ind: индекс элемента (отсчет с начала, 0 - первый с начала элемент в очереди, 1 - второй с начала элемент в очереди, и т.д.)

        :raise: TypeError - если указан не целочисленный тип индекса
        :raise: IndexError - если индекс вне границ очереди

        :return: Значение просмотренного элемента
        """
        if not isinstance(ind, int):
            raise TypeError('Индекс элемента не типа integer!')
        elem_to_check = self.my_queue[ind]  # TODO реализовать метод peek
        if ind < 0 or ind > len(self.my_queue) :
            raise IndexError('Индекс вне границ очереди!')
        return elem_to_check

    def clear(self) -> None:
        """ Очистка очереди. """
        self.my_queue.clear()  # TODO реализовать метод clear

    def __len__(self):
        """ Количество элементов в очереди. """
        sum_ = 0
        for _ in self.my_queue:
            sum_ += 1
        return sum
if __name__ == '__main__':
    queue1 = Queue()
    queue1.enqueue(1)
    queue1.enqueue(2)
    print(queue1.peek(2))