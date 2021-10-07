
#################################Home Learning Task 6 Part B

# https://stackabuse.com/linear-regression-in-python-with-scikit-learn/
#From this website select follow and complete the Linear Regression Model.


#########LINEAR REGRESSION THEORY
import pandas as pd
import numpy as np
from pandas.core.frame import DataFrame
import matplotlib.inline as plt
dataset = pd.read_csv("student_scores.csv")
dataset.shape

dataset.head()

dataset.describe()

dataset.plot(x="Hours", y="Scores", style="o")
plt.title("Hours vs Percentage")
plt.xlabel("Hours Studied")
plt.ylabel("Percentage Score")
plt.show()

X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 1].values

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

print(regressor.intercept_)

print(regressor.coef_)

y_pred = regressor.predict(X_test)

DataFrame = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
DataFrame

from sklearn import metrics
print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))

Mean Absolute Error: 4.183859899
Mean Squared Error: 21.5987693072
Root Mean Squared Error: 4.6474476121


########MULTI LINEAR REGRESSION
import pandas as pd
import numpy as np
import matplotlib.inline as plt
dataset = pd.read_csv("petrol_consumption.csv")
dataset.shape

dataset.head()

dataset.describe()

X = dataset[['Petrol_tax', 'Average_income', 'Paved_Highways',
       'Population_Driver_licence(%)']]
y = dataset['petrol_consumption']

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

coeff_DataFrame = pd.DataFrame(regressor.coef_, X.columns, columns=['Coefficient'])
coeff_DataFrame

y_pred = regressor.predict(X_test)

DataFrame = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
DataFrame

from sklearn import metrics
print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))

Mean Absolute Error: 45.8979842541
Mean Squared Error: 3609.37119141
Root Mean Squared Error: 60.0780425065