import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
df=pd.read_csv('house_price.csv')
# print(df)
le=LabelEncoder()
df['Location']=le.fit_transform(df['Location'])
# print(df)
y=df[['Price_INR']]
print(y)
x=df.drop(['Price_INR'],axis=1)
print(x)
model=LinearRegression()
model.fit(x,y)
m1,m2,m3,m4,m5=model.coef_[0]
c=model.intercept_
print(m1,m2,m3,m4,m5,c)
sqft=int(input("Enter sqft:"))
Bedrooms=int(input("Enter bedroom:"))
Bathrooms=int(input("Enter bathrooms:"))
Location=int(input("Enter Location :"))
House_Age=int(input("Enter House_Age:"))
pradicted_house_price=m1*sqft+m2*Bedrooms+m3*Bathrooms+m4*Location+m5*House_Age+c
print(pradicted_house_price)