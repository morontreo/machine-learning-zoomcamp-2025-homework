#!/usr/bin/env python
# coding: utf-8

# In[10]:


# Importing the lambda_handler from the function
from lambda_function import lambda_handler


# In[11]:


# Testing using the image of the first questions
mock_event = {
    "url": "https://habrastorage.org/webt/yf/_d/ok/yf_dokzqy3vcritme8ggnzqlvwa.jpeg"
}

# Mock Context Object (usually an empty object/dict is sufficient for basic tests)
mock_context = {}


# In[12]:


# Calling the function and printing response
response = lambda_handler(mock_event, mock_context)

print(f"Response Body: {response}")


# In[ ]:




