# coding:utf-8
from collections import defaultdict
from sklearn.datasets import load_iris  # 鸢尾属植物
from operator import itemgetter

dataset = load_iris()
x = dataset.data
y = dataset.target
# print "iris==", dataset.DESCR


def train_feature_value(X, y_true, feature_index, value):
    class_counts = defaultdict(int)
    for sample, y in zip(X, y_true):
        if sample[feature_index] == value:
            class_counts[y] += 1
    sorted_class_counts = sorted(class_counts.items(), key=itemgetter(1), reverse=True)
    most_frequent_class = sorted_class_counts[0][0]
    incorrect_predictions = [class_counts for class_value, class_count in class_counts.items() if class_value
                             != most_frequent_class]
    error = sum(incorrect_predictions)
    return most_frequent_class, error