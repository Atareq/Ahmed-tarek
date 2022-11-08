#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pyopenms import*


# In[3]:


seq=AASequence.fromString("VAKA")
seq_wz_MonoWeight=seq.getMonoWeight()
seq_monoweight_2=seq.getMonoWeight(Residue.ResidueType.Full,2)
mz=seq.getMZ(2)


# In[5]:


print(f"The {seq}  With MonoWeight  is {seq_wz_MonoWeight}")
print(f"The Peptide With MonoWeight and 2H is {seq_monoweight_2} and The MZ ==> {mz}")


# In[6]:


print(f" {seq} Are Consist of :")
resultOfAllMonoWeight=0
for i in seq:
    print(i.getName()+" => "+str(i.getMonoWeight()))
    resultOfAllMonoWeight+=i.getMonoWeight()


# In[9]:


print(f"The Sum of All Amino Acid (VAKA) is {resultOfAllMonoWeight}")


# In[10]:


print(f"Is The VAKA == V + A + K + A ? {bool(seq_monoweight_2==resultOfAllMonoWeight)}")


# In[ ]:




