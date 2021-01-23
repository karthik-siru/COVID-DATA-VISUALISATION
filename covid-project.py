#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
import chart_studio.plotly as py 
import plotly.offline as po
import plotly.graph_objs as pg 
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


po.init_notebook_mode(connected=True)


# In[3]:


csv_file = pd.read_csv('project.csv')


# In[4]:


csv_file


# In[5]:


data = dict(type = 'choropleth', 
         geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
          featureidkey='properties.ST_NM',
          locationmode='geojson-id',
          locations=csv_file['state'],
            z =csv_file['deaths'], 
            text = csv_file['text'],
          colorbar = {'title' : 'COVID - DEATHS ' }  ,
          colorscale='Reds'
            
           )


# In[6]:


layout = dict(geo = dict(scope= 'asia'))


# In[7]:


x = pg.Figure(data = [data] , layout = layout)


# In[8]:


po.plot(x)


# In[9]:


data1= dict(type = 'choropleth', 
          geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
          featureidkey='properties.ST_NM',
          locationmode='geojson-id',
          locations=csv_file['state'],
            z =csv_file['recovered'], 
            text = csv_file['text'], 
            colorbar = {'title' : 'COVID - RECOVERED - CASES' }  ,
            colorscale='Greens'
           )


# In[10]:


layout =  dict(geo = dict(scope= 'asia'))


# In[11]:


y =   pg.Figure(data = [data1] , layout = layout)


# In[12]:


po.plot(y)


# In[43]:


data2= dict(type = 'choropleth', 
          
          geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
          featureidkey='properties.ST_NM',
          locationmode='geojson-id',
          locations=csv_file['state'],
            z =csv_file['Active-cases'], 
            text = csv_file['text'], 
            colorbar = {'title' : 'COVID - RECOVERED - CASES' }  ,
            colorscale='Greens'
           )


# In[44]:


layout =  dict(geo = dict(scope= 'asia'))


# In[45]:


z = pg.Figure(data=[data2], layout = layout)


# In[46]:


po.plot(z)


# In[ ]:




