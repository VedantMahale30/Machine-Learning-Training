import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

#load data 
data  = pd.read_csv("hp.csv")
print(data)

#feature and target

feature = data[["area"]]
target = data["price"]
print(feature)
print(target)

#train and test the data 

x_train,x_test,y_train,y_test = train_test_split(feature,target,random_state=11)
print(x_train)
print(y_train)
print(x_test)
print(y_test)


#model using train data 
model = LinearRegression()
model.fit(x_train,y_train)

#score using test data
score = model.score(x_test,y_test)
print(score)





