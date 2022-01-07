#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
df = pd.read_csv('partner.csv')
df1 = pd.read_csv('metadata.csv')
df2 = pd.read_csv('balance.csv')
df3 = pd.read_csv('sellers.csv')


# In[2]:


df.columns = [c.lower() for c in df.columns] #postgres doesn't like capitals or spaces
from sqlalchemy import create_engine
engine = create_engine('postgresql://nada:nada@localhost:5432/testdb')
df.to_sql("partner", engine)


# In[8]:


df1.columns = [c.lower() for c in df1.columns] #postgres doesn't like capitals or spaces

from sqlalchemy import create_engine
engine = create_engine('postgresql://nada:nada@localhost:5432/testdb')

df1.to_sql("metadata", engine)


# In[9]:


df2.columns = [c.lower() for c in df2.columns] #postgres doesn't like capitals or spaces

from sqlalchemy import create_engine
engine = create_engine('postgresql://nada:nada@localhost:5432/testdb')

df2.to_sql("balance", engine)


# In[10]:


df3.columns = [c.lower() for c in df3.columns] #postgres doesn't like capitals or spaces

from sqlalchemy import create_engine
engine = create_engine('postgresql://nada:nada@localhost:5432/testdb')

df3.to_sql("sellers", engine)


# In[4]:


resultat = df.groupby('partner')['seller_id'].nunique()


# In[5]:


resultat


# In[6]:


resultat.agg({'Le nombre total des partenaires est': pd.Series.nunique})


# In[7]:


df3[df3.duplicated()].head()


# In[8]:


print('Le nombre total des vendeurs est: ' ,len(df3.index))


# In[9]:


df2_inactif = df2[(df2['debit'] == 0) & (df2['credit'] == 0)]


# In[10]:


df2_inactif


# In[11]:



result = df2_inactif.groupby('name')['seller_id'].nunique()
result


# In[12]:


print('Le nombre total des vendeurs inactifs est: ' ,len(df2_inactif.index))


# In[13]:


df2


# In[18]:


df2.drop( df2[ (df2['debit'] == 0) & (df2['credit'] == 0) ].index, inplace=True)


# In[19]:


print('Le nombre total des vendeurs actifs est: ' ,len(df2.index))


# In[22]:


resu = df2.groupby('name')['seller_id'].nunique()
resu


# In[24]:


tri = df2.sort_values( by=["name", "seller_id"], ascending=[1,0])
tri


# In[25]:


tri['name'].value_counts()


# In[26]:


tri['seller_id'].value_counts()


# In[27]:


tri


# In[28]:


tri[['date','heure']] = tri.date.str.split(" ",expand=True) 
tri


# In[29]:


tri['date'] = pd.to_datetime(tri['date'])
tri


# In[30]:


tri.sort_values(by='date')


# In[33]:


tri_datetot =tri['name'].loc[tri["date"].isin(pd.date_range('2021-11-25', '2021-12-31'))]
z = tri_datetot.value_counts()
z


# In[34]:


tri_datenov =tri['name'].loc[tri["date"].isin(pd.date_range('2021-11-25', '2021-11-30'))]
x = tri_datenov.value_counts()
x


# In[35]:



print('Le nombre total des transaction pour la période de moi de Novembre 2021 est: ' ,len(tri_datenov.index))
print('le patenaires le plus fidéle pour la période de Novembre est', x.argmax(), 'avec un nombre de transaction', x.max())
print('La moyenne de ',len(tri_datenov.index)/6,'par jour')


# In[36]:


tri_date =tri['name'].loc[tri["date"].isin(pd.date_range('2021-12-01', '2021-12-31'))]
y=tri_date.value_counts()
y


# In[37]:


print('Le nombre total des transaction pour le moi Décembre 2021 est: ' ,len(tri_date.index))
print('le patenaires le plus fidéle en moi de décembre est', z.argmax(), 'avec un nombre de transaction', z.max())
print('La moyenne de ',len(tri_date.index)/31,'par jour')


# In[38]:


tri_date11 =tri['name'].loc[tri["date"].isin(pd.date_range('2021-11-19', '2021-11-25'))]
a = tri_date11.value_counts()
a


# In[39]:



tri_date1 =tri['name'].loc[tri["date"].isin(pd.date_range('2021-11-26', '2021-12-02'))]
b = tri_date1.value_counts()
b


# In[40]:



tri_date2 =tri['name'].loc[tri["date"].isin(pd.date_range('2021-12-03', '2021-12-09'))]
c = tri_date2.value_counts()
c


# In[41]:



tri_date3 =tri['name'].loc[tri["date"].isin(pd.date_range('2021-12-10', '2021-12-16'))]
d = tri_date3.value_counts()
d


# In[42]:



tri_date4 =tri['name'].loc[tri["date"].isin(pd.date_range('2021-12-17', '2021-12-22'))]
e = tri_date4.value_counts()
e


# In[43]:



tri_date5 =tri['name'].loc[tri["date"].isin(pd.date_range('2021-12-23', '2021-12-31'))]
f = tri_date5.value_counts()
f


# In[44]:


print('Le nombre total des transaction pour la période 2021-11-19, 2021-11-25 est: ' ,len(tri_date11.index),'transactions')
print('le patenaires le plus fidéle pour cette période est', a.argmax(), 'avec un nombre de transaction', a.max())
print('La moyenne des transactions effectués pour cette période est',len(tri_date11.index)/7,'par jour')


# In[45]:


print('Le nombre total des transaction pour la période 2021-11-26, 2021-12-02 est: ' ,len(tri_date1.index),'transactions')
print('le patenaires le plus fidéle pour cette période est', b.argmax(), 'avec un nombre de transaction', b.max())
print('La moyenne des transactions effectués pour cette période est',len(tri_date1.index)/7,'par jour')


# In[46]:


print('Le nombre total des transaction pour la période 2021-12-03, 2021-12-09 est: ' ,len(tri_date2.index),'transactions')
print('le patenaires le plus fidéle pour cette période est', c.argmax(), 'avec un nombre de transaction', c.max())
print('La moyenne des transactions effectués pour cette période est',len(tri_date2.index)/7,'par jour')


# In[47]:


print('Le nombre total des transaction pour la période 2021-12-10, 2021-12-16  est: ' ,len(tri_date3.index),'transactions')
print('le patenaires le plus fidéle pour cette période est', d.argmax(), 'avec un nombre de transaction', d.max())
print('La moyenne des transactions effectués pour cette période est',len(tri_date3.index)/7,'par jour')


# In[48]:


print('Le nombre total des transaction pour la période 2021-12-17, 2021-12-22 est: ' ,len(tri_date4.index),'transactions')
print('le patenaires le plus fidéle pour cette période  est', e.argmax(), 'avec un nombre de transaction', e.max())
print('La moyenne des transactions effectués pour cette période est' ,len(tri_date4.index)/7,'par jour')


# In[49]:


print('Le nombre total des transaction pour la période 2021-12-23 au 2021-12-31  est: ' ,len(tri_date5.index),'transactions')
print('le patenaires le plus fidéle pour cette période est', f.argmax(), 'avec un nombre de transaction', f.max())
print('La moyenne des transactions effectués pour cette période est',len(tri_date5.index)/7,'par jour')


# In[51]:


count = tri.groupby(tri['date'].dt.date).size()
count


# In[52]:


print('nombre des jours total est : ', len(pd.to_datetime(tri['date']).dt.date.unique()), 'jours')


# In[53]:


print('la moyenne générale des transactions  est', (len(tri.index))/(len(pd.to_datetime(tri['date']).dt.date.unique())),'transactions par jour')


# In[ ]:




