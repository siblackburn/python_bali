#!/usr/bin/env python
# coding: utf-8

# # K-Means Algorithm

'''Implemtnation for Kmeans clustering algorithm'''


import math
import numpy as np
import pandas as pd
from itertools import cycle

get_ipython().run_line_magic('matplotlib', 'notebook')
import matplotlib.pyplot as plt
            
colors = cycle('bgrcmykw')


# ## Generate random clusters

# In[2]:


# pick random centers
n_clusters = 3
dots_per_cluster = 50
rand_x = np.random.rand(n_clusters)
rand_y = np.random.rand(n_clusters)

x_s = np.array([])
y_s = np.array([])

# for each center, generate multiple points randomly around the center
for i in range(0, n_clusters):    
    center = (rand_x[i], rand_y[i])
    x, y = np.random.multivariate_normal(center, [[.01, 0], [0, .01]], dots_per_cluster).T
    x_s = np.concatenate((x_s, x))
    y_s = np.concatenate((y_s, y))
    
    
# plot the clusters
plt.figure()
plt.scatter(x_s, y_s, s=np.pi*3, alpha=.5)
plt.show()


# ## K-Mean Algorithm

# In[3]:


def dist(x_1, y_1, x_2, y_2):
    return math.sqrt(math.pow(x_2-x_1 ,2) + math.pow(y_2-y_1 ,2))


# In[4]:


def assign_points_to_centroids(k, centroid_x_s, centroid_y_s, x_s, y_s):
    points_by_centroid = { i: [] for i in range(0, k) }
    for i in range(0, len(x_s)):
        #the above iterates over all points in the plot
        # compute the distance to each centroid. So each point has 3 distances calculated for it.
        distances = [dist(x_s[i], y_s[i], centroid_x_s[c_i], centroid_y_s[c_i]) for c_i in range(0, k)]
        closest_centroid_index = np.argmin(distances)
        #closest centroid index then calculates the minimum distance so we can find which cluster the point belongs to
        
        # add point to closest centroid
        points_by_centroid[closest_centroid_index].append(i)
    return points_by_centroid


def plot_state(k, x_s, y_s, centroid_x_s, centroid_y_s):
    points_by_centroid = assign_points_to_centroids(k, centroid_x_s, centroid_y_s, x_s, y_s)
    
    # plot assignments
    plt.figure()
    for centroid_idx, point_indices in points_by_centroid.items():
        
        c = next(colors)

        # plot the centroid
        plt.plot(centroid_x_s[centroid_idx], centroid_y_s[centroid_idx], marker='P', color=c)
        
        plt.scatter(np.take(x_s, point_indices), np.take(y_s, point_indices), s=np.pi*3, color=c, alpha=.5)
    plt.show()
    

def recompute_centroids(k, x_s, y_s, centroid_x_s, centroid_y_s):
    points_by_centroid = assign_points_to_centroids(k, centroid_x_s, centroid_y_s, x_s, y_s)
    
    for idx, point_indices in enumerate(points_by_centroid.values()):
        if len(point_indices) == 0:
            print('lost an index')
        centroid_x_s[idx] = np.mean(np.take(x_s, point_indices))
        centroid_y_s[idx] = np.mean(np.take(y_s, point_indices))
        #the above calculates new x_y coordinate of centroid. Which is the mean of all the x's and y's coordinates that belong to that centroid
        
def k_means(k, x_s, y_s, iterations=10): #k=how many clusters. Iterations = how many times to we want to cluster
    centroid_x_s = np.random.rand(k)
    centroid_y_s = np.random.rand(k)
    
    for i in range(0, iterations):
        print(f'iter  {i+1}')
        recompute_centroids(k, x_s, y_s, centroid_x_s, centroid_y_s)
    return centroid_x_s, centroid_y_s
    


# In[5]:


k = 3
centroid_x_s, centroid_y_s = k_means(k, x_s, y_s)

plot_state(k, x_s, y_s, centroid_x_s, centroid_y_s)


# ## Initialize K-Means with farthest apart points

# In[6]:


# source: https://codereview.stackexchange.com/questions/179561/farthest-point-algorithm-in-python
def calc_distances(p0, points):
    return ((p0 - points)**2).sum(axis=1)

def farthest_points(pts, K):
    farthest_pts = np.zeros((K, 2))
    farthest_pts[0] = pts[np.random.randint(len(pts))]
    distances = calc_distances(farthest_pts[0], pts)
    for i in range(1, K):
        farthest_pts[i] = pts[np.argmax(distances)]
        distances = np.minimum(distances, calc_distances(farthest_pts[i], pts))
    return farthest_pts


# In[7]:


farthest_pts = farthest_points(np.dstack((x_s, y_s))[0], 3)

centroid_x_s = farthest_pts.T[0]
centroid_y_s = farthest_pts.T[1]

plot_state(k, x_s, y_s, centroid_x_s, centroid_y_s)


# In[9]:


def k_means_modified(k, x_s, y_s, iterations=10):
    
    farthest_pts = farthest_points(np.dstack((x_s, y_s))[0], k)

    centroid_x_s = farthest_pts.T[0]
    centroid_y_s = farthest_pts.T[1]
    
    
    for i in range(0, iterations):
        print(f'iter  {i+1}')
        recompute_centroids(k, x_s, y_s, centroid_x_s, centroid_y_s)
    return centroid_x_s, centroid_y_s


# In[10]:


k = 3
centroid_x_s, centroid_y_s = k_means_modified(k, x_s, y_s)

plot_state(k, x_s, y_s, centroid_x_s, centroid_y_s)


# ## Let's do something useful: plot earthquake centers!

# In[11]:


get_ipython().system('pip install shapely')
get_ipython().system('pip install geopandas')
get_ipython().system('pip install descartes')


# In[12]:


from shapely.geometry import Point
import geopandas as gpd
from geopandas import GeoDataFrame


# In[14]:


csv = pd.read_csv('./data/quakes.csv')


# In[15]:


csv.head()


# In[16]:


geometry = [Point(xy) for xy in zip(csv['longitude'], csv['latitude'])]
gdf = GeoDataFrame(csv, geometry=geometry)   
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
gdf.plot(ax=world.plot(figsize=(10, 6)), marker='o', color='red', markersize=15);


# ## Let's find the top 10 earthquake centers!

# In[17]:


k = 10
centroid_x_s, centroid_y_s = k_means_modified(k, csv['longitude'].values, csv['latitude'].values)

df = pd.DataFrame(list(range(0, k)), columns = ['Centroid Idx'])

geometry = [Point(xy) for xy in zip(centroid_x_s, centroid_y_s)]
gdf = GeoDataFrame(df, geometry=geometry)   
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
gdf.plot(ax=world.plot(figsize=(10, 6)), marker='P', color='red', markersize=30);


# In[ ]:




