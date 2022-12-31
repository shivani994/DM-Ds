#ass6setaq2  and slip20
#write  a python program to impelement hierarchical Agglomerative clustering algoritm
#(download customer.csv dataset from github.com).

import numpy as pandas
import pandas as pd
import matplotlib.pyplot as mtp
dataset=pd.read_csv('Mall_Customers.csv')
x=dataset.iloc[:,[3,4]].values
import scipy.cluster.hierarchy as shc
dendro = shc.dendrogram(shc.linkage(x, method="ward"))
mtp.title("Dendrogram plot")
mtp.ylabel("Euclidean Distance")
mtp.xlabel("Customers")
mtp.show()
from sklearn.cluster import AgglomerativeClustering
hc= AgglomerativeClustering(n_clusters=5,affinity='euclidean',linkage='ward')
y_pred=hc.fit_predict(x)
mtp.scatter(x[y_pred==0,0],x[y_pred==0,1],s=100,c='blue',label='Cluster 1')
mtp.scatter(x[y_pred==1,0],x[y_pred==1,1],s=100,c='green',label='Cluster 2')
mtp.scatter(x[y_pred==2,0],x[y_pred==2,1],s=100,c='red',label='Cluster 3')
mtp.scatter(x[y_pred==3,0],x[y_pred==3,1],s=100,c='cyan',label='Cluster 4')
mtp.scatter(x[y_pred==4,0],x[y_pred==4,1],s=100,c='magenta',label='Cluster 5')
mtp.title('Cluster of customers')
mtp.xlabel('Annual Income(k$)')
mtp.ylabel('Spending Score(1-100)')
mtp.legend()
mtp.show()