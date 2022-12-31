#ass2setAQ2slip15 write a python program build Decision tree classfier for shows.csv
# from pandas and predict class label for show staring a 40 years old
# american comedian, with 10 years of experience, and a comedy ranking of 7?
#create csv file as shown in
#http://www.w3schools.com/python/python_ml_decision_tree.asp

import pandas 
from sklearn import tree
#import pydotplus
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
#import matplotlib.image as pltimg
df= pandas.read_csv("shows1.csv")
d={'UK':0,'USA':1,'N':2}
df['Nationality']=df['Nationality'].map(d)
d={'YES':1,'NO':0}
df['Go']=df['Go'].map(d)
features=['Age','Experience','Rank','Nationality']
X=df[features]
y=df['Go']
dtree=DecisionTreeClassifier()
dtree=dtree.fit(X,y)
#data=tree.export_graphviz(dtree,out_file=None,feature_name=features)
#graph=pydotplus.graph_from_dot_data(data)
#graph.write_png('mydecisiontree.png')
#img=pltimg.imread('mydecisiontree.png')
#imgplot=plt.imshow(img)
tree.plot_tree(dtree,feature_name=features)
#two line  to make our compiler able to draw:
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()
#plt.show()




