#!/usr/bin/python3

import gensim
import logging

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


# Скачайте и распакуйте модели на НКРЯ и на корпусе новостей в Gensim-формате:
# http://rusvectores.org/static/models/rusvectores4/full_models.tar.gz

# Модифицируйте код ниже так, чтобы загружалось две модели в две разных переменных

modelfile = ''  # Укажите путь к файлу с моделью

# Загружаем модель:
if modelfile.endswith('.vec.gz'):
    model = gensim.models.KeyedVectors.load_word2vec_format(modelfile, binary=False)
elif modelfile.endswith('.bin.gz'):
    model = gensim.models.KeyedVectors.load_word2vec_format(modelfile, binary=True)
else:
    model = gensim.models.KeyedVectors.load(modelfile)
model.init_sims(replace=True)

# 1)
# Реализуйте вывод ближайших соседей слов из списка и их косинусной близости
# учитывая только высокочастотные слова (доля слова в корпусе выше 0.00001)
# Общее количество слов в корпусе каждой модели можно посмотреть на http://rusvectores.org/ru/models/
# Частоту конкретного слова WORD можно извлечь из модели model:
# frequency = model.wv.vocab[WORD].count
# или
# frequency = model.vocab[WORD].count
# (в зависимости от версии Gensim)

# Список интересных нам слов (смотри частеречные тэги на http://universaldependencies.org/u/pos/all.html)
words = []

for word in words:
    pass

# 2)
# Загрузите в Python текст
# https://github.com/akutuzov/utmn_school_2018/blob/master/day1/code/text_lemmatized.txt
# Он уже лемматизирован и размечен. Разбейте его по словам и превратите в список (split).
# Найдите 2-5 слов из этого текста, которые более всего отличаются по своему значению в НКРЯ и в новостях.
# Лучше всего сравнить списки ближайших соседей слова в двух моделях.
# Вы можете сравнить их вручную, а можете использовать какую-либо метрику схожести двух списков,
# например, коэффициент Жаккара (https://ru.wikipedia.org/wiki/%D0%9A%D0%BE%D1%8D%D1%84%D1%84%D0%B8%D1%86%D0%B8%D0%B5%D0%BD%D1%82_%D0%96%D0%B0%D0%BA%D0%BA%D0%B0%D1%80%D0%B0)
