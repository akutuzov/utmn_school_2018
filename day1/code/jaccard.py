#!/usr/bin/python3


def calculate_jaccard(data0, data1):
    """
    :param data0: первый список данных (например, соседей слова в первой модел)
    :param data1: второй список данных (например, соседей слова во второй модели)
    :return: возвращаем коэффициент близости этих двух списков по Жаккару (от 0 до 1)
    """
    set0 = set(data0)
    set1 = set(data1)
    n = len(set0 & set1)
    similarity = n / (len(set0) + len(set1) - n)
    return similarity
