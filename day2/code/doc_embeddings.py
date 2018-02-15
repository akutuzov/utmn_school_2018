#!/usr/bin/python3

import gensim
import logging

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


modelfile = ''  # Укажите путь к файлу с моделью для отдельных слов

# Загружаем модель:
if modelfile.endswith('.vec.gz'):
    model = gensim.models.KeyedVectors.load_word2vec_format(modelfile, binary=False)
elif modelfile.endswith('.bin.gz'):
    model = gensim.models.KeyedVectors.load_word2vec_format(modelfile, binary=True)
else:
    model = gensim.models.Word2Vec.load(modelfile)
model.init_sims(replace=True)

# Загрузите в Python предложения из файла sentences_lemmatized.txt
# Сгенерируйте для каждого предложения усредненный вектор
# при помощи функции fingerprint из файла semantic_fingeprint.py
# Вам нужно импортировать эту функцию в начале своего скрипта
# Запишите каждый усредненный вектор (семантический отпечаток) в список


# Импортируйте из semantic_fingerprint.py функцию save_model
# и сохраните получившиеся у вас средние вектора предложений как отдельную векторную модель
