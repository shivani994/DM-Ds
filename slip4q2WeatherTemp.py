#Ass3setbq1 slip4q2
#consider following dataset
#weather=['Sunny','Sunny','Overcast','Rainy','Rainy','Rainy','Overcast','Sunny','Sunny','Rainy','Sunny','Overcast','Overcast','Rainy']
#temp=['Hot','Hot','Hot','Mild','Cool','Cool','Cool','Mild','Cool','Mild','Mild','Mild','Hot','Mild']
#play=['No','No','Yes', 'Yes', 'Yes', 'No' ,'Yes' ,'No', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No']
#use navie Bayes algorithm tp predict[0:Overcast, 2:Mild]tuple belong  to which class whether to play the sport or not
#assigining features and label varible

weather=['Sunny','Sunny','Overcast','Rainy','Rainy','Rainy','Overcast','Sunny','Sunny','Rainy','Sunny','Overcast','Overcast','Rainy']
temp=['Hot','Hot','Hot','Mild','Cool','Cool','Cool','Mild','Cool','Mild','Mild','Mild','Hot','Mild']
play=['No','No','Yes', 'Yes', 'Yes', 'No' ,'Yes' ,'No', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No']

#import labeEncoder
from sklearn import preprocessing

#creating labelEncoder
le= preprocessing.LabelEncoder()

#converting string labels into numbers.
wheather_encoded=le.fit_transform(weather)
print(wheather_encoded)

#converting string labels into numbers
temp_encoded=le.fit_transform(temp)
label=le.fit_transform(play)
print("Temp:",temp_encoded)
print("play:",label)

#combining weather and temp into single list of tuples
features=zip(wheather_encoded,temp_encoded)
print(features)

#import Gaussain Naive Bayes model
from sklearn.naive_bayes import GaussianNB

#Create a Gaussian Classifier
model=GaussianNB()

#Train the model using the training sets
model.fit(features,label)

#predict Output

predicted=model.predict([0,2])# 0:overcast, 2:Mild
print("Predicted Value:",predicted)