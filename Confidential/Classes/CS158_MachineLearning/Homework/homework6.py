# %% [markdown]
# **Homework 6**
# 

# %%
import pandas as pd
import numpy as np

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# %% [markdown]
# *Problem 1.*
# 
# Let $f(x,y)=x^2+2xy+2y^2-4x-4y$.
# 
# Calculate  $\nabla f(x,y)$, the gradient of $f(x,y)$ on paper. (No need to turn this in, but you'll need it for the next parts of the problem.) In this problem you will use the gradient to find the minimum of $f(x,y)$. Do this first on paper by setting the gradient equal to $\langle 0,0 \rangle$ and solving for $x$ and $y$, so you can check that gradient descent is giving you the right answer.
# 

# %% [markdown]
# Next, write a function fGD which implements gradient descent to find the minimum of $f(x,y)$. Your function should take in the following parameters:
# * `lr` (learning rate)
# * `max_iter` (maximum number of iterations)
# * `x_init` (initial value of x)
# * `y_init` (initial value of y)
# 
# Your function should return the final values of x and y

# %%
def fGD(lr,max_iter,x_init,y_init):
  x = x_init
  y = y_init
  
  for i in range(max_iter):
    gradient = (2*x + 2*y - 4, 2*x + 4*y - 4)
    x = x - lr * gradient[0]
    y = y - lr * gradient[1]

  return x,y

# %% [markdown]
# Now run this to check you answer. Is it what you expect?

# %%
fGD(0.0001,10000,5,5)

# %% [markdown]
# *Problem 2*
# 
# Write a function GD which implements gradient descent to find the slope `m` and intercept `b` for a linear model relating a numpy array y to a numpy array x.
# 
# Your function should take in the following parameters:
# * x (A numpy array of values)
# * y (The target numpy array of values)
# * `lr` (learning rate)
# * `max_iter` (maximum number of iterations)
# * `m_init` (initial slope)
# * `b_init` (initial intercept)
# 
# Your function should return the slope and intercept found by gradient descent.

# %%
def GD(x,y,lr,max_iter,m_init,b_init):
  m = m_init
  b = b_init
  n = len(x) 
  
  for iteration in range(max_iter):
      y_pred = m * x + b
      
      dm = (-2/n) * np.sum(x * (y - y_pred))
      db = (-2/n) * np.sum(y - y_pred)      
      
      m -= lr * dm
      b -= lr * db
      
  return m, b

# %% [markdown]
# You can test your code here. Is the result close to what you would expect?

# %%
x=np.arange(10)
y=3*x+2
GD(x,y,.001,1000,1,1)

# %% [markdown]
# Problem 3.
# 
# Recall the speed vs distance modification of the `flights` dataset we created in Homework 5:

# %%
flights=pd.read_csv("https://vincentarelbundock.github.io/Rdatasets/csv/nycflights13/flights.csv")
flights=(
    flights[['tailnum','distance','air_time']][pd.notna(flights['air_time'])].
    assign(speed=lambda x:60*x.distance/x.air_time).
    groupby('tailnum').
    agg('mean').
    sort_values('distance',ascending=False)[32:]
)

# %% [markdown]
# To make things a little easier, we'll define separate `distance` and `speed` arrays:

# %%
distance=np.array(flights.distance)
speed=np.array(flights.speed)

# %% [markdown]
# In Homework 5 you created a linear model of `speed` vs `distance` using the normal equations, and should have ended up with an RSS of about 1843267. The normal equations guarantee that this is the best possible, but for larger datasets they can be very slow to implement.
# 
# In this problem you will do this again using the GD function defined in the previous problem. Unfortunately, just applying this to x=distance and y=speed may not work, since distance and speed are on such different scales. To compensate, first write a function with inputs x, y, lr, max_iter, m_init, and b_init that does the following:
# 
# 1. Rescales the input values of x and y to obtain arrays of values x_scaled and y_scaled between 0 and 1
# 2. Calls GD on x_scaled, y_scaled, lr, max_iter, m_init, and b_init
# 3. Uses the resulting slope and intercept to find values pred_scaled from x_scaled
# 4. Returns re-scaled values of pred_scaled so that the resulting array is a linear approximation of y.
# 

# %%
def PredictWithRescaling(x,y,lr,max_iter,m_init,b_init):
  scaled_x = x / (max(x) - min(x))
  scaled_y = y / (max(y) - min(y))
  
  m, b = GD(scaled_x, scaled_y, lr, max_iter, m_init, b_init)
  pred_scaled = m * scaled_x + b
  
  predictions = pred_scaled * (max(y) - min(y))

  return predictions

# %% [markdown]
# The following code block uses your PredictWithRescaling function to create predictions based on `distance` and `speed` with a learning rate of 0.0001 and just 100 iterations. How close does it get to the minimum possible RSS? What if you change this to 200 iterations?

# %%
pred=PredictWithRescaling(distance,speed,0.0001,200,1,1)
RSS=np.sum((speed-pred)**2)
RSS


