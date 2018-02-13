#!/usr/bin/python3

import gensim
import logging

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

# Скачайте любую модель с http://rusvectores.org/ru/models/

modelfile = ''  # Укажите путь к файлу с моделью

# Загружаем модель:
if modelfile.endswith('.vec.gz'):
    model = gensim.models.KeyedVectors.load_word2vec_format(modelfile, binary=False)
elif modelfile.endswith('.bin.gz'):
    model = gensim.models.KeyedVectors.load_word2vec_format(modelfile, binary=True)
else:
    model = gensim.models.KeyedVectors.load(modelfile)
model.init_sims(replace=True)

# Список интересных нам слов (смотри частеречные тэги на http://universaldependencies.org/u/pos/all.html)
words = []

for word in words:
    # Если слово есть в модели:
    # Реализуйте вывод вектора слова
    # Реализуйте вывод ближайших соседей слов из списка и их косинусной близости
    pass

# Реализуйте вычисление близости между двумя произвольными словами

# Реализуйте решение пропорций ("мать" к "дочери" как "отец" к "сыну")

# Реализуйте вывод объёма словаря модели (сколько слов она знает)?



