#!/usr/bin/python3

import sys
import numpy as np


def fingerprint(text, model):
    """
    :param text: список слов в документе
    :param model: модель, загруженная в Gensim
    :return: возвращаем средний вектор слов в тексте (semantic fingerprint)
    """
    # Создаем список всех слов в документе, которые есть в модели
    lexicon = [w for w in text if w in model]
    lw = len(lexicon)
    if lw < 1:
        print('Empty lexicon in', text, file=sys.stderr)
    vectors = np.zeros((lw, model.vector_size))  # Создаём пустую матрицу векторов для слов
    for i in list(range(lw)):  # Перебираем все слова в тексте
        word = lexicon[i]
        vectors[i, :] = model[word]  # Добавляем вектор текущего слова в матрицу
    semantic_fingerprint = np.sum(vectors, axis=0)  # Вычисляем сумму векторов всех слов в документе
    semantic_fingerprint = np.divide(semantic_fingerprint, lw)  # Вычисляем среднее
    return semantic_fingerprint
