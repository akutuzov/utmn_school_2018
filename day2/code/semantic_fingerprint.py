#!/usr/bin/python3

import sys
import numpy as np
from gensim import utils


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


def save_model(fname, words, vectors):
    """
    :param fname: имя файла, в который мы хотим сохранить векторную модель
    :param words: список сущностей (слов, предложений, других идентификаторов)
    :param vectors: список векторов для этих сущностей
    :return:
    """
    total_vec = len(vectors)
    with utils.smart_open(fname, 'ab') as fout:
        print("storing %s x %s projection weights into %s" % (total_vec, len(vectors[0]), fname), file=sys.stderr)
        fout.write(utils.to_utf8("%s %s\n" % (total_vec, len(vectors[0]))))
        for i in range(len(vectors)):
            doctag = words[i]
            row = vectors[i]
            fout.write(utils.to_utf8("%s %s\n" % (doctag.strip(), ' '.join("%f" % val for val in row))))
