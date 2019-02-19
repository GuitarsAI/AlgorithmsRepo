#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Display
import matplotlib.pyplot as plt
from IPython.core.display import HTML, display

# Logging & Debbuging
import logging

# Data
import json


# In[2]:


# Logging Configuration
import sys
# Create logger
logging.basicConfig(format='%(levelname)s : %(message)s', level=logging.INFO)
logger = logging.getLogger()

# Create STDERR handler
handler = logging.StreamHandler(sys.stderr)

# Set STDERR handler as the only handler 
logger.handlers = [handler]


# In[3]:


# Function to Display a Website
def show_web(url):
    html_code='<center><iframe src="%s" width="800" height="600" frameborder="0" marginheight="0" marginwidth="0">Loading...</iframe></center>' 		% (url)
    display(HTML(html_code))


# In[4]:


show_web("https://en.wikipedia.org/wiki/Merge_sort")


# In[5]:


# Define function split
def split(a_list):
    logger.info("\n--Inside function split(%s)"%a_list)
    middle_ind=len(a_list)//2
    logger.info("  Calculate the index of the middle point: %d."%middle_ind)
    logger.info("  Returning the ouput %s."%[a_list[:middle_ind], a_list[middle_ind:]])
    logger.info("--Exiting function split(%s)"%a_list)
    return a_list[:middle_ind], a_list[middle_ind:]


# In[6]:


# Test function split
split([1,2,3])


# In[7]:


# Define Merge Function
def merge(lList,rList):
    logger.info("\n++Inside function merge(%s,%s)."%(str(lList),str(rList)))
    lInd=0
    rInd=0
    result=[]
    for i in range(len(lList)+len(rList)):
        logger.info("    Output Element %d"%i)
        if rInd == len(rList):
            result.append(lList[lInd])
            lInd+=1
            logger.info("    Case end of rList. Intermediate result: %s."%str(result))
        elif lInd == len(lList):
            result.append(rList[rInd])
            rInd+=1
            logger.info("    Case end of lList. Intermediate result: %s."%str(result))
        elif lList[lInd] < rList[rInd]:
            result.append(lList[lInd])
            logger.info("    Case element from lList %d <= %d element from rList. Intermediate result: %s."%(lList[lInd],rList[rInd],str(result)))
            lInd+=1
        else:
            result.append(rList[rInd])
            logger.info("    Case element from lList %d >= %d element from rList. Intermediate result: %s."%(lList[lInd],rList[rInd],str(result)))
            rInd+=1
    logger.info("    Returning the ouput %s."%str(result))
    logger.info("++Exiting function merge(%s,%s)++\n."%(str(lList),str(rList)))
    return result


# In[8]:


# Test Merge Function
merge([3,4,5,7],[2,4,6])


# In[9]:


# Define MergeSort Function
def mergeSort(aList, counter=0):
    counter+=1
    logger.info("\n******MERGESORT: %d time. mergeSort(%s)"%(counter,aList))
    if len(aList) <=1:
        logger.info("      MERGESORT: Input list length < 1. Returning %s."%aList)
        logger.info("******MERGESORT: Exiting mergeSort(%s)\n"%aList)
        counter+=1
        return aList
    
    logger.info("        MERGESORT: Calling split(%s)."%aList)
    l,r = split(aList)
    logger.info("        MERGESORT: Calling function mergeSort(%s)."%l)
    L = mergeSort(l, counter)
    logger.info("        MERGESORT: Calling function mergeSort(%s)."%r)
    R = mergeSort(r,counter+1)
    counter+=1
    logger.info("        MERGESORT: Returning merge(%s,%s)."%(str(L),str(R)))
    logger.info("******MERGESORT: Exiting mergeSort(%s)\n"%aList)
    return merge(L,R)


# In[10]:


# Test Function mergeSort
mergeSort([2,3,1])


# In[11]:


# Test Function mergeSort
mergeSort([3,6,4,55,4,2,7,1,27])


# In[12]:


REQUEST = json.dumps({
    'path' : {},
    'args' : {}
})


# In[13]:


# GET /sortList
req = json.loads(REQUEST)
args = req['args']

if 'unsorted_list' not in args:
  print(json.dumps({'sortedList': None}))
else:
  # Note the [0] when retrieving the argument.
  # This is because you could potentially pass multiple angles.
  unsorted_list = int(args['unsorted_list'][0])
  sortedList = math.radians(mergeSort(unsorted_list))
  print(json.dumps({'Sorted List:': sortedList}))


# In[14]:


get_ipython().run_line_magic('notebook', '-e RestAPImergeSort.ipynb')


# In[15]:


stop


# In[16]:


import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 0))
addr = s.getsockname()
print (addr[1])
s.close()


# In[17]:


get_ipython().run_line_magic('notebook', '-e RestAPImergeSort.py')


# In[18]:


get_ipython().run_line_magic('notebook', '-e test.py')

