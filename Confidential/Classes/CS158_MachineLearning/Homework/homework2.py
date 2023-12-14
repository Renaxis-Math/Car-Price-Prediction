# %% [markdown]
# **Homework 2**

# %% [markdown]
# We begin with the usual imports.

# %%
import numpy as np
import pandas as pd

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# %% [markdown]
# Now load the iris dataset.

# %%
iris = pd.read_csv("https://vincentarelbundock.github.io/Rdatasets/csv/datasets/iris.csv",index_col=0)
iris.head(5)

# %% [markdown]
# Define `data` to be a DataFrame containing the `Petal.Length` and `Petal.Width` of the flowers in the iris dataset. Define `target` to be a Pandas Series containing the `Species` column.

# %%
data = iris[["Petal.Length", "Petal.Width"]].reset_index(drop=True)
target = iris.Species

# %% [markdown]
# Define a function `sq_distances` with inputs `data` (a DataFrame of known Petal Lengths and Petal Widths), `length` and `width` (the Petal Length and Petal Width of an unknown flower). The function should return a Pandas series of squared distances from the unknown point to each point in `data`. Use Pandas and/or Numpy operations. DO NOT USE A FOR LOOP.

# %%
def sq_distances(data,length,width):
  return pd.Series(np.linalg.norm(data - (length, width), axis=1))

# %% [markdown]
# Define a function `SpeciesOfNeighbors` that gives the Species of the k nearest neighbors from the point with given Petal Length and Petal Width to the points in `data`. (The list of species for each point in `data` is contained in the Series `target`.)

# %%
def SpeciesOfNeighbors(data,target,x,y,k):
  distances = sq_distances(data, x, y)
  distances_species_df = pd.concat([target, distances], axis=1, keys=['Species', 'Distance']).sort_values('Distance')

  return distances_species_df['Species'][:k]

# %% [markdown]
# Create a function `prediction` that takes a Pandas Series of labels, and returns the label that appears the most often. (Hint: The Pandas Series function `value_counts()` will be useful here.

# %%
def prediction(labels):
  most_frequen_labelID = labels.value_counts(sort=False).argmax()
  return list(labels)[0]

# %% [markdown]
# Create a function `KNN` which takes a DataFrame `data` of known Petal Lengths and Petal Widths, a Series `target` containing their species, a hyperparameter `k`, and the `length` and `width` of the petal of an unknown flower. Your function should return the most common species among the k nearest neighbors of the unknown flower.

# %%
def KNN(data,target,x,y,k):
  nearest_neighbor_ids = SpeciesOfNeighbors(data, target, x, y, k)
  return prediction(nearest_neighbor_ids)

# %% [markdown]
# Test your code here (it should return 'setosa'):

# %%
KNN(data,target,1.4,0.2,3)


