from re import *

def first_task() -> tuple:
    data = ''.join(open('task1-ru.txt', encoding='UTF-8').readlines())
    first_search = set(findall(r' (с[a-zA-Zа-яА-ЯёЁ]+)', data))
    second_search = set(findall(r'и ([a-zA-Zа-яА-ЯёЁ]+)', data))
    return first_search, second_search


def second_task() -> list:
    data = ''.join(open('task2.html', encoding='UTF-8').readlines())
    search = set(findall(r"font-family: '(.*?)'", data))
    return search


def output() -> None:
    print('Вариант 7\n')
    first_answer = first_task()
    [print(*answer, end='\n\n') for answer in first_answer]

    second_answer = second_task()
    print(*second_answer)
    

if __name__ == '__main__':
    output()








