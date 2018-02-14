#!/usr/bin/python3

def calculate_jaccard(data0, data1):
    set0 = set(data0)
    set1 = set(data1)
    n = len(set0 & set1)
    similarity = n / (len(set0) + len(set1) - n)
    return similarity
