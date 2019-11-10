#!/usr/bin/env python
# coding: utf-8

# In[20]:


import matplotlib.pyplot as plt
import numpy as np

def plot(xs, ys):
    plt.plot(xs, ys)
    plt.show()


# In[21]:


x = np.arange(0.1, 10, 0.1)
ys = 3 * (x ** -1)


# In[23]:


plot(x, ys)


# In[ ]:




