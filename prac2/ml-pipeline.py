import pickle
import sys
import numpy as np 
from sklearn.linear_model import LogisticRegression
print("===ML Pipeline===")
X=np.array([[1], [2], [3]])
y=np.array([[2,4,6]])
model=LinearRegression()
model.fit(X,y)
print("Model trained")

with open('model.pkl', 'wb') as f:
    pickle.dump(model,f)
print("Model saved")
pred=model.predict([[4]])[0]
print(f"Prediction: {pred:.1f}")
if abs(pred-8.0)<0.1:
    print("VALIDATION SUCCESSFULL")
    sys.exit(0)
else:
    print("VALIDATION FAILED")
    sys.exit(1)