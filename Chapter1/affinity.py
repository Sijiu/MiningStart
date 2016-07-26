# coding:utf-8
import numpy as np
from collections import defaultdict
from operator import itemgetter

dataset_filename = "affinity_dataset.txt"
X = np.loadtxt(dataset_filename)
n_samples, n_features = X.shape
# print X[:6], len(X), n_samples, n_features

# num_apple_purchases = 0
# for sample in X:
#     if sample[3]:
#         num_apple_purchases += 1
# print "{0} people bought apples".format(num_apple_purchases)

features = ["bread", "milk", "cheese", "apples", "bananas"]

valid_rules = defaultdict(int)
invalid_rules = defaultdict(int)
num_occurences = defaultdict(float)
for sample in X:  # sample 样本
    for premise in range(5):  # premise 前提
        if sample[premise] == 0:
            continue
        num_occurences[premise] += 1
        for conclusion in range(n_features):  # conclusion 结论
            if premise == conclusion:
                continue
            if sample[conclusion] == 1:
                valid_rules[(premise, conclusion)] += 1
            else:
                invalid_rules[(premise, conclusion)] += 1
# print num_occurences
support = valid_rules
confidence = defaultdict(float)
for premise, conclusion in valid_rules.keys():
    rule = (premise, conclusion)
    confidence[rule] = valid_rules[rule] / num_occurences[premise]
# print confidence

def print_rule(premise, conclusion, support, confidence, features):
    premise_name = features[premise]
    conclusion_name = features[conclusion]
    print "Rules: If a person buys {0} they will also buy {1}".format(premise_name, conclusion_name)
    print "- Support : {0}".format(support[(premise, conclusion)])
    print "- Confidence : {0:.3f}".format(confidence[(premise, conclusion)])

# print_rule(1, 3, support, confidence, features)
sorted_support = sorted(support.items(), key=itemgetter(1), reverse=True)
for index in range(5):
    print "Rule #{0}".format(index + 1)
    premise, conclusion = sorted_support[index][0]
    print_rule(premise, conclusion, support, confidence, features)



