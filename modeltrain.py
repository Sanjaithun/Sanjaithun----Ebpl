import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib

# Sample dataset (replace with real one for 100+ features)
data = {
    'area': [1000, 1500, 2000, 2500],
    'bedrooms': [2, 3, 4, 3],
    'bathrooms': [1, 2, 3, 2],
    'location': ['Chennai', 'Bangalore', 'Hyderabad', 'Chennai'],
    'price': [50, 75, 120, 90]
}

df = pd.DataFrame(data)

df['location'] = df['location'].astype('category').cat.codes

X = df[['area', 'bedrooms', 'bathrooms', 'location']]
y = df['price']

model = RandomForestRegressor()
model.fit(X, y)

joblib.dump(model, 'model.pkl')
print("✅ Model trained and saved!")
