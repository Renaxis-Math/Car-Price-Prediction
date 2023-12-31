# %% [markdown]
# **Homework 7**
# 
# In this assignment you will do a lot of reading first. Read all text and code blocks below, and make sure you understand every line of code. At the bottom of the colab you will find the assignment.
# 
# We begin as usual with a few imports that you'll need:

# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# %% [markdown]
# We'll look at the classic "cars" dataset. You can read about it here:
# [link](https://vincentarelbundock.github.io/Rdatasets/doc/causaldata/auto.html)

# %%
cars=pd.read_csv('https://vincentarelbundock.github.io/Rdatasets/csv/causaldata/auto.csv')
cars.head(3)

# %% [markdown]
# The two columns we'll focus on are `displacement` and `mpg`. Let's take a look at them:

# %%
plt.scatter(cars.displacement, cars.mpg)

# %% [markdown]
# The following function will take an array of features `x`, an array of targets `y`, a fraction `p`, and split them into `train` and `test` sets.

# %%
def TrainTestSplit(x,y,p,seed=1):
  '''Splits datasets x and y into train and test sets
  p is the fraction going to train'''
  np.random.seed(seed) #controls randomness
  size=len(x)
  train_size=int(p*size)
  train_mask=np.zeros(size,dtype=bool)
  train_indices=np.random.choice(size, train_size, replace=False)
  train_mask[train_indices]=True
  test_mask=~train_mask
  x_train=x[train_mask]
  x_test=x[test_mask]
  y_train=y[train_mask]
  y_test=y[test_mask]
  return x_train,x_test,y_train,y_test

# %% [markdown]
# Let's apply this to the `displacement` and `mpg` columns of the `cars` dataset, and then view the resulting train and test sets.

# %%
x_train,x_test,y_train,y_test=TrainTestSplit(cars.displacement,cars.mpg,0.75)
plt.scatter(x_train,y_train)
plt.scatter(x_test,y_test,color='r')

# %% [markdown]
# Eventully, we will use gradient descent to build a polynomial model of a data set of degree d. To this end, we will need a helper function to take an array `x` and create a feature matrix of shape `(len(x),d+1)`, whose `i`th column is the array `x**i`.

# %%
def PolyFeatures(x,d):
  X=np.zeros((len(x),d+1))
  for i in range(d+1):
    X[:,i]=x**i
  return X

# %% [markdown]
# Next, we'll need a functions that `scale` and `unscale` data. It's best to do this as methods associated with a class, so that scaling can be determined by one dataset but applied to another.

# %%
class Scaler:
  def __init__(self,z):
    self.min=np.min(z)
    self.max=np.max(z)

  def scale(self,x):
    return (x-self.min)/(self.max-self.min)

  def unscale(self,x):
    return x*(self.max-self.min)+self.min

# %% [markdown]
# We can now create objects of this class that will govern how scaling and unscaling work in the x and y directions:

# %%
xscaler=Scaler(x_train)
yscaler=Scaler(y_train)

# %% [markdown]
# Try these out by uncommenting and running some of the code below. Can you tell what they do?

# %%
xscaler.scale(x_train)
xscaler.scale(x_test)
yscaler.unscale(yscaler.scale(y_test))

# %% [markdown]
# Our next task is to write a function that determines the coefficients of a linear model with feature matrix `X` and target `y`. The model will be defined by an array of coefficients, one for each column in `X`.

# %%
def train(X,y,max_iter,lr):
  coeff=np.ones(X.shape[1])
  for i in range(max_iter):
    resid=X@coeff-y
    gradient=2*((X.T)@resid)
    coeff=coeff-lr*gradient #Here's the Gradient Descent!
  return coeff

# %% [markdown]
# Next, let's create a prediction function which takes a feature matrix `X` and a model determined by coefficients `coeff` and makes predictions:

# %%
def predict(X,coeff):
  return X@coeff

# %% [markdown]
# Let's put everything together and see it in action! The code below trains a degree 5 polynomial model on x_train, y_train, and uses it to make predictions on x_test. Then, we plot the resulting curve, together with the train and test datasets.

