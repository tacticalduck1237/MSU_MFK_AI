#ссылка на ноутбук https://colab.research.google.com/drive/1NWkGyzrcRRzqN_doGzHBvDdFkVOnOSzo?usp=sharing

#ПРОРЕШАННЫЙ НОУТБУК
import numpy as np

def precision(y_true, y_pred):
    true_positive = np.sum((y_true == 1) & (y_pred == 1))
    false_positive = np.sum((y_true == 0) & (y_pred == 1))

    if true_positive + false_positive == 0:
        return 0.0
    return true_positive / (true_positive + false_positive)

def recall(y_true, y_pred):
    true_positive = np.sum((y_true == 1) & (y_pred == 1))
    false_negative = np.sum((y_true == 1) & (y_pred == 0))

    if true_positive + false_negative == 0:
        return 0.0
    return true_positive / (true_positive + false_negative)

def f1(y_true, y_pred):
    prec = precision(y_true, y_pred)
    rec = recall(y_true, y_pred)
    if prec + rec == 0:
        return 0.0
    return 2 * (prec * rec) / (prec + rec)
