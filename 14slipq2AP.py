#Q2. Write a Python Programme to apply Apriori algorithm on Groceries dataset. Dataset
#can be downloaded from
#(https://github.com/amankharwal/Websitedata/blob/master/Groceries
#_dataset.csv).
#Also display support and confidence for each rule.

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from apyori import apriori
store_data = pd.read_csv('Groceries_dataset.csv',header=None)
store_data.head()
records = []
for i in range(0, 7501):
    records.append([str(store_data.values[i,j]) for j in range(0, 20)])
association_rules = apriori(records, min_support=0.0045, min_confidence=0.2, min_lift=3, max_length=None)
association_results = list(association_rules)
print(len(association_results))
48
for item in association_results:

    # first index of the inner list
    # Contains base item and add item
    pair = item[0] 
    items = [x for x in pair]
    
    print("Le:",items)
    print("Rule: " + items[0] + " -> " + items[1])

    #second index of the inner list
    print("Support: " + str(item[1]))

    #third index of the list located at 0th
    #of the third index of the inner list

    print("Confidence: " + str(item[2][0][2]))
    print("Lift: " + str(item[2][0][3]))
    print("=====================================")