# %%
x_train_scaled=xscaler.scale(x_train) #scale train feature
y_train_scaled=yscaler.scale(y_train) #scale train target
X_train=PolyFeatures(x_train_scaled,5) #create deg 5 feature matrix for training
coeff=train(X_train,y_train_scaled,10000,0.01) #generate coefficients of model
x_test_scaled=xscaler.scale(x_test.sort_values()) #scale x_test (sort_values is only necessary for plotting later)
X_test=PolyFeatures(x_test_scaled,5) #create deg 5 feature matrix
pred_scaled=predict(X_test,coeff) #generate scaled predictions
pred=yscaler.unscale(pred_scaled) #unscale to create predictions
plt.scatter(x_train,y_train) #plot train data
plt.scatter(x_test,y_test,color='r') #plot test data
plt.plot(x_test.sort_values(),pred,'-r') #plot model, connect the dots

# %% [markdown]
# Finally, we put this all into a function to generate the MSE for the test set, for different values of max_iter, learning rate, and degree.

# %%
def PolyScalePredictTest(max_iter,lr,d):
  x_train_scaled=xscaler.scale(x_train) #scale train feature
  y_train_scaled=yscaler.scale(y_train) #scale train target
  X_train=PolyFeatures(x_train_scaled,d) #create deg d feature matrix for training
  coeff=train(X_train,y_train_scaled,max_iter,lr) #generate coefficients of model
  x_test_scaled=xscaler.scale(x_test) #scale test feature
  X_test=PolyFeatures(x_test_scaled,d) #create deg d feature matrix for testing
  pred_scaled=predict(X_test,coeff) #generate scaled predictions for test features
  pred=yscaler.unscale(pred_scaled) #unscale to create predictions
  MSE=np.sum((pred-y_test)**2)/len(y_test) #compute MSE
  return MSE

# %% [markdown]
# Now run this code to generate a list of MSE's for different degree models:

# %%
[PolyScalePredictTest(10000,0.01,d) for d in range(1,8)]

# %% [markdown]
# You should see that the fourth element in the list is the smallest MSE, indicating that a degree 4 polymial fits the test data best. Lower degree polynomials won't be as good, and higher degree polynomials will be overfit.

# %% [markdown]
# ---
# **Assignment**
# 
# Your assignment is to create a *linear* (not polynomial) model of the mpg column of the cars dataset, based on the displacement, weight, and gear ratio columns. That is, you will create a model of the form
# 
# $$mpg \sim a (displacement)+ b(weight) +c(gear\_ratio) +d$$
# 
# Most of the functions above can be used as-is. Be careful! Each column of your feature matrix will have to be scaled differently before running the `train()` function on it.
# 
# When you do the train/test split, use `p=0.75` and don't change the default value of seed. Train your model using `max_iter=10000` and `lr=0.01`. Finally, make predictions based on the test set, and report your MSE.

# %%
ROW = 0
COLUMN = 1

# %%
X=np.array(cars[['displacement','weight','gear_ratio']])
X = np.append(X, np.ones((X.shape[0], 1)), axis = COLUMN)
y=cars.mpg

# %%
X_train,X_test,y_train,y_test=TrainTestSplit(X,y,0.75)

# %%
#there's some work to do here, because each column of X_train and X_test should be scaled separately (except the one you added)
X_train_scaled = xscaler.scale(X_train[:, :-1])
X_train_scaled = np.append(X_train_scaled, np.ones((X_train_scaled.shape[0], 1)), axis = COLUMN)

X_test_scaled = xscaler.scale(X_test[:, :-1])
X_test_scaled = np.append(X_test_scaled, np.ones((X_test_scaled.shape[0], 1)), axis = COLUMN)

# %%
y_train_scaled=yscaler.scale(y_train)

# %%
max_iter = 10000
lr = 0.01
coeff=train(X_train_scaled,y_train_scaled,max_iter,lr)

# %%
pred_scaled=predict(X_test_scaled,coeff)

# %%
pred=yscaler.unscale(pred_scaled)

# %%
MSE=np.sum((pred-y_test)**2)/len(y_test)


