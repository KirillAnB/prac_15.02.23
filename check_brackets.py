def check_brackets(brackets_row: str) -> bool:
    """
    :param brackets_row: Входная строка для проверки
    :return: True, если последовательность корректна, False в противном случае
    """
    list_ = []  # Список, в который будем добавлять скобки из проверяемой строки
    for char in brackets_row:
        if char == '(':  # Если скобка открывающая - добавляем
            list_.append(char)  # FIRST IN
        elif char == ')':  #  Если закрывающая - проверяем, что перед ней была открывающая
            if list_:
                del list_[-1]  # FIRST OUT
            else:
                return False
    if list_:  #  Если после проверки строки остались незакрытые скобки
        print(list_)
        return False
    return True  #  Возвращаем  True если строка была пустой или все скобки были закрыты


if __name__ == '__main__':
    print(check_brackets("()()"))  # True
    print(check_brackets(")("))  # False
    print(check_brackets(''))  # True
    print(check_brackets('('))  # False
    print(check_brackets(')'))  # False
