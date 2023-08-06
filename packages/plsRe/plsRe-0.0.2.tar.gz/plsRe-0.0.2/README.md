# plsre Documentation
* * *
## Installation
```python
pip install plsre
```
* * *
## Usage
```python
from plsre import PlsRegression as PR
# Perform Partial Least_Squared Regression training

X = np.array([[0., 0., 1.], [1.,0.,0.], [2.,2.,2.], [2.,5.,4.]])
Y = np.array([[0.1, -0.2], [0.9, 1.1], [6.2, 5.9], [11.9, 12.3]])

P, Q, W, T,B = PR.plsr_train(X,Y)

# Perform Prediction using different optimization
print(PR.plsr_predict(X,Y,P,Q,W,B))
print(PR.plsr_predict_numba(X,Y,P,Q,W,B))
print(PR.plsr_predict_numpy(X,Y,P,Q,W,B))

```
