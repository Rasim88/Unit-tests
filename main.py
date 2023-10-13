# Класс для выполнения операций с двумя списками чисел
class ListComparator:
    def __init__(self, list1, list2):
        self.list1 = list1
        self.list2 = list2

    # Метод для вычисления среднего значения списка
    def calculate_average(self, lst):
        if len(lst) == 0:
            return 0
        return sum(lst) / len(lst)

    # Метод для сравнения средних значений двух списков
    def compare_averages(self):
        avg1 = self.calculate_average(self.list1)
        avg2 = self.calculate_average(self.list2)

        if avg1 > avg2:
            return "Первый список имеет большее среднее значение"
        elif avg2 > avg1:
            return "Второй список имеет большее среднее значение"
        else:
            return "Средние значения равны"

# Пример использования класса ListComparator
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

comparator = ListComparator(list1, list2)
result = comparator.compare_averages()
print(result)

