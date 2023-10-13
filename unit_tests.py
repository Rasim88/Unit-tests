import pytest
from list_comparator import ListComparator

class TestListComparator:
    def test_calculate_average(self):
        comparator = ListComparator([], [])
        assert comparator.calculate_average([1, 2, 3, 4, 5]) == 3

    def test_compare_averages(self):
        comparator = ListComparator([1, 2, 3, 4, 5], [6, 7, 8, 9, 10])
        assert comparator.compare_averages() == "Второй список имеет большее среднее значение"

        comparator = ListComparator([1, 2, 3, 4, 5], [1, 2, 3, 4, 5])
        assert comparator.compare_averages() == "Средние значения равны"

        comparator = ListComparator([1, 2, 3, 4, 5], [0, 0, 0, 0, 0])
        assert comparator.compare_averages() == "Первый список имеет большее среднее значение"
