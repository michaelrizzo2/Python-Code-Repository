
# coding: utf-8

# In[2]:

import matplotlib


# In[3]:

from math import *


# In[4]:

matplotlib.use("Agg")


# In[5]:

import numpy as np


# In[6]:

import matplotlib.pyplot as plt


# In[7]:

import matplotlib.animation as manimation


# In[8]:

FFMpegWriter=manimation.writers["ffmpeg"]


# In[9]:

metadata=dict(title="Movie Test")


# In[10]:

my_writer=FFMpegWriter(fps=30,metadata=metadata)


# In[11]:

my_figure=plt.figure()


# In[11]:




# In[12]:

plt.xlim(-10,10)


# In[13]:

plt.ylim(-10,10)


# In[16]:

with my_writer.saving(my_figure,"my_test2.mp4",100):
    for i in range(90):
        x=0.1*i
        y=0.1*i
        plt.plot(x,y,'k-o')
        my_writer.grab_frame()
plt.clf()


# In[15]:




# In[ ]:



