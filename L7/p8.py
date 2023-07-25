import pandas as pd
from sklearn.linear_model import LogisticRegression 
from sklearn.model_selection import train_test_split
from sklearn.metrics import plot_confusion_matrix, classification_report
import matplotlib.pyplot as plt

data = pd.read_csv("vehicle_data_sep2022.csv")
print(data)

feature =data[["Age"]]
target =data[["Vehicle"]]


x_train, x_test, y_train, y_test = train_test_split(feature,target)


model = LogisticRegression()
model.fit(feature,target)

plot_confusion_matrix(model,x_test,y_test)
plt.show()
input()

cr = classification_report(y_test,model.predict(x_test))
print(cr)
